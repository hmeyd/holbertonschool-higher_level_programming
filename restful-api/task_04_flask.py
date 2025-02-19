#!/usr/bin/python3
"""
Développer une API simple en utilisant Flask
"""
from flask import Flask, jsonify, request


app = Flask(__name__)


users = {
    "jane": {"username": "jane",
             "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john",
             "name": "John", "age": 30, "city": "New York"}
}


@app.route("/", methods=["GET"])
def home():
    """return welcom"""
    return "Welcome to the Flask API!"


@app.route("/data", methods=["GET"])
def get_data():
    """Route pour récupérer les noms d'utilisateurs"""
    return jsonify(list(users.keys()))


@app.route("/status", methods=["GET"])
def status():
    """Route pour vérifier l'état de l'API"""
    return "OK", 200


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Route dynamique pour récupérer les informations
    d'un utilisateur"""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return "User not found", 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Route pour ajouter un utilisateur via POST"""
    data = request.get_json()
    username = data.get("username")
    if username in users:
        return "User {} already exists".format(username), 400
    users[username] = {
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }
    return jsonify(users[username]), 201


if __name__ == "__main__":
    app.run(debug=True)
