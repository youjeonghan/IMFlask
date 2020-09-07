'''
Redis Management Modules and Models
'''
from flask import g, current_app
from redis import Redis


def get_redis_cur(store_g=False):
    '''
    Open DB Cursor Connection

    Params
    -------
    store_g : if True, store to Flask Global Object g.
    '''
    redis_cur = Redis(
        host=current_app.config['REDIS_HOST'],
        port=current_app.config['REDIS_PORT'],
        password=current_app.config['REDIS_PW'])

    if store_g:
        g.redis_cur = redis_cur

    return redis_cur


def close_redis_cur():
    '''
    Close DB Curosr Conneciton
    '''
    redis_cur = g.pop("redis_cur", None)
    if redis_cur:
        redis_cur.close()


def redis_init():
    '''db-init in redis'''
    cur = get_redis_cur()
    cur.set("__author__", "IML")
    cur.close()
