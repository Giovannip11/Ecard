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

        self.EMPEROR = self.cards("Empereor", 1)
        self.SLAVE = self.cards("Slave", -1)
        self.CITIZEN = self.cards("Citizen", 0)

    def side(self):
        if random.choice([True, False]):
            self.player1.side = "Empereor"
            self.player2.side = "Slave"
        else:
            self.player1.side = "Slave"
            self.player2.side = "Empereor"

    def deal_cards(self):
        if self.player1.side == "Emperor":
            self.player1.cards = [self.EMPEROR] + [self.CITIZEN] * 4
            self.player2.cards = [self.SLAVE] + [self.CITIZEN] * 4
        else:
            self.player1.cards = [self.SLAVE] + [self.CITIZEN] * 4
            self.player2.cards = [self.EMPEROR] + [self.CITIZEN] * 4

    def compare_cards(self, c1, c2):
        total = c1.power + c2.power

        if total == 0:
            return "Slave"
        if total == 1:
            return "EMPEREOR"
        if total == -1:
            return "CITIZEN"

    def play_turn(self, player_card):
        bot_card = random.choice(self.player2.cards)

        self.player1.cards.remove(player_card)
        self.player2.cards.remove(bot_card)

        winner = self.compare_cards(player_card, bot_card)

        self.round += 1

        if self.round % 2 == 0:
            self.side()

        return {
            "player_card": player_card.name,
            "bot_card": bot_card.name,
            "winner": winner,
            "player_side": self.player1.side,
        }


Player = player("Kaiji")
bot = player("Tonegawa")

game = Game(Player, bot)
game.side()


game.side()


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
