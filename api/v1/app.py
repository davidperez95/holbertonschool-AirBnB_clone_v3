#!/usr/bin/python3
"""
This is a comment that is going to change
"""
from api.v1.views import app_views
from models import storage
from flask import Flask, make_response, jsonify
from os import environ


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close(exception):
    """close the storage"""
    storage.close()


@app.errorhandler(404)
def not_found_error(error):
    """
    Error handler for 404 error not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)


if __name__ == "__main__":
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')

    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'

    app.run(host=host, port=port, threaded=True, debug=True)
