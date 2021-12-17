from flask import jsonify

from user import app


@app.errorhandler(404)
def invalid_route(e):
    return jsonify({'message': 'Route not found'})


@app.errorhandler(500)
def invalid_route(e):
    return jsonify({'message': 'Internal server error'})


@app.errorhandler(405)
def invalid_route(e):
    return jsonify({'message': 'Method Not Allowed'})
