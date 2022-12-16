#!/usr/bin/python3
"""
This is a comment
"""
from api.v1.views import app_views
from flask import jsonify
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models import storage
from models.user import User
from models.review import Review


@app_views.route('/status')
def status():
    """
    Status of the API
    """
    return jsonify({'status': 'OK'})

@app_views.route('/stats')
def number_of_objects():
    classes = [Amenity, City, Place, State, User]

    number_objs = {}    
    for check_class in classes:
        number_objs[check_class.__name__] = storage.count(check_class)

    return jsonify(number_objs)
