'''
API Main Handler
'''
from flask import abort
from app.models.mysql import get_mysql_cur, close_mysql_cur
from app.models.mongodb import get_mongo_cur, close_mongo_cur
from app.models.redis import get_redis_cur, close_redis_cur


def init_app(app):
    '''api pre handler 초기화'''
    @app.before_first_request
    def before_first_request():
        '''맨 처음 리퀘스트가 오기 전에'''

    @app.before_request
    def before_request():
        '''리퀘스트가 오기 전에'''
        get_mysql_cur(store_g=True)
        get_mongo_cur(store_g=True)
        get_redis_cur(store_g=True)

    @app.after_request
    def after_request(response):
        '''정상 작동시, 리스폰스를 보내기 전에'''
        return response

    @app.teardown_request
    def teardown_request(exception):
        '''비정상 작동시, 리스폰스를 보내기 전에'''
        close_mysql_cur()
        close_mongo_cur()
        close_redis_cur()

    @app.teardown_appcontext
    def teardown_appcontext(exception):
        '''app context가 종료되기 전에'''


def input_check(data, key, value_type):
    '''input 파라미터 인자 검증 함수'''
    if key not in data:
        abort(400, description="'%s' not in data." % key)
    if not isinstance(data[key], value_type):
        abort(400, description="'%s' must be '%s' type." % (key, str(value_type)))
