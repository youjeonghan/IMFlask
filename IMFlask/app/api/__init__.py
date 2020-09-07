'''
API Main Handler
'''
from flask import abort
from app.models.mysql import get_mysql_cur, close_mysql_cur
from app.models.mongodb import get_mongo_cur, close_mongo_cur
from app.models.redis import get_redis_cur, close_redis_cur 


def init_app(app):

    @app.before_first_request
    def before_first_request():
        pass  

    @app.before_request
    def before_request():
        get_mysql_cur(store_g=True)
        get_mongo_cur(store_g=True)
        get_redis_cur(store_g=True) 

    @app.after_request
    def after_request(response):
        return response

    @app.teardown_request
    def teardown_request(exception):
        close_mysql_cur()
        close_mongo_cur()
        close_redis_cur()
    
    @app.teardown_appcontext
    def teardown_appcontext(exception):
        pass


def input_check(data, key, value_type):
    if key not in data:
        abort(400, description="'%s' not in data." % key)
    if not isinstance(data[key], value_type):
        abort(400, description="'%s' must be '%s' type." % (key, str(value_type)))