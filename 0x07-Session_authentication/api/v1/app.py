#!/usr/bin/env python3
"""
Route module for the API
"""

from os import getenv

from api.v1.auth.session_db_auth import SessionDBAuth
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None
auth = getenv('AUTH_TYPE')


if auth == 'auth':
    from api.v1.auth.auth import Auth
    auth = Auth()
if auth == 'session_auth':
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()
if auth == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
if auth == 'session_exp_auth':
    from api.v1.auth.session_exp_auth import SessionExpAuth
    auth = SessionExpAuth()
if auth == 'session_db_auth':
    auth = SessionDBAuth


@app.errorhandler(404)
def not_found(error) -> str:
    """
    Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def not_authorized(error):
    '''handle authorized error'''
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden_status(error):
    '''forbidden'''
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request():
    '''dothis before every request'''
    if auth is None:
        return
    if not auth.require_auth(request.path, ['/api/v1/status/',
                                            '/api/v1/unauthorized/',
                                            '/api/v1/forbidden/',
                                            '/api/v1/auth_session/login/']):
        return
    if auth.authorization_header(request) is None \
            and auth.session_cookie(request) is None:
        abort(401)
    current_user = auth.current_user(request)
    if current_user is None:
        abort(403)
    request.current_user = current_user


if __name__ == "__main__":
    '''main block'''
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port, debug=True)
