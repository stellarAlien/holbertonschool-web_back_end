#!/usr/bin/env python3

import email
from flask import Flask, jsonify, request
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

    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)