#!/usr/bin/python3
"""handle routes to the places api endpoint"""
from flask import request, jsonify, abort
from models import storage
from models.city import City
from models.place import Place
from models.user import User
from api.v1.views import app_views


@app_views.route('/cities/<city_id>/places',
                 methods=['GET'], strict_slashes=False)
def places_getter(city_id):
    """get a list of all stored places"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    return jsonify([place.to_dict() for place in city.places]), 200


@app_views.route('/places/<place_id>',
                 methods=['GET'], strict_slashes=False)
def place_getter(place_id):
    """get a specific stored place based on id"""
    result = storage.get(Place, place_id)
    if result is None:
        abort(404)
    return jsonify(result.to_dict()), 200


@app_views.route('/places/<place_id>',
                 methods=['DELETE'], strict_slashes=False)
def places_deleter(place_id=None):
    """delete a specific stored place based on id"""
    if place_id is None:
        abort(404)
    result = storage.get(Place, place_id)
    if result is None:
        abort(404)
    storage.delete(result)
    storage.save()
    return jsonify({}), 200


@app_views.route('/cities/<city_id>/places',
                 methods=['POST'], strict_slashes=False)
def places_poster(city_id):
    """create a new place in storage"""
    json_body = request.get_json()
    if json_body is None:
        abort(400, "Not a JSON")
    if storage.get(City, city_id) is None:
        abort(404)
    user_id = json_body.get("user_id")
    if user_id is None:
        abort(400, "Missing user_id")
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    name = json_body.get("name")
    if name is None:
        abort(400, "Missing name")
    new_place = Place(name=name, city_id=city_id,
                      user_id=user_id, number_rooms=0,
                      number_bathrooms=0, max_guest=0,
                      price_by_night=0)
    new_place.save()
    return jsonify(new_place.to_dict()), 201

@app_views.route('/places/<place_id>',
                 methods=['PUT'], strict_slashes=False)
def places_putter(place_id):
    """update a specific stored place based on id"""
    result = storage.get(Place, place_id)
    if result is None:
        abort(404)
    json_body = request.get_json()
    if json_body is None:
        abort(400, "Not a JSON")
    new_place = Place(name="dummy", city_id="123",
                      user_id="456", number_rooms=0,
                      number_bathrooms=0, max_guest=0,
                      price_by_night=0)
    new_place.__init__(**result.to_dict())
    new_place.__init__(**json_body)
    storage.delete(result)
    new_place.save()
    return jsonify(new_place.to_dict()), 200
