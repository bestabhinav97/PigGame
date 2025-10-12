from .player import Player
from .dice import Dice

class Game():
    
    def __init__(self):
        dice = Dice()

        

    def checkRolls(self,die1,die2):
        if die1 and die2 != 1:
            score = die1 + die2
            return score
        elif die1 == 1 or die2 == 1:
            return 1
        elif die1 == 1 and die1 == 1:
            return 2
    
    

    
    def playGame(self):
        print("PLAY AGAINST FRIEND OR COMPUTER")
        print("1 - Friend")
        print("2 - Computer")

        gameChoice = input("Enter your choice")
        currentPlayer = 0
        dice = Dice()

        if gameChoice == 1:
            print("Enter player 1 name")
            p1Name = input()
            player1 = Player(p1Name)
            print("Enter player 2 name")
            p2Name = input()
            player2 = Player(p2Name)

            
        gameOver = False
        while gameOver == False:
            players = [player1,player2]
            currentPlayer = 0
            print(f"{Player[currentPlayer]}'s TURN")
            die1 = dice.roll()
            die2 = dice.roll()
            
            checkValue = self.checkRolls(die1,die2)
            if checkValue == 1:
                players[currentPlayer].runningScore = 0
                currentPlayer = 1-currentPlayer
            elif checkValue == 2:
                players[currentPlayer].runningScore = 0
                players[currentPlayer].totalScore = 0
                currentPlayer = 1-currentPlayer
            else:
                players[currentPlayer].runningScore = checkValue
                repeatChoice = input("HOLD OR AGAIN")





            

