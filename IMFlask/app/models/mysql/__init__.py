'''
MySQL Management Modules and Models
'''
import pymysql
from sqlalchemy.engine.url import make_url
from flask import g, current_app
from app.models.mysql.tables import tables

def get_mysql_cur(store_g=True):
    '''
    Open DB Cursor Connection

    Params
    -------
    store_g : if True, store to Flask Global Object g.
    '''
    uri = current_app.config['MYSQL_URI']
    uri = make_url(uri)
    mysql_cur = pymysql.connect(
            host=uri.host,
            port=uri.port,
            user=uri.username,
            passwd=uri.password,
            db=uri.database,
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor)

    if store_g:
        g.mysql_cur = mysql_cur

    return mysql_cur


def close_mysql_cur():
    '''
    Close DB Cursor Connection
    '''
    mysql_cur = g.pop('mysql_cur', None)
    if mysql_cur:
        mysql_cur.close()


def mysql_init():
    conn = get_mysql_cur(store_g=False)
    with conn.cursor() as cur:
        for sql in tables:
            cur.execute(sql)
        sql = '''
            INSERT INTO imltable(author) VALUES ('IML');
        '''
        cur.execute(sql)
    conn.commit()
    conn.close()