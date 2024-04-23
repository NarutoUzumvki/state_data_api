from flask import Blueprint, redirect, url_for, jsonify, request
import requests 
import traceback

ut_bp = Blueprint('ut', __name__)

@ut_bp.route("/create", methods = ["POST"])
def add_ut():
    return redirect(url_for('states.add_state', is_ut=1), code=307)
    # try:
    #     data = request.json
    #     data["is_ut"] = 1
    #     response = requests.post(url_for('states.add_state', _external=True), json=data, headers=request.headers)
    #     return response.text
    # except Exception as error:
    #     traceback.print_exc()
    #     return jsonify({"error": "Something went wrong"}), 400    


@ut_bp.route("<string:code>/retrieve", methods=["GET"])
def get_ut(code):
    return redirect(url_for('states.get_state', code=code, is_ut=1), code=307)


@ut_bp.route("<string:code>/retrieve/all/cities", methods=["GET"])
def get_all_cities_by_state_code(code):
    return redirect(url_for('states.get_all_cities_by_state_code', code=code, is_ut=1), code=307)


@ut_bp.route("/retrieve/all", methods=["GET"])
def get_all_ut():
    return redirect(url_for('states.get_all_states', is_ut=1), code=307)               


@ut_bp.route("<string:code>/update", methods=["PUT"])
def update_ut(code):
    return redirect(url_for('states.update_state', code=code, is_ut=1), code=307)    
    #code=307 to preserve request info. Defaults to a get request if it's not provided.


@ut_bp.route("<string:code>/delete", methods=["DELETE"])
def remove_ut(code):
    return redirect(url_for('states.remove_state', code=code, is_ut=1), code=307)