'''
Flask Application Error Handler
'''
import sys
from flask import Blueprint, jsonify, request

erros = Blueprint('error_handler', __name__)


@erros.app_errorhandler(400)
def bad_requests(error):
    if request.accept_mime_types.accept_json and \
        not request.accept_mime_types.accept_html:
        return jsonify(result=str(error)), 400
    return "400 Page", 400


@erros.app_errorhandler(404)
def not_found(error):
    if request.accept_mime_types.accept_json and \
        not request.accept_mime_types.accept_html:
        return jsonify(result=str(error)), 404
    return "404 Page", 404


@erros.app_errorhandler(500)
def internal_server_error(error):
    sys.stdout.write(error + "\n")
    return "fail", 500
