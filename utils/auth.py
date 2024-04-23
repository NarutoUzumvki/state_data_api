from flask import request, jsonify
from jose import jwt, JWTError
from jose.exceptions import ExpiredSignatureError
from datetime import datetime, timedelta
from functools import wraps
import time
import redis
import bcrypt

from params import SECRET_KEY, ALGORITHM
from db_operations.users import get_user_by_username
from db_operations.redis_operations import (check_usage_limit, 
    add_jwt_to_redis, check_jwt_expiration, expire_jwt)


def get_current_user(func):
    @wraps(func)                # wraps preserves metadata of the "func"
    def wrapped(*args, **kwargs):
        token = request.headers.get('Authorization', '').split('Bearer ')[-1]
        
        if not token:
            return jsonify({"error": 'Token is missing'}), 401

        try:
            if not check_jwt_expiration(token):
                return jsonify({"error": 'Token has expired'}), 401
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username = payload.get('sub')
            user_id = payload.get('id')
            role = payload.get('role')
            if username is None or user_id is None:
                return jsonify({"error": 'Authentication Failed'}), 401
            current_user = {'username': username, 'id': user_id, 'role': role}
        except ExpiredSignatureError:
            return jsonify({"error": 'Token has expired'}), 401
        except JWTError:
            return jsonify({"error": 'Invalid token'}), 401

        return func(current_user, *args, **kwargs)

    return wrapped


def expire_token(token):
    expire_jwt(token)


def validate_json(required_fields):
    def decorator(func):
        @wraps(func)    # Preserves metadata of the original "func"
        def wrapped(*args, **kwargs):
            json_data = request.get_json()
            if not json_data:
                return jsonify({"error": "JSON payload not provided"}), 400

            missing_fields = [field for field in required_fields if field not in json_data]
            if missing_fields:
                return jsonify({"error": f"Missing required field(s) [{', '.join(missing_fields)}]"}), 400

            return func(*args, **kwargs)

        return wrapped 
    return decorator


def validate_api_key(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        api_key = request.json.get('api_key')
        if not api_key:
            return jsonify({"error": "'api_key' is a required field'"}), 401

        usage_limit = check_usage_limit(api_key)
        if usage_limit == -1:
            return jsonify({"error": "Invalid 'api_key''"}), 401
        
        if not usage_limit:
            return jsonify({"error": "rate limit exceeded"}), 400
        
        return func(*args, **kwargs)
         
    return wrapped 


def create_access_token(username: str, user_id: int, role: str, expires_delta: timedelta):
    data = {'sub': username, 'id': user_id, 'role': role}
    # expires = datetime.utcnow() + expires_delta
    # encode.update({'exp': expires})
    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    add_jwt_to_redis(token, ttl=expires_delta)
    return token


# def get_current_user(token):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username = payload.get('sub')
#         user_id = payload.get('id')
#         if username is None or user_id is None:
#             return None
#         return {'username': username, 'id': user_id}
#     except JWTError:
#         import traceback 
#         traceback.print_exc()
#         return None


def authenticate_user(username: str, password: str):
    user = get_user_by_username(username)
    if not user:
        return False
    if not bcrypt.checkpw(password.encode('utf-8'), user.hashed_password.encode('utf-8')):
        return False
    return user