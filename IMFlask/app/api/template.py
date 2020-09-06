from flask import Blueprint, render_template
from app.api.decorators import timer

template = Blueprint('template', __name__)


@template.route("/")
def index():
	return render_template('index.html')

@template.route("/500")
def error_test():
    raise RuntimeError('Custom Error')