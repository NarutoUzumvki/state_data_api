from flask import Blueprint, request, jsonify
from datetime import timedelta
import traceback

from utils.auth import (authenticate_user, create_access_token, 
    validate_json, get_current_user, expire_token)

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/token")
@validate_json(['username', 'password'])
def login_for_access_token():
    try:
        data = request.json
        username = data.get("username")
        password = data.get("password")
    except Exception as error:
        traceback.print_exc()
        return jsonify({"error": "Something went wrong"}), 400

    user = authenticate_user(username, password)
    if not user:
        return jsonify({"error": "Could not validate user"}), 400
    token = create_access_token(user.username, user.id, user.role, timedelta(minutes=20))

    return jsonify({'access_token': token, 'token_type': 'Bearer'}), 200

@auth_bp.route("/api_key")
@validate_json(['username', 'password'])
def login_for_api_key():
    try:
        data = request.json
        username = data.get("username")
        password = data.get("password")
    except Exception as error:
        traceback.print_exc()
        return jsonify({"error": "Something went wrong"}), 400
        
    user = authenticate_user(username, password)
    if not user:
        return jsonify({"error": "Could not validate user"}), 400
        
    return jsonify({"api_key": user.api_key}), 200

@auth_bp.route("/logout", methods=["POST"])
def logout():
    token = request.headers.get('Authorization', '').split('Bearer ')[-1]
    if not token:
        return jsonify({"error": 'Token is missing'}), 401
    else:
        expire_token(token)
        return jsonify({'message': "Logged Out"}), 200