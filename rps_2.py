import random 
class GameEngine:
    def __init__(self, computer):
        self.computer = computer
starter = GameEngine(random.choice([-4,-2,-1]))
class Player:
    def __init__ (self, options):
        self.options = options
play = Player({"rock":4,"paper":2,"scissors":1})
class ScoreBoard:
    def __init__(self, outcome):
        self.outcome = outcome
match = ScoreBoard(play.options[input("Choose: ")]+starter.computer)
if match.outcome not in [0,1,2,-3]:
    print("You win!")
