'''
Flask Application Error Handler
'''
from flask import Blueprint, jsonify, request

error_handler = Blueprint('error_handler', __name__)


@error_handler.app_errorhandler(400)
def bad_requests(error):
    '''400 error handler'''
    if request.accept_mimetypes.accept_json:
        return jsonify(msg=str(error)), 400
    return "400 page", 400


@error_handler.app_errorhandler(404)
def not_found(error):
    '''404 error handler'''
    if request.accept_mimetypes.accept_json:
        return jsonify(msg=str(error)), 404
    return "404 Page", 404


@error_handler.app_errorhandler(500)
def internal_server_error(error):
    '''404 error handler'''
    if request.accept_mimetypes.accept_json:
        return jsonify(msg=str(error)), 404
    return "404 Page", 404
