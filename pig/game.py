from .player import Player
from .dice import Dice

class Game():
    
    def __init__(self):
        self.dice = Dice()

    def roll(self): 
        return self.dice.roll()

    def checkRolls(self,die1,die2):
        if die1!=1 and die2 != 1:
            score = die1 + die2
            return score
        elif die1 == 1 or die2 == 1:
            return 1
        elif die1 == 1 and die2 == 1:
            return 2
    
    


    
    def playGame(self):
        print("PLAY AGAINST FRIEND OR COMPUTER")
        print("1 - Friend")
        print("2 - Computer")

        gameChoice = input("Enter your choice: \n")
        

        if gameChoice == "1":
            
            p1Name = input("Enter player 1 name: \n")
            player1 = Player(p1Name)
            
            p2Name = input("Enter player 2 name: \n")
            player2 = Player(p2Name)

        players = [player1,player2]
        currentPlayer = 0
            
        gameOver = False
        while gameOver == False:
            
            print(f"{players[currentPlayer].name}'s TURN \n")

            rollChoice = input("ENTER R TO ROLL: ")
            if rollChoice == "R" or "r":
                die1 = self.dice.roll()
                die2 = self.dice.roll()
            else:
                print("INVALID CHOICE")
            
            
            checkValue = self.checkRolls(die1,die2)
            print(f"You rolled a {die1} and a {die2}\n")
            if checkValue == 1:
                print("OOPS  YOU ROLLED ONE ONE, YOU LOOSE THE ROUND SCORE")
                print(f"{players[currentPlayer].name}'s current total score is {players[currentPlayer].totalScore} \n")
                players[currentPlayer].runningScore = 0
                currentPlayer = 1-currentPlayer
            elif checkValue == 2:
                print("SNAKE EYE!!!!   YOU LOOSE ALL THE POINTS")
                print(f"{players[currentPlayer].name}'s current total score is {players[currentPlayer].totalScore} \n")
                players[currentPlayer].runningScore = 0
                players[currentPlayer].totalScore = 0
                currentPlayer = 1-currentPlayer
            else:
                players[currentPlayer].runningScore = checkValue
                repeatChoice = input("1.HOLD OR 2.AGAIN: ")
                
                
                if repeatChoice == "2":
                    
                    repeateTurn = True
                    while repeateTurn:
                        die1 = self.roll()
                        die2 = self.roll()
                        checkValueRepeat = self.checkRolls(die1,die2)
                        
                        if checkValueRepeat == 1:
                            print(f"You rolled a {die1} and a {die2}")
                            print("OOPS, YOU LOOSE THE ROUND SCORE")
                            print(f"{players[currentPlayer].name}'s TOTAL SCORE IS {players[currentPlayer].totalScore}\n")
                            print
                            players[currentPlayer].runningScore = 0
                            currentPlayer = 1-currentPlayer
                            repeateTurn = False
                        
                        elif checkValueRepeat == 2:
                            print(f"You rolled a {die1} and a {die2}")
                            print("YOU LOOSE ALL THE POINTS \n")
                            players[currentPlayer].runningScore = 0
                            players[currentPlayer].totalScore = 0
                            currentPlayer = 1-currentPlayer
                            repeateTurn = False
                        
                        else:
                            print(f"You rolled a {die1} and a {die2}")
                            players[currentPlayer].runningScore = players[currentPlayer].runningScore + checkValueRepeat
                            players[currentPlayer].totalScore = players[currentPlayer].runningScore
                            print(f"{players[currentPlayer].name}'s current running score is {players[currentPlayer].runningScore} ")
                            #players[currentPlayer].runningScore = 0
                            nextChoice = input("1.HOLD or 2.REPEAT")
                            if nextChoice == "1":
                                players[currentPlayer].totalScore += players[currentPlayer].runningScore
                                players[currentPlayer].runningScore = 0
                                print(f"{players[currentPlayer].name}'s TOTAL SCORE IS {players[currentPlayer].totalScore}\n")
                                repeateTurn = False  # end turn
                            elif nextChoice == "2":
                                repeateTurn = True  # keep rolling
                            else:
                                repeateTurn = False
                            
                
                
                elif repeatChoice == "1":
                    #players[currentPlayer].runningScore = players[currentPlayer].runningScore + checkValue
                    players[currentPlayer].totalScore += players[currentPlayer].runningScore
                    print(f"{players[currentPlayer].name}'s current total score is {players[currentPlayer].totalScore} ")
                    players[currentPlayer].runningScore = 0
                    currentPlayer = 1-currentPlayer

            if players[currentPlayer].totalScore > 20:
                print(f"CONGRATULATION {players[currentPlayer].name} IS THE WINNER!!!!")
                gameOver = True           

                        







            

