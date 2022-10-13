import random
print("Play until you win!") 
print("Rock, Paper, or Scissors?")
class GameEngine:
    def __init__(self, computer):
        self.computer = computer
starter = GameEngine(random.choice([-4,-2,-1]))
class Player:
    def __init__ (self, options):
        self.options = options
play = Player({"rock":4,"paper":2,"scissors":1})
class ScoreBoard:
    def __init__(self, score, loss):
        self.score = score
        self.loss = loss
while True:
    match = ScoreBoard(play.options[input("Choose: ")]+starter.computer,[0,-1,-2,3])
    if match.score in match.loss:
        starter.computer = 0
    else:
        print("You win!")
        break
