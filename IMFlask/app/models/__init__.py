'''
Flask Application Models
'''
import sys
from app.models.mysql import mysql_init
from app.models.mongodb import mongo_init
from app.models.redis import redis_init


def init_app(app):
    '''
    db-init cli command function
    '''
    mysql_init()
    sys.stdout.write("Mysql init ... OK" + "\n")
    mongo_init()
    sys.stdout.write("MongoDB init ... OK" + "\n")
    redis_init()
    sys.stdout.write("Redis init ... OK" + "\n")
