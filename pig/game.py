from .player import Player
from .dice import Dice

class Game():
    
    def __init__(self):
        dice = Dice()

        

    
    
    def playGame(self):
        print("PLAY AGAINST FRIEND OR COMPUTER")
        print("1 - Friend")
        print("2 - Computer")

        gameChoice = input("Enter your choice")
        currentPlayer = 0

        if gameChoice == 1:
            print("Enter player 1 name")
            p1Name = input()
            player1 = Player(p1Name)
            print("Enter player 2 name")
            p2Name = input()
            player2 = Player(p2Name)

            

            print(f"Player {currentPlayer+1}'s turn")
            die1 = Dice.roll()
            die2 = Dice.roll()

            if die1 != 1 and die2!=1:
                player1.runningScore = die1 + die2
                print("HOLD or ")            



            

