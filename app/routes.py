from flask.globals import request
from app import app

from flask import Flask, render_template


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/game")
def game():
    player = request.args.get("player")
    return f"<h1>Welcome, {player}!</h1><p>The game will start soon...</p>"


@app.route("/rules")
def rules():
    return "<h1>Rules</h1><p>Here you’ll explain how the game works.</p>"
