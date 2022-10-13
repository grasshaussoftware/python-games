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
    def __init__(self, score, win):
        self.score = score
        self.win = win
match = ScoreBoard(play.options[input("Choose: ")]+starter.computer,[1,2,-3])
if match.score in match.win:
    print("You win!")
