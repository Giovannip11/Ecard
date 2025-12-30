from unicodedata import name
import app
from app.routes import game
import random
import app.oponent as oponent
class player:
    def __init__(self,life):
        self.life = life

Kaiji = player(life=10000)
Tonegawa = player(life=10000)

class cards:
    def __init__(self,name,power):
        self.name = name
        self.power = power

Empereor=cards("Empereor",1)
Slave=cards("Slave",-1)
Citizen=cards("Citizen",0)
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
def comparison_cards_power(player_card,oponent_card):
    if player_card.power + oponent_card.power ==0:
        return Slave
    if player_card.power + oponent_card.power ==1:
        return Empereor
    if player_card.power + oponent_card.power ==-1:
        return Citizen
    
def chose_winner(player_card,oponent_car):
    if player_card == oponent_car:
        return "Draw"   
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
    