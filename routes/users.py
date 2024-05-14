from flask import Blueprint, jsonify, request
import bcrypt
import sqlalchemy
import traceback

from utils.auth import get_current_user, validate_json
from db_operations.users import *

users_bp = Blueprint('users', __name__)

@users_bp.route("/create", methods = ["POST"])
@validate_json(['username', 'password', 'confirm_password'])
def create_user():
    try:
        data = request.json
        username = data.get("username")
        password = data.get("password")
        password2 = data.get("confirm_password")
        email = data.get("email")
        role = data.get("role", "user")
        if role not in {"admin", "user", "prime"}:
            return jsonify({"error": "Invalid role"}), 400
        if role == "admin":
            return jsonify({"error": "This action requires allevation"}), 400
        if password != password2:
            return jsonify({"error": "Passwords don't match"}), 400
        if len(username) < 4:
            return jsonify({"error": "Username must be atleast 4 characters"}), 400
        if len(password) < 8:
            return jsonify({"error": "Password must be atleast 8 characters"}), 400
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    except:
        traceback.print_exc()
        return jsonify({"error": "Something went wrong"}), 400

    try:
        if role == "prime":
            # Payment Logic
            pass
        new_user = create_new_user(username, hashed_password, email, role)
        user_data = {
            'username': new_user.username, 
            'api_key': new_user.api_key,
            'role': new_user.role
            }
        if new_user.email:
            user_data.update({"email": new_user.email})
        return jsonify(user_data), 201
    except sqlalchemy.exc.IntegrityError:
        return jsonify({"error": f"Username {username} already exists"}), 400
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": "Something went wrong"}), 400


@users_bp.route("/change/password", methods = ["PUT"])
@validate_json(['old_password', 'new_password', 'confirm_password'])
@get_current_user
def change_password(user):
    try:
        data = request.json
        old_password = data.get("old_password")
        new_password = data.get("new_password")
        confirm_password = data.get("confirm_password")
        user_data = get_user_by_id(user.get("id"))
        if not bcrypt.checkpw(old_password.encode('utf-8'), user_data.hashed_password.encode('utf-8')):
            return jsonify({"error": "Incorrect Password"}), 400
        if new_password != confirm_password:
            return jsonify({"error": "Passwords dont match"}), 401
    except:
        traceback.print_exc()
        return jsonify({"error": "Something went wrong"}), 400       

    try:
        hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
        update_password(user.get("id"), hashed_password)
        return jsonify({"message": "Password updated successfully"}), 200
    except:
        traceback.print_exc()
        return jsonify({"error": "Something went wrong"}), 400