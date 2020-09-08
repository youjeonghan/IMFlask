'''
Create Application Object Code
'''
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import config
from app import api

from app.api.auth import auth as auth_bp
from app.api.v1 import api_v1 as api_v1_bp
from app.api.template import template as template_bp
from app.api.error_handler import error_handler as error_bp


jwtmanager = JWTManager()
cors = CORS()


def create_app(config_name):
    '''Application Object 생성 함수'''
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)
    jwtmanager.init_app(app)
    cors.init_app(app)
    api.init_app(app)

    app.register_blueprint(template_bp)
    app.register_blueprint(error_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(api_v1_bp, url_prefix='/api/v1')

    return app
