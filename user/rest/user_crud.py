from datetime import datetime

from flask import jsonify, request
from sqlalchemy import asc, desc

from user import app
from user.db.model import User, db
from user.db.schema import UserDtoSchema
from user.multi_lang_response.multi_lang_response import response_process
from user.validation.login_validation import register


@app.route("/api/v1/user/register", methods=['POST'])
def create_user():
    data = request.json

    lang = request.args.get("lang")

    validation_result = register.validate(request.json)

    if validation_result.get('success', False) is False:
        return jsonify({
            "errors": [],
            "warnings": [],
            "label_errors": response_process(lang, validation_result.get("error"))
        }), 400

    user = User()

    user.first_name = data['first_name']

    user.mail_id = data['mail_id']

    user.created_date_time = datetime.now()

    user.last_name = data['last_name']

    user.age = data['age']

    db.session.add(user)

    db.session.commit()

    return jsonify({
        "message": response_process(lang, "successfully_registered")
    }), 201


@app.route('/api/v1/user/list', methods=['GET'])
def get_all_users():

    lang = request.args.get("lang")

    if request.args.get('limit') is None or request.args.get('page_number') is None:
        return jsonify({
            "errors": [response_process(lang, "limit&page_number")]
        }), 400

    limit = request.args.get('limit')

    page_number = request.args.get('page_number')

    sort_key = request.args.get('sort_key')

    sort_type = request.args.get('sort_type')

    search_text = request.args.get('search_text')

    count = 0

    if sort_key is None:

        load_by = User.created_date_time

    else:

        load_by = getattr(User, sort_key)

    if sort_type == 'ASC':

        ordering = asc

    else:

        ordering = desc

    to_order = ordering(load_by)

    if search_text is None:

        users = User.query.order_by(to_order).paginate(page=int(page_number),
                                                       per_page=int(limit)).items

        count = User.query.count()

    else:

        users = User.query.order_by(to_order).filter(
            User.id.like(search_text) | User.first_name.like(f'%{search_text}%')).paginate(
            page=int(page_number),
            per_page=int(limit)).items

    user = UserDtoSchema(many=True)

    output = user.dump(users)

    if search_text is not None:
        count = len(output)

    result = {'total Count': count, 'users': output}

    return jsonify(result), 200


@app.route("/api/v1/user/update", methods=['PUT'])
def user_update():
    data = request.json

    lang = request.args.get("lang")

    if data['id'] is None:
        return jsonify({
            "warnings": [],
            "errors": [response_process(lang, "update_id_required")]
        }), 400

    validation_result = register.validate(request.json)

    if validation_result.get('success', False) is False:
        return jsonify({
            "errors": [],
            "warnings": [],
            "label_errors": response_process(lang, validation_result.get("error"))
        }), 400

    user = User.query.filter_by(id=data['id']).first()

    if user is None:
        return jsonify({
            "warnings": [],
            "errors": [response_process(lang, "user_not_found")]
        }), 400

    user.first_name = data['first_name']

    user.mail_id = data['mail_id']

    user.modified_date_time = datetime.now()

    user.last_name = data['last_name']

    user.age = data['age']

    db.session.add(user)

    db.session.commit()

    return jsonify({
        "message": response_process(lang, "user_updated")
    }), 200


@app.route('/api/v1/user/detail', methods=['GET'])
def user_detail():
    lang = request.args.get("lang")

    user_id = request.args.get('user_id')

    if user_id is None:
        return jsonify({
            "warnings": [],
            "label_errors": {},
            "errors": [response_process(lang, "detail_id_required")]
        }), 400

    user = User.query.filter_by(id=user_id).first()

    if user is None:
        return jsonify({
            "warnings": [],
            "label_errors": {},
            "errors": [response_process(lang, "user_not_found")]
        }), 400

    issue_schema = UserDtoSchema()

    output = issue_schema.dump(user)

    return jsonify(output), 200


@app.route("/api/v1/user/delete", methods=['DELETE'])
def user_delete():
    user_id = request.args.get('user_id')

    lang = request.args.get("lang")

    if user_id is None:
        return jsonify({
            "warnings": [],
            "label_errors": {},
            "errors": [response_process(lang, "delete_id_required")]
        }), 400

    user = User.query.filter_by(id=user_id).first()

    if user is None:
        return jsonify({
            "warnings": [],
            "label_errors": {},
            "errors": [response_process(lang, "user_not_found")]
        }), 400

    db.session.delete(user)

    db.session.commit()

    return jsonify({
        "message": response_process(lang, "user_deleted")
    }), 200
