#!/usr/bin/python3
" un fichier test pour une application flask"
from flask import Flask, jsonify, request

users = {}
app = Flask(__name__)
@app.route('/')
def home():
    return "welcome in my page"


@app.route("/data")
def data():
    return jsonify(list(users.keys()))



@app.route("/statue")
def statue():
    return "ok"


@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return "cet utilisateur n'exist pas"
    
@app.route("/add_user", methods=["POST"])
def add_user():
    user_data = request.get_json()
    if not user_data or "username" not in user_data:
        return jsonify({"request: is not found"}), 400
    username = user_data["username"]
    users[username] = user_data
    return jsonify({"Message": "user added", "user": user_data}), 201



if __name__ == "__main__":
    app.run(debug=True)