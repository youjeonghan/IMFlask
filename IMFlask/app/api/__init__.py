'''
API Main Handler
'''
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
        app.logger.warning("asd")
        close_mysql_cur()
        close_mongo_cur()
        close_redis_cur()
    
    @app.teardown_appcontext
    def teardown_appcontext(exception):
        pass