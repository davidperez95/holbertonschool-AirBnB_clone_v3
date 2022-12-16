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

    classes = [Amenity, City, Place, Review, State, User]
    classes_name = ['amenities', 'cities', 'places', 'reviews', 'states', 'users']

    number_objs = {}
    for index in range(len(classes)):
        number_objs[classes_name[index]] = storage.count(classes[index])

    return jsonify(number_objs)
