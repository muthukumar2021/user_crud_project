from flask_marshmallow import Marshmallow, Schema
from marshmallow import fields

from user import app

ma = Marshmallow(app)


class UserDtoSchema(Schema):
    first_name = fields.String()
    last_name = fields.String()
    id = fields.Integer()
    mail_id = fields.String()
    age = fields.Integer()
