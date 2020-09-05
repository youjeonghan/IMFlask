from flask import Blueprint, request

auth = Blueprint('auth', __name__)


@auth.route("/signup", methods=['POST'])
def index():
	data = request.get_json()
	
