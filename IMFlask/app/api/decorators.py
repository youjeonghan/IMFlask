'''
API Main Decorator
'''
from functools import wraps
from flask import current_app, g
from time import time
from app.models.mongodb.user import User
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity

def timer(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        process_time = time()
        result = f(*args, **kwargs)
        process_time = time() - process_time
        
        if current_app.config['DEBUG']:
            if isinstance(result, tuple):
                result[0]['process_time'] = process_time
            else:
                result['process_time'] = process_time
        
        return result
    return wrapper


def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        user_id = get_jwt_identity()
        model = User(g.mongo_cur)
        if not user_id or \
           not model.user_id_check(user_id):
            return {"msg": "Bad Access Token"}, 403
        result = f(*args, **kwargs)
        return result
    return wrapper


def admin_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        user_id = get_jwt_identity()
        model = User(g.mongo_cur)
        if not user_id or \
           not model.user_id_check(user_id) or \
           user_id != current_app.config['ADMIN_ID']:
            return {"msg": "Bad Access Token"}, 403
        result = f(*args, **kwargs)
        return result
    return wrapper