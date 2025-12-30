import app
import random
from app.game import Empereor, Slave, Citizen

def choose_oponent_card():
    
    if app.game is None:
        return None

    if app.game.player_side == "Empereor":
        return random.choice([Slave, Citizen])
    elif app.game.player_side == "Slave":
        return random.choice([Empereor, Citizen])

    return random.choice([Empereor, Slave, Citizen])



