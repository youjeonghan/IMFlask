from flask import Blueprint

template = Blueprint('template', __name__)


@template.route("/")
def index():
	return "Welcome to IMFlask!"