from flask import Blueprint, Flask, jsonify, render_template, request
from flask.globals import request

from app.game import CITIZEN, EMPEREOR, SLAVE, Game


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


@routes.route("/play", methods=["POST"])
def play():
    data = request.json
    card_name = data["card"]

    mapping = {"Emperor": EMPEREOR, "Slave": SLAVE, "Citizen": CITIZEN}

    player_card = mapping[card_name]
    bot_card = game.bot_choose()

    result = game.compare(player_card, bot_card)

    return jsonify(
        {"player_card": player_card.name, "bot_card": bot_card.name, "result": result}
    )
