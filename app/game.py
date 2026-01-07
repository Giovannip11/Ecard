import random


class player:
    def __init__(self, name, life=10000):
        self.life = life
        self.name = name
        self.cards = []
        self.side = None

    def choose_card(self):
        return random.choice(self.cards)

    def bot_choose_card(self):
        return random.choice(self.cards)


class Game:
    class cards:
        def __init__(self, name, power):
            self.name = name
            self.power = power

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.turns = 0

        self.EMPEREOR = self.cards("Empereor", 1)
        self.SLAVE = self.cards("Slave", -1)
        self.CITIZEN = self.cards("Citizen", 0)

    def side(self):
        sides = ["Empereor", "Slave"]
        random.shuffle(sides)

        self.player1.side = sides[0]
        self.player2.side = sides[1]
        if self.player1.side == "Empereor":
            self.player1.cards = [self.EMPEREOR, self.CITIZEN]
            self.player2.cards = [self.SLAVE, self.CITIZEN]
        else:
            self.player1.cards = [self.SLAVE, self.CITIZEN]
            self.player2.cards = [self.EMPEREOR, self.CITIZEN]

    def compare_cards(self, c1, c2):
        total = c1.power + c2.power

        if total == 0:
            return "Slave"
        if total == 1:
            return "EMPEREOR"
        if total == -1:
            return "CITIZEN"

    def play_turn(self):
        self.turn = +1
        card1 = self.player1.choose_card(self)
        card2 = self.player2.bot_choose_card(self)

        if card1 == card2:
            return print("Empate")

        winner_card = self.compare_cards(card1, card2)

        if winner_card == card1:
            return "Player 1 venceu"
        if winner_card == card2:
            return "PLayer 2 venceu"


Player = player("Kaiji")
bot = player("Tonegawa")

game = Game(player, bot)
game.side()


game.side()
game.play_turn()


def tonegawa_expressions():
    expressions = [
        "Money is worth more than life.",
        "You have no one to blame but yourself for being losers.What you must to do now is to win! Just win!",
        "One:courage,Two:guts,ThreeDetermination!This is E-Card",
    ]
    time = +1
    if time % 5 == 0:
        return print(expressions)


# after two turns side need to change
"""idk but...fucking magic"""
