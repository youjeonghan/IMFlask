'''
V1 author API
'''
from flask import g, request
from app.api import input_check
from app.api.v1 import api_v1 as api
from app.api.decorators import timer
from app.controllers.author_con import get_author
from app.controllers.author_con import insert_author


@api.route('/author', methods=['GET', 'POST'])
@timer
def apiv1_get_author():
    '''Get/Put Author in Mysql'''
    data = request.get_json()

    # GET
    if request.method == "GET":
        return {
            "msg": "success",
            "result": get_author(g.mysql_cur)
        }

    # POST
    input_check(data, 'author', str)
    insert_author(g.mysql_cur, data['author'])
    return {}, 204
