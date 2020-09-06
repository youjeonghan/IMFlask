'''
Flask Application Error Handler
'''
import sys
from flask import Blueprint, jsonify, request

errors = Blueprint('error_handler', __name__)


@errors.app_errorhandler(400)
def bad_requests(error):
    if request.accept_mimetypes.accept_json and \
        not request.accept_mimetypes.accept_html:
        return jsonify(result=str(error)), 400
    return "400 Page", 400


@errors.app_errorhandler(404)
def not_found(error):
    if request.accept_mimetypes.accept_json and \
        not request.accept_mimetypes.accept_html:
        return jsonify(result=str(error)), 404
    return "404 Page", 404

