from flask import Blueprint, jsonify, request
import sqlalchemy
import traceback
from utils.auth import get_current_user, validate_json, validate_api_key 
from utils.location_and_weather import get_location_coordinates, get_weather_forecast
from db_operations.cities import *

cities_bp = Blueprint('cities', __name__)

@cities_bp.route("/create", methods = ["POST"])
@validate_json(['name', 'state_code'])
@get_current_user
def add_city(user):
    if not user or user["role"] not in {"superuser", "admin"}:
        return jsonify({"error": "Not authorized for this operation"}), 401

    try:
        data = request.json
        name = data.get("name")
        state_code = data.get("state_code")
        state_code = str(state_code).strip()
        if len(state_code) != 2:
            return jsonify({"error": "'state_code' should be of 2 letters only"}), 400
    except:
        traceback.print_exc()
        return jsonify({"error": "Something went wrong"}), 400

    try:
        new_city = add_new_city(name, state_code)
        city_data = {'code': new_city.code, 'name': new_city.name, 'state_code': new_city.state_code}
        return jsonify(city_data), 201
    except sqlalchemy.exc.IntegrityError:
        return jsonify({"error": f"'State' with state_code '{code}' does not exist"}), 400
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": "Something went wrong"}), 400


@cities_bp.route("<string:code>/retrieve", methods=["GET"])
@validate_api_key
def get_city(code):
    try:
        city = get_city_by_code(code)
        if not city:
            return jsonify({"error": f"City with code: {code} does not exist"}), 400
        map_link, lat, lng = get_location_coordinates(f"{city.name}, {city.state_code}")
        weather_forecast = get_weather_forecast(lat, lng)
        city_data = {
            'code': city.code,
            'name': city.name,
            'state_code': city.state_code,
            'map_link': map_link,
            'weather_forecast': weather_forecast
        }
        return jsonify(city_data), 201
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": "Something went wrong"}), 400


@cities_bp.route("/retrieve/all", methods=["GET"])
@get_current_user
def get_all_cities(user):
    if not user or user["role"] not in {"admin", "prime"}:
        return jsonify({"error": "Not authorized for this operation"}), 401

    try:
        cities = return_all_cities()
        formatted_data = [{
            "code": city.code,
            "name": city.name, 
            "state_code": city.state_code
        } for city in cities]
        return jsonify(formatted_data), 201
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": "Something went wrong"}), 400


@cities_bp.route("<string:code>/update", methods=["PUT"])
@validate_json(['name', 'state_code'])
@get_current_user
def update_city(user, code):
    if not user or user["role"] != "admin":
        return jsonify({"error": "Not authorized for this operation"}), 401

    try:
        data = request.json
        state_code = data.get("state_code")
        name = data.get("name")
    except Exception as error:
        traceback.print_exc()
        return jsonify({"error": "Something went wrong"}), 400

    try:
        city = get_city_by_code(code)
        if not city:
            updated_city = add_new_city(name, state_code, code)
            # return jsonify({"error": f"'City' with code '{code}' does not exist"}), 404
        else:
            updated_city = update_existing_city(code, name, state_code)
        city_data = {'code': updated_city.code, 'name': updated_city.name, 'state_code': updated_city.state_code}
        return jsonify(city_data), 201
    except sqlalchemy.exc.IntegrityError:
        return jsonify({"error": f"'State' with state_code '{code}' does not exist"}), 400
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": "Something went wrong"}), 400


@cities_bp.route("<string:code>/delete", methods=["DELETE"])
@get_current_user
def remove_city(user, code):
    if not user or user["role"] != "admin":
        return jsonify({"error": "Not authorized for this operation"}), 401

    try:
        # city = get_city_by_code(code)
        # if not city:
        #     return f"city with code: {code} does not exist", 400
        delete_city(code)
        return jsonify({"error": f"City with code {code} deleted"}), 200
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": "Something went wrong"}), 400