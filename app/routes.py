from flask.globals import request
from app import app

from flask import Flask, render_template


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/game")
def game():
    player = request.args.get("player")
    return render_template("game.html", player=player)


@app.route("/rules")
def rules():
    return render_template("rules.html")
