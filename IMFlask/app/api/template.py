'''
Template API
'''
from flask import Blueprint, render_template

template = Blueprint('template', __name__)


@template.route("/")
def index():
    '''index page'''
    return render_template('index.html')


@template.route("/500")
def error_test():
    '''테스트를 위한 강제 에러 발생 URL'''
    raise RuntimeError('Custom Error')
