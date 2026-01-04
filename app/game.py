import random

import app
import app.oponent as oponent


class player:
    def __init__(self, life):
        self.life = life


Kaiji = player(life=10000)
Tonegawa = player(life=10000)


class game:
    def __init__(self, player, turns, cards, player_side):
        self.player = player
        self.turns = turns
        self.cards = cards
        self.player_side = player_side

    def _shuffle_deck(self):
        if hasattr(game, "deck"):
            random.shuffle(cards)

    def _start(self):
        _choose_side()
        if player_side == Empereor:
            player.play_turn()
        else:
            oponent.play_turn()

        if hasattr(game, "kaiji") and Kaiji.life <= 0:
            return "Tonegawa wins"
        if hasattr(game, "Tonegawa") and Tonegawa.life <= 0:
            return "Kaiji wins"

    def start_game(self):
        if game is not None:
            print("Game Start")


class cards:
    def __init__(self, name, power):
        self.name = name
        self.power = power


class player_side:
    def __init__(self, name, side):
        self.name = name
        self.side = side


Empereor_side = player_side("Empereor", 1)
Slave_side = player_side("Slave", 2)

Empereor = cards("Empereor", 1)
Slave = cards("Slave", -1)
Citizen = cards("Citizen", 0)


def bet(life):
    if game is not None:
        return bet(life)
    try:
        betlife = int(input("Enter the life you want to bet: "))
        return betlife
    except Exception:
        return None


def player_choose_card():
    if game is None:
        return None

    try:
        if hasattr(game, "player_choose_card"):
            player_choose_card()
    except Exception:
        pass

    player_card_name = getattr(game, "player_card", None)
    if player_card_name is None:
        return None

    if player_side == "Empereor":
        match player_card_name:
            case "Empereor":
                return Empereor
            case "Citizen":
                return Citizen
    elif player_side == "Slave":
        match player_card_name:
            case "Slave":
                return Slave
            case "Citizen":
                return Citizen

    return None


def comparison_cards_power(player_card, oponent_card):
    if player_card is None or oponent_card is None:
        return None
    total = player_card.power + oponent_card.power
    if total == 0:
        return Slave
    if total == 1:
        return Empereor
    if total == -1:
        return Citizen
    return None


def choose_winner(player_card, oponent_card):
    if player_card is None or oponent_card is None:
        return None
    if player_card == oponent_card:
        return "Draw"
    winner_card = comparison_cards_power(player_card, oponent_card)
    if winner_card is None:
        return None
    if winner_card == player_card:
        return "Kaiji wins"
    if winner_card == oponent_card:
        return "Tonegawa wins"
    return None


def _choose_side():
    if getattr(game, "player_side", None) == "random":
        player_side = random.choice(["Empereor", "Slave"])
        computer_side = "Empereor" if player_side == "Slave" else "Slave"


def play_turn():
    if app.game is None:
        return None

    try:
        betlife = bet(life)
    except Exception:
        betlife = None

    try:
        if hasattr(game, "play_turn"):
            game.play_turn()
    except Exception:
        pass

    player_card = player_choose_card()
    opponent_card = oponent.choose_oponent_card()
    result = choose_winner(player_card, opponent_card)

    return (player_card, opponent_card, result)


def side_after_turn():
    if player_side == Empereor and game.computer_side == Slave:
        if game.turn_count % 2 == 0 and game.turn_count != 0:
            change(Kaiji, Tonegawa)


def change(player, oponent):
    player.side, oponent.side = oponent.side, player.side


def tonegawa_expressions():
    expressions = [
        "Money is worth more than life.",
        "You have no one to blame but yourself for being losers.What you must to do now is to win! Just win!",
        "One:courage,Two:guts,ThreeDetermination!This is E-Card",
    ]


# after two turns side need to change
"""idk but...fucking magic"""
