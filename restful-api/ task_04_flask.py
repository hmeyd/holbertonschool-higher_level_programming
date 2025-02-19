#!usr/bin/python3
""" Develop a Simple API using Python with Flask"""
from flask import Flask, jsonify, request

app = Flask(__name__)
users = {"jane": {"name": "Jane", "age": 28,
                  "city": "Los Angeles"}}

@app.route("/", methods=["GET"])
def home():
    return  "Welcome to the Flask API!"
@app.route("/data", methods=["GET"])
def get_data():
    return jsonify(list(users.keys))
@app.route("/status", methods=["GET"])
def status():
    return "ok", 200
@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    user = user.get(username)
    if user:
        return jsonify(user)
    else:
        return "User not found", 404
@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    username  = data.get("username")
    if username in users:
        return "User {} already exists".format(username), 400
    users[username] = {
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }
    return jsonify(users[username]), 201
if __name__== "__main__":
    app.run(debug=True)