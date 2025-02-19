#!/usr/bin/python3
"""
Un script Python basique pour récupérer des posts de
JSONPlaceholder en utilisant requests
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from functools import wraps

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)


users = {
    "user1": {"username": "user1", "password":
              generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password":
               generate_password_hash("password"), "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    """ Vérifie si l'utilisateur existe et si son mot de
    passe est correct """
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """ Route protégée par Basic Auth """
    return jsonify({"message": "Basic Auth: Access Granted"}), 200


@app.route('/login', methods=['POST'])
def login():
    """ Authentifie un utilisateur et lui renvoie un token JWT """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        token = create_access_token(identity={"username": username,
                                              "role": user["role"]})
        return jsonify({"access_token": token}), 200

    return jsonify({"error": "Invalid credentials"}), 401


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """ Route protégée avec JWT """
    current_user = get_jwt_identity()
    return jsonify({"message": "JWT Auth: Access Granted",
                    "user": current_user["username"]}), 200


def admin_required(fn):
    """ Décorateur pour restreindre l'accès aux
    administrateurs uniquement """

    @wraps(fn)
    def wrapper(*args, **kwargs):
        current_user = get_jwt_identity()
        if current_user["role"] != "admin":
            return jsonify({"error": "Admin access required"}), 403
        return fn(*args, **kwargs)
    return wrapper


@app.route('/admin-only', methods=['GET'])
@jwt_required()
@admin_required
def admin_only():
    """ Route accessible uniquement aux administrateurs """
    return jsonify({"message": "Admin Access: Granted"}), 200


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """ Erreur JWT : Aucun token fourni """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """ Erreur JWT : Token invalide """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """ Erreur JWT : Token expiré """
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """ Erreur JWT : Token révoqué """
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """ Erreur JWT : Token non frais requis """
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run(debug=True)
