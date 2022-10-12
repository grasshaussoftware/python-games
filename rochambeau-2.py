import random

class Game:
    def __init__(self, player1, opponent, choices):
        self.player1 = player1
        self.opponent = opponent
        self.choice = choices

set = Game(input("Choose: "),random.choice([-4,-2,-1]),{"rock":4,"paper":2,"scissors":1})

class Core:
    def __init__(self, outcome):
        self.outcome = outcome

match = Core(set.choice[set.player1]+set.opponent)

set.player1
set.opponent

if match.outcome == 0:
    print("Tie")
elif match.outcome == 1 or 2 or -3:
    print("Computer Wins")
elif match.outcome == 3 or -1 or -2:
    print("You Win!")
