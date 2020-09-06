'''
Flask Application Config
'''
import os
from logging.config import dictConfig

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY', 'hard to guess string')
    TEST_ACCESS_TOKEN = os.environ.get('FLASK_TEST_ACCESS_TOKEN')

    ADMIN_ID = os.environ.get('FLASK_ADMIN_ID', "iml")
    ADMIN_PW = os.environ.get('FLASK_ADMIN_PW', "iml")

    MYSQL_URI = os.environ.get('FLASK_MYSQL_URI')

    MONGO_URI = os.environ.get('FLASK_MONGO_URI')
    MONGO_DB_NAME = os.environ.get('FLASK_MONGO_DB_NAME')

    REDIS_HOST = os.environ.get('FLASK_REDIS_HOST')
    REDIS_PORT = os.environ.get('FLASK_REDIS_PORT')
    REDIS_PW = os.environ.get('FLASK_REDIS_PW')

    ALLOWED_EXTENSION = {'txt', 'docs', 'md', 'hwp', 'ppt', 'pptx'}
    SLOW_API_TIME = 0.5

    @staticmethod
    def init_app(app):
        pass


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

    @staticmethod
    def init_app(app):
        dictConfig({
            'version': 1,
            'formatters': {
                'default': {
                    'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
                }
            },
            'handlers': {
                'file': {
                    'level': 'INFO',
                    'class': 'logging.handlers.RotatingFileHandler',
                    'filename': './server_error.log',
                    'maxBytes': 1024 * 1024 * 5,
                    'backupCount': 5,
                    'formatter': 'default',
                },
            },
            'root': {
                'level': 'INFO',
                'handlers': ['file']
            }
        })


config = {
    'development':DevelopmentConfig,
    'production':ProductionConfig,
    'testing':TestingConfig,

    'default':DevelopmentConfig,
}
