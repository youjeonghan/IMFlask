'''
V1 author API
'''
from flask import g, request
from app.api import input_check
from app.api.v1 import api_v1 as api
from app.api.decorators import timer
from app.controllers.author_con import get_author_with_mongo
from app.controllers.author_con import get_author_with_mysql
from app.controllers.author_con import insert_author_with_mysql
from app.controllers.author_con import get_author_with_redis


@api.route('/author/mysql', methods=['GET', 'POST'])
@timer
def apiv1_get_author_with_mysql():
    '''Get/Put Author in Mysql'''
    data = request.get_json()

    if request.method == "GET":
        return {
            "msg": "success",
            "result": get_author_with_mysql(g.mysql_cur)
        }

    # POST
    input_check(data, 'author', str)
    insert_author_with_mysql(g.mysql_cur,
                             data['author'])
    return {}, 204


@api.route('/author/mongodb')
@timer
def apiv1_get_author_with_mongodb():
    '''Get Author in MongoDB'''
    return {
        "msg": "success",
        "result": get_author_with_mongo(g.mongo_cur)
    }


@api.route('/author/redis')
@timer
def apiv1_get_author_with_redis():
    '''Get Author in Redis'''
    return {
        "msg": "success",
        "result": get_author_with_redis(g.redis_cur)
    }
