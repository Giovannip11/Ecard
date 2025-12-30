import app 
import random

def choose_oponent_card():
    if app.game is not None:
        if app.game.player_side == "Empereor":
            random.choice(["Slave", "Citizen"])
        elif app.game.player_side == "Slave":
            random.choice(["Empereor", "Citizen"])