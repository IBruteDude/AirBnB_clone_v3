#!/usr/bin/python3
"""handle routes to the states api endpoint"""
from flask import request
from models import storage
from models.state import State
from app import app


@app.route('/api/v1/states/<state_id>', methods=['GET', 'DELETE', 'POST', 'PUT'])
def states_handler(state_id=None):
    match(request.method):
        case 'GET':
            storage.get(State, state_id)
        case 'DELETE':
            pass
        case 'POST':
            pass
        case 'PUT':
            pass

"""
Create a new view for State objects that handles all default RESTFul API actions:

In the file api/v1/views/states.py
You must use to_dict() to retrieve an object into a valid JSON
Retrieves the list of all State objects: GET /api/v1/states

Retrieves a State object: GET /api/v1/states/<state_id>

If the state_id is not linked to any State object, raise a 404 error
Deletes a State object:: DELETE /api/v1/states/<state_id>

If the state_id is not linked to any State object, raise a 404 error
Returns an empty dictionary with the status code 200
Creates a State: POST /api/v1/states

You must use request.get_json from Flask to transform the HTTP body request to a dictionary
If the HTTP body request is not valid JSON, raise a 400 error with the message Not a JSON
If the dictionary doesn’t contain the key name, raise a 400 error with the message Missing name
Returns the new State with the status code 201
Updates a State object: PUT /api/v1/states/<state_id>

If the state_id is not linked to any State object, raise a 404 error
You must use request.get_json from Flask to transform the HTTP body request to a dictionary
If the HTTP body request is not valid JSON, raise a 400 error with the message Not a JSON
Update the State object with all key-value pairs of the dictionary.
Ignore keys: id, created_at and updated_at
Returns the State object with the status code 200
"""
