#!/usr/bin/python3
"""
module comented
"""
from api.v1.views import app_views
from models import storage
from models.state import State
from flask import abort, jsonify, make_response, request


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def all_states():
    """
    Returns all the states
    """
    states = storage.all(State).values()
    states_list = []

    for state in states:
        states_list.append(state.to_dict())

    return jsonify(states_list)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """
    Returns an especific state by its id
    """
    state = storage.get(State, state_id)
    if not state:
        abort(404)

    return(jsonify(state.to_dict()))


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_state(state_id):
    """
    Deletes an state
    """
    state = storage.get(State, state_id)
    if not state:
        abort(404)

    storage.delete(state)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def post_state():
    """
    Creates a new state
    """
    if not request.get_json():
        abort(400, description='Not a JSON')

    if 'name' not in request.get_json():
        abort(400, description='Missing name')

    data = request.get_json()
    instance = State(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def put_state(state_id):
    """
    Updates an state by its id
    """
    state = storage.get(State, state_id)

    if not state:
        abort(404)

    if not request.get_json():
        abort(400, description='Not a JSON')

    data = request.get_json()
    for key, value in data.items():
        setattr(state, key, value)
    storage.save()
    return make_response(jsonify(state.to_dict()), 200)
