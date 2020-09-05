'''
MongoDB Management Modules and Models
'''
from pymongo import MongoClient
from flask import g, current_app


def get_mongo_cur(store_g=False):
    '''
    Open DB Cursor Connection

    Params
    -------
    store_g : if True, store to Flask Global Object g.
    '''
    mongo_cur = MongoClient(current_app.config['MONGO_URI'])

    if store_g:
        g.mongo_cur = mongo_cur

    return mongo_cur


def close_mongo_cur():
    '''
    Close DB Cursor Connection
    '''
    mongo_cur = g.pop('mongo_cur', None)
    if mongo_cur:
        mongo_cur.close()


def mongo_init():
    cur = get_mongo_cur()
    db_name = current_app.config['MONGO_DB_NAME']
    col = cur[db_name]['master_config']

    col.update(
        {"__author__": "IML"},
        {"$set": {"__author__": "IML"}},
        upsert=True)

    cur.close()
