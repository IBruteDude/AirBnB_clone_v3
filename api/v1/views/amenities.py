#!/usr/bin/python3
"""handle routes to the amenities api endpoint"""
from flask import request, jsonify, abort
from models import storage
from models.amenity import Amenity
from api.v1.views import app_views


@app_views.route('/amenities',
                 methods=['GET'], strict_slashes=False)
def amenities_getter():
    """get a list of all stored amenities"""
    amenities = storage.all(Amenity)
    return jsonify([amenity.to_dict() for amenity in amenities.values()]), 200


@app_views.route('/amenities/<amenity_id>',
                 methods=['GET'], strict_slashes=False)
def amenity_getter(amenity_id):
    """get a specific stored amenity based on id"""
    result = storage.get(Amenity, amenity_id)
    if result is None:
        abort(404)
    return jsonify(result.to_dict()), 200


@app_views.route('/amenities/<amenity_id>',
                 methods=['DELETE'], strict_slashes=False)
def amenities_deleter(amenity_id=None):
    """delete a specific stored amenity based on id"""
    if amenity_id is None:
        abort(404)
    result = storage.get(Amenity, amenity_id)
    if result is None:
        abort(404)
    storage.delete(result)
    storage.save()
    return jsonify({}), 200


@app_views.route('/amenities',
                 methods=['POST'], strict_slashes=False)
def amenities_poster():
    """create a new amenity in storage"""
    json_body = request.get_json()
    if json_body is None:
        abort(400, "Not a JSON")
    if json_body.get("name") is None:
        abort(400, "Missing name")
    new_amenity = Amenity(name=json_body["name"])
    new_amenity.save()
    return jsonify(new_amenity.to_dict()), 201


@app_views.route('/amenities/<amenity_id>',
                 methods=['PUT'], strict_slashes=False)
def amenities_putter(amenity_id):
    """update a specific stored amenity based on id"""
    result = storage.get(Amenity, amenity_id)
    if result is None:
        abort(404)
    json_body = request.get_json()
    if json_body is None:
        abort(400, "Not a JSON")
    new_amenity = Amenity(name="dummy")
    new_amenity.__init__(**result.to_dict())
    new_amenity.__init__(**json_body)
    storage.delete(result)
    new_amenity.save()
    return jsonify(new_amenity.to_dict()), 200
