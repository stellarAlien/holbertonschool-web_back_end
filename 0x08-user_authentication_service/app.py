#!/usr/bin/env python3

import email
from flask import Flask, jsonify, request, abort
from auth import Auth

app = Flask(__name__)
Auth = Auth()

@app.route("/")
def get():
    return jsonify({"message": "Bienvenue"})

@app.route("/users", methods=['POST'], strict_slashes=False)
def users():
    '''get user credentials'''
    email = request.form['email']
    password = request.form['password']
    try:
        Auth.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

    return jsonify({"email": "<registered email>",
                        "message": "user created"})

@app.route("/sessions", methods=['POST'], strict_slashes=False)
def login():
    '''log in function'''
    email = request.form['email']
    password = request.form['password']
    if Auth.valid_login(email, password):
        sess = Auth.create_session(email)
        resp = jsonify({"email": "<user email>", "message": "logged in"})
        resp.set_cookie('session_id', sess)
        return resp

    abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)