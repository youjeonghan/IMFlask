from flask import Blueprint, request, g
from app.api.decorators import login_required, admin_required
from app.controllers.user_con import create_user
from app.controllers.user_con import signin
from flask_jwt_extended import get_jwt_identity

auth = Blueprint('auth', __name__)


@auth.route("/signup", methods=['POST'])
def api_signup():
    data = request.get_json()
    if create_user(g.mongo_cur, 
                   data['user_id'],
                   data['user_pw']):
        return {"msg":"success"}
    return {"msg":"already user"}


@auth.route("/signin", methods=['POST'])
def api_signin():
    data = request.get_json()
    result = signin(g.mongo_cur,
                    data['user_id'],
                    data['user_pw'])
    if not result:
        return {'msg':'login Failed'}
    return {
        "msg":"success",
        "result":result
    }


@auth.route("/login_test")
@login_required
def api_login_test():
    return "Hello, " + get_jwt_identity()


@auth.route("/admin_test")
@admin_required
def api_admin_test():
    return "Admin, " + get_jwt_identity()