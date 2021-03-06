'''
auth/user controller
'''
from app.models.mysql.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token


def create_user(mongo_cur, user_id, user_pw):
    '''유저 생성 컨트롤러'''
    model = User(mongo_cur)
    if model.user_id_check(user_id):
        return False
    model.create_user(user_id, 
                      generate_password_hash(user_pw))
    return True


def signin(mongo_cur, user_id, user_pw):
    '''유저 회원가입 컨트롤러'''
    model = User(mongo_cur)
    user = model.get_info(user_id)

    if not user:
        return False
    
    elif not check_password_hash(user['pw'], user_pw):
        return False
    
    return {
        "access_token": create_access_token(
            identity=user_id, expires_delta=False)
    }