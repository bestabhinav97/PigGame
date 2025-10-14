from .player import Player
from .dice import Dice

class Game():
    
    def __init__(self):
        self.dice = Dice()

    def roll(self): 
        return self.dice.roll()
    
    def cheatRoll(self):
        return self.dice.cheatDiceRoll()
    
    def checkRolls(self, die1, die2):
        if die1 == 1 and die2 == 1:
            return 2
        elif die1 == 1 or die2 == 1:
            return 1
        else:
            return die1 + die2



    
    


    
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
            rollChoice = input("ENTER R TO ROLL or quit to leave the game: ").strip().lower()
            if rollChoice == "r":
                die1 = self.dice.roll()
                die2 = self.dice.roll()
            elif rollChoice == "quit":
                print("QUITING GAME")
                gameOver = True
                break
            else:
                print("INVALID CHOICE! Enter Again")
                continue
            
            
            checkValue = self.checkRolls(die1,die2)
            print(f"You rolled a {die1} and a {die2}\n")
            if checkValue == 1:
                print("😬 OOPS  YOU ROLLED ONE ONE, YOU LOOSE THE ROUND SCORE")
                print(f"{players[currentPlayer].name}'s current total score is {players[currentPlayer].totalScore} \n")
                players[currentPlayer].runningScore = 0
                currentPlayer = 1-currentPlayer
            elif checkValue == 2:
                print("🐍 SNAKE EYE - YOU LOOSE ALL THE POINTS \n")
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
                            print("😬 OOPS, YOU LOOSE THE ROUND SCORE")
                            print(f"{players[currentPlayer].name}'s TOTAL SCORE IS {players[currentPlayer].totalScore}\n")
                            print
                            players[currentPlayer].runningScore = 0
                            currentPlayer = 1-currentPlayer
                            repeateTurn = False
                        
                        elif checkValueRepeat == 2:
                            print(f"You rolled a {die1} and a {die2}")
                            print("🐍 SNAKE EYE - YOU LOOSE ALL THE POINTS \n")
                            players[currentPlayer].runningScore = 0
                            players[currentPlayer].totalScore = 0
                            currentPlayer = 1-currentPlayer
                            repeateTurn = False
                        
                        else:
                            print(f"You rolled a {die1} and a {die2}")
                            players[currentPlayer].runningScore = players[currentPlayer].runningScore + checkValueRepeat
                            players[currentPlayer].totalScore = players[currentPlayer].runningScore
                            print(f"{players[currentPlayer].name}'s current running score is {players[currentPlayer].runningScore} ")
                            if players[currentPlayer].totalScore >= 20:
                                print(f"🎉 🎉 🎉 CONGRATULATION {players[currentPlayer].name} IS THE WINNER!!!! 🎉 🎉 🎉")
                                gameOver = True
                                break
                            #players[currentPlayer].runningScore = 0
                            nextChoice = input("1.HOLD or 2.REPEAT")
                            if nextChoice == "1":
                                players[currentPlayer].totalScore += players[currentPlayer].runningScore
                                players[currentPlayer].runningScore = 0
                                print(f"{players[currentPlayer].name}'s TOTAL SCORE IS {players[currentPlayer].totalScore}\n")
                                if players[currentPlayer].totalScore >= 20:
                                    print(f"🎉 🎉 🎉 CONGRATULATION {players[currentPlayer].name} IS THE WINNER!!!! 🎉 🎉 🎉")
                                    gameOver = True
                                    break
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

            


    def cheatGame(self):
        print("ENTER THE GAME IN CHEAT MODE....")
        print("YOU ALWAYS ROLL 6 and 6 to reach the end of the game faster.")

        playerName = input("Enter you player name: ")
        player = Player(playerName)
        computerScore = 0

        gameOver = False

        while gameOver:
            roll = input("Press R to Roll: ")
            if roll == "r" or "R":
                die1 = self.cheatRoll()
                die2 = self.cheatRoll()

            





                        







            

