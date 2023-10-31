#!/usr/bin/python3
"""handle routes to the states api endpoint"""
from flask import request, jsonify, abort
from models import storage
from models.state import State
from api.v1.views import app_views



@app_views.route('/states',
                 methods=['GET'], strict_slashes=False)
def states_getter():
    states = storage.all(State)

    return jsonify([state.to_dict() for state in states.values()]), 200


@app_views.route('/states/<state_id>',
                 methods=['GET'], strict_slashes=False)
def state_getter(state_id):
    result = storage.get(State, state_id)
    if result is None:
        abort(404)
    return jsonify(result.to_dict()), 200

@app_views.route('/states/<state_id>',
           methods=['DELETE'], strict_slashes=False)
def states_deleter(state_id=None):
    if state_id is None:
        abort(404)
    result = storage.get(State, state_id)
    if result is None:
        abort(404)
    storage.delete(result)
    storage.save()
    return jsonify({}), 200

@app_views.route('/states',
           methods=['POST'], strict_slashes=False)
def states_poster():
    json_body = request.get_json()
    if json_body is None:
        abort(400, "Not a JSON")
    if json_body.get("name") is None:
        abort(400, "Missing name")
    new_state = State(name=json_body["name"])
    new_state.save()
    return jsonify(new_state.to_dict()), 201

@app_views.route('/states/<state_id>',
           methods=['PUT'], strict_slashes=False)
def states_putter(state_id):
    result = storage.get(State, state_id)
    if result is None:
        abort(404)
    json_body = request.get_json()
    if json_body is None:
        abort(400, "Not a JSON")
    new_state = State(name="dummy")
    new_state.__dict__.update(**result.to_dict())
    new_state.__dict__.update(**json_body)
    storage.delete(result)
    new_state.save()
    return jsonify(new_state.to_dict()), 200
