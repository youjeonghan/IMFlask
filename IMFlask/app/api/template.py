'''
Template API
'''
import time
from flask import Blueprint, render_template, abort
from app.api.decorators import timer

template = Blueprint('template', __name__)


@template.route("/")
def index():
    '''index page'''
    return render_template('index.html')


@template.route("/500")
def error_test():
    '''테스트를 위한 강제 에러 발생 URL'''
    raise RuntimeError('Custom Error')


@template.route("/abort/<int:status_code>")
def abort_test(status_code):
    '''테스트를 위한 강제 에러 발생 URL'''
    abort(status_code)


@template.route("/slow/<int:sec>")
@timer
def slow_test(sec):
    '''테스트를 위한 강제 에러 발생 URL'''
    time.sleep(sec)
    return {}, 204