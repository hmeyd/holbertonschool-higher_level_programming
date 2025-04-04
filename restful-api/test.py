#!/usr/bin/python3
"""
Set up a simple HTTP server to serve JSON data and
handle different endpoints
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/bonjour/<string:titre>/<string:name>')
def bonjour(titre: str, name: str):
    return render_template("bonjour.html", titre=titre, name=name)

if __name__ == "__main__":
    app.run(debug=True)
