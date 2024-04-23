from flask import Blueprint, jsonify, request
import sqlalchemy
import traceback
from utils.auth import get_current_user, validate_api_key, validate_json
from db_operations.states import *
from db_operations.cities import return_all_cities_by_state_code

states_bp = Blueprint('states', __name__)


@states_bp.route("/create", methods = ["POST"])
@validate_json(['code', 'name', 'capital'])
@get_current_user
def add_state(user):
    if not user or user["role"] not in {"superuser", "admin"}:
        return jsonify({"error": "Not authorized for this operation"}), 401

    try:
        data = request.json
        code = data.get("code")
        name = data.get("name")
        capital = data.get("capital")
        description = data.get("description")
        chief_minister = data.get("chief_minister")
        population = data.get("population")
        area = data.get("area")
        is_ut = bool(request.args.get("is_ut"))
    except Exception as error:
        traceback.print_exc()
        return jsonify({"error": "Something went wrong"}), 400

    try:
        new_state = add_new_state(name, code, description, capital, chief_minister, population, area, is_ut)
        state_data = {
            "code": new_state.code,
            "name": new_state.name, 
            "description": new_state.description, 
            "capital": new_state.capital, 
            "chief_minister": new_state.chief_minister, 
            "population": new_state.population,
            "area": new_state.area
        }
        return jsonify(state_data), 201
    except sqlalchemy.exc.IntegrityError:
        return jsonify({"error": f"{'UT' if is_ut else 'State'} with name '{name}' or code '{code}' already exists"}), 400
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": "Something went wrong"}), 400


@states_bp.route("<string:code>/retrieve", methods=["GET"])
@validate_api_key
def get_state(code):
    try:
        state = get_state_by_code(code)
        is_ut = bool(request.args.get('is_ut'))
        if not state:
            return jsonify({"error": f"{'UT' if is_ut else 'State'} with code '{code}' does not exist"}), 404
        if state.is_ut and not is_ut:
            return jsonify({"error": f"State with code '{code}' does not exist"}), 404
        if not state.is_ut and is_ut:
            return jsonify({"error": f"UT with code '{code}' does not exist"}), 404
        state_data = {
            "code": state.code,
            "name": state.name, 
            "description": state.description, 
            "capital": state.capital, 
            "chief_minister": state.chief_minister, 
            "population": state.population,
            "area": state.area
        }
        return jsonify(state_data), 201
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": "Something went wrong"}), 400


@states_bp.route("/retrieve/all", methods=["GET"])
@get_current_user
def get_all_states(user):
    if not user or user["role"] not in {"admin", "prime"}:
        return jsonify({"error": "Not authorized for this operation"}), 401
    try:
        is_ut = bool(request.args.get('is_ut'))
        states = return_all_states(is_ut=is_ut)
        formatted_data = [{
            "code": state.code,
            "name": state.name, 
            "description": state.description, 
            "capital": state.capital, 
            "chief_minister": state.chief_minister, 
            "population": state.population,
            "area": state.area
        } for state in states]
        return jsonify(formatted_data), 201
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": "Something went wrong"}), 400


@states_bp.route("<string:code>/retrieve/all/cities", methods=["GET"])
@validate_api_key
def get_all_cities_by_state_code(code):
    try:
        state = get_state_by_code(code)
        is_ut = bool(request.args.get('is_ut'))
        if not state:
            return jsonify({"error": f"{'UT' if is_ut else 'State'} with code '{code}' does not exist"}), 404
        if state.is_ut and not is_ut:
            return jsonify({"error": f"State with code '{code}' does not exist"}), 404
        if not state.is_ut and is_ut:
            return jsonify({"error": f"UT with code '{code}' does not exist"}), 404
        cities = return_all_cities_by_state_code(code)
        formatted_data = [{'code': city.code, 'name': city.name} for city in cities]
        return jsonify(formatted_data), 201
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": "Something went wrong"}), 400


@states_bp.route("<string:code>/update", methods=["PUT"])
@validate_json(['name', 'capital'])
@get_current_user
def update_state(user, code):
    if not user or user["role"] != "admin":
        return jsonify({"error": "Not authorized for this operation"}), 401

    try:
        data = request.json
        name = data.get("name")
        description = data.get("description")
        capital = data.get("capital")
        chief_minister = data.get("chief_minister")
        population = data.get("population")
        area = data.get("area") 
        is_ut = bool(request.args.get("is_ut"))
    except sqlalchemy.exc.IntegrityError:
        return jsonify({"error": f"{'UT' if is_ut else 'State'} with name '{name}' already exists"}), 400
    except Exception as error:
        traceback.print_exc()
        return jsonify({"error": "Something went wrong"}), 400
    
    try:
        state = get_state_by_code(code)
        if not state:
            updated_state = add_new_state(name, code, description, capital, chief_minister, population, area, is_ut)
            # return jsonify({"error": f"{'UT' if is_ut else 'State'} with code: '{code}' does not exist"}), 400
        else:
            updated_state = update_existing_state(code, name, description, capital, chief_minister, population, area, is_ut)
        state_data = {
            "code": updated_state.code,
            "name": updated_state.name, 
            "description": updated_state.description, 
            "capital": updated_state.capital, 
            "chief_minister": updated_state.chief_minister, 
            "population": updated_state.population,
            "area": updated_state.area
        }
        return jsonify(state_data), 201

    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": "Something went wrong"}), 400


@states_bp.route("<string:code>/delete", methods=["DELETE"])
@get_current_user
def remove_state(user, code):
    if not user or user["role"] != "admin":
        return jsonify({"error": "Not authorized for this operation"}), 401

    try:
        # state = get_state_by_code(code)
        # if not state:
        #     return jsonify({"error": f"{'UT' if is_ut else 'State'} with code: '{code}' does not exist"}), 400
        is_ut = bool(request.args.get("is_ut"))
        delete_state(code, is_ut=is_ut)
        return jsonify({"message": f"{'UT' if is_ut else 'State'} with code '{code}' deleted"}), 200
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": "Something went wrong"}), 400