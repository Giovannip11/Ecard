from flask import Blueprint, jsonify, render_template, request

from app.game import Game, player

routes = Blueprint("routes", __name__)


p1 = player("Kaiji")
bot = player("Tonegawa")


game = Game(p1, bot)
game.side()


@routes.route("/")
def index():
    return render_template("index.html")


@routes.route("/game")
def game_page():
    player = request.args.get("player")
    return render_template("game.html", player=player)


@routes.route("/rules")
def rules():
    return render_template("rules.html")


@routes.route("/play", methods=["POST"])
def play():
    data = request.json
    card_name = data["card"]

    mapping = {"Emperor": game.EMPEROR, "Slave": game.SLAVE, "Citizen": game.CITIZEN}

    player_card = mapping[card_name]

    result = game.play_turn(player_card)

    return jsonify(result)
