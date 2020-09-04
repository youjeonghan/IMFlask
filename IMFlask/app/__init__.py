from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import config

from IMFlask.app.auth import auth as auth_bp
from IMFlask.app.v1 import api_v1 as api_v1_bp
from IMFlask.app.errors import errors as error_bp

jwtmanager = JWTManager()
cors = CORS()

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])

	jwtmanager.init_app(app)
	cors.init_app(app)

	app.register_blueprint(auth_bp, url_prefix='/auth')
	app.register_blueprint(api_v1_bp, url_prefix='/api/v1')
	app.register_blueprint(error_bp)

	return app
