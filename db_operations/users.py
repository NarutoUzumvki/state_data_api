import secrets
import string

from .redis_operations import add_apikey_to_redis
from database_config import ScopedSession
from models import Users

def create_new_user(username, hashed_password, email, role):
    api_key = create_api_key()
    new_user = Users(
        username=username,
        hashed_password=hashed_password,
        email=email,
        api_key=api_key,
        is_active=True,
        role=role
    )
    add_apikey_to_redis(api_key=api_key, subscription="premium" if role=="prime" else "regular")
    with ScopedSession() as session:
        session.add(new_user)
        session.commit()
        print(f"New User {new_user.username} created")
    return new_user

# def update_user(user_id, new_username, new_email):
#     with ScopedSession() as session:
#         user = get_user_by_id(user_id)
#         user.username = new_username
#         user.email = new_email
#         session.commit()
#     return user

# def check_password(user_id, entered_password):
#     user = session.query(Users).filter(Users.id==user_id).first()
#     if not user:
#         return 
#     if not bcrypt.checkpw(entered_password.encode('utf-8'), user.hashed_password.encode('utf-8')):
#         return False
#     return True

def update_password(user_id, hashed_password):
    with ScopedSession() as session:
        user = session.query(Users).filter(Users.id==user_id).first()
        if not user:
            return
        user.hashed_password = hashed_password
        session.add(user)
        session.commit()
    return user

def get_user_by_username(username):
    with ScopedSession() as session:
        user = session.query(Users).filter(Users.username==username).first()
    return user

def get_user_by_id(user_id):
    with ScopedSession() as session:
        user = session.query(Users).filter(Users.id==user_id).first()
    return user

def delete_user(user_id):
    with ScopedSession() as session:
        session.query(Users).filter(Users.id==user_id).delete()
        session.commit()
    
def create_api_key(length=32):
    characters = string.ascii_letters + string.digits + "!#$&*-?"
    api_key = ''.join(secrets.choice(characters) for i in range(length))
    return api_key