import app
from app.routes import game
import random

def start_game():
    if app.game is not None:
        app.game.start()



def _start():
    game.shuffle_deck()
    game.choose_side()

def _shuffle_deck():
    random.shuffle(game.deck)

def _choose_side():
    if game.player_side =="random":
        game.player_side = random.choice(['X', 'O'])
        game.computer_side = 'O' if game.player_side == 'X' else 'X'
    pass


game.start = _start
game.shuffle_deck = _shuffle_deck
game.choose_side = _choose_side
    