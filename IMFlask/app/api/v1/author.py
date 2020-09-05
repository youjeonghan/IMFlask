from flask import g, request
from app.api.v1 import api_v1 as api
from app.api.decorators import timer
from app.controllers.author_con import get_author_with_mongo
from app.controllers.author_con import get_author_with_mysql
from app.controllers.author_con import insert_author_with_mysql
from app.controllers.author_con import get_author_with_redis


@api.route('/author/mysql', methods=['GET', 'PUT'])
@timer
def apiv1_get_author_with_mysql():
    # GET
    if request.method == "GET":
        return {
            "msg": "success",
            "result": get_author_with_mysql(g.mysql_cur)
        }
    
    # PUT
    data = request.get_json()
    insert_author_with_mysql(g.mysql_cur, 
                             data['auhtor'])
    return {}, 204


@api.route('/author/mongodb')
@timer
def apiv1_get_author_with_mongodb():
    return {
        "msg": "success",
        "result": get_author_with_mongo(g.mongo_cur)
    }


@api.route('/author/redis')
@timer
def apiv1_get_author_with_redis():
    return {
        "msg": "success",
        "result": get_author_with_redis(g.redis_cur)
    }