#!/usr/bin/python3
"""
Module for cities views
"""
from api.v1.views import app_views
from models import storage
from models.city import City
from models.state import State
from flask import abort, jsonify, make_response, request


@app_views.route('/states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def all_cities(state_id):
    """
    Returns all the cities by a given state id
    """
    cities_list = []
    state = storage.get(State, state_id)

    if not state:
        abort(404)

    for city in state.cities:
        cities_list.append(city.to_dict())

    return jsonify(cities_list)


@app_views.route('/cities/<city_id>/', methods=['GET'], strict_slashes=False)
def get_city(city_id):
    """
    Returns a City by its  id
    """
    city = storage.get(City, city_id)
    if not city:
        abort(404)

    return jsonify(city.to_dict())


@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def delete_city(city_id):
    """
    Deletes a city by its id
    """
    city = storage.get(City, city_id)
    if not city:
        abort(404)

    storage.delete(city)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/states/<state_id>/cities', methods=['POST'],
                 strict_slashes=False)
def post_city(state_id):
    """
    Creates a new City
    """
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    data = request.get_json()
    instance = City(**data)
    instance.state_id = state.id
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def put_city(city_id):
    """
    Updates a City
    """
    city = storage.get(City, city_id)
    if not city:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'state_id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(city, key, value)
    storage.save()
    return make_response(jsonify(city.to_dict()), 200)
