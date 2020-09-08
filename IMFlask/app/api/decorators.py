'''
API Main Decorator
'''
from functools import wraps
from time import time
from flask import current_app, g
from app.models.mongodb.user import User
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity


def timer(func):
    '''API 시간 측정 데코레이터'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        process_time = time()
        result = func(*args, **kwargs)
        g.process_time = time() - process_time

        if current_app.config['DEBUG']:
            if isinstance(result, tuple):
                result[0]['process_time'] = g.process_time
            else:
                result['process_time'] = g.process_time

        return result
    return wrapper


def login_required(func):
    '''토큰 검증 데코레이터'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        user_id = get_jwt_identity()
        model = User(g.mongo_cur)
        if not user_id or \
           not model.user_id_check(user_id):
            return {"msg": "Bad Access Token"}, 403
        # TO DO: 아예 유저 인포를 던지는게 나을라나?
        g.user_id = user_id
        result = func(*args, **kwargs)
        return result
    return wrapper


def admin_required(func):
    '''토큰 검증 및 관리자 권한 검증 데코레이터'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        user_id = get_jwt_identity()
        model = User(g.mongo_cur)
        if not user_id or \
           not model.user_id_check(user_id) or \
           user_id != current_app.config['ADMIN_ID']:
            return {"msg": "Bad Access Token"}, 403
        # TO DO: 아예 유저 인포를 던지는게 나을라나?
        g.user_id = user_id
        result = func(*args, **kwargs)
        return result
    return wrapper
