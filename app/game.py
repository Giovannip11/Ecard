from unicodedata import name
import app
from app.routes import game
import random
import app.oponent as oponent


class cards:
    def __init__(self,name):
        self.name = name

Empereor=cards("Empereor")
Slave=cards("Slave")
Citizen=cards("Citizen")
def start_game():
    if app.game is not None:
        app.game.start()



def _start():
    game.shuffle_deck()
    game.choose_side()

def _shuffle_deck():
    random.shuffle(game.deck)
def player_chosse_card():
    if app.game is not None:
        app.game.player_choose_card()
    if game.player_side=="Empereor":
        match app.game.player_card:
            case "Empereor":
                return Empereor
            case "Citizen":
                return Citizen
    if game.player_side=="Slave":
        match app.game.player_card:
            case "Slave":
                return Slave
            case "Citizen":
                return Citizen

def _choose_side():
    if game.player_side =="random":
        game.player_side = random.choice(['Empereor', 'Slave'])
        game.computer_side = 'Empereor' if game.player_side == 'Slave' else 'Slave'
    pass

def play_turn():
    if app.game is not None:
        app.game.play_turn()
        app.game.player_choose_card()
        return player_chosse_card()
        return oponent.choose_oponent_card()
        


    

game.start = _start
game.shuffle_deck = _shuffle_deck
game.choose_side = _choose_side
    