
from .player import Player
from .dice import Dice
from .intelligence import Intelligence


class Game:
    def __init__(self):
        self.dice = Dice()
        self.target = 100  # Winning score

    def roll(self):
        return self.dice.roll()

    def checkRolls(self, die1, die2):
        # Snake eyes check first
        if die1 == 1 and die2 == 1:
            return 2
        if die1 == 1 or die2 == 1:
            return 1
        return die1 + die2

    def playGame(self):
        print("PLAY AGAINST FRIEND OR COMPUTER")
        print("1 - Friend")
        print("2 - Computer")

        gameChoice = input("Enter your choice: \n").strip()

        ai = None
        if gameChoice == "1":
            p1Name = input("Enter player 1 name: \n").strip() or "Player 1"
            player1 = Player(p1Name)
            p2Name = input("Enter player 2 name: \n").strip() or "Player 2"
            player2 = Player(p2Name)
        elif gameChoice == "2":
            p1Name = input("Enter your name: \n").strip() or "Player 1"
            player1 = Player(p1Name)
            diff = input("Choose AI difficulty (easy/medium/hard): \n").strip().lower()
            if diff not in ("easy", "medium", "hard"):
                diff = "medium"
            ai = Intelligence(diff, target_score=self.target)
            player2 = Player(f"Computer({diff})")
        else:
            print("Invalid choice, defaulting to Friend mode")
            p1Name = input("Enter player 1 name: \n").strip() or "Player 1"
            player1 = Player(p1Name)
            p2Name = input("Enter player 2 name: \n").strip() or "Player 2"
            player2 = Player(p2Name)

        players = [player1, player2]
        currentPlayer = 0
        gameOver = False

        while not gameOver:
            print(f"\n{players[currentPlayer].name}'s TURN")

            # --- 🔹 Step 3: Allow name change at any time ---
            name_choice = input("Press ENTER to continue or type 'name' to change your name: ").strip().lower()
            if name_choice == "name":
                new_name = input("Enter your new name: ").strip()
                players[currentPlayer].change_name(new_name)
                print(f"Your name is now {players[currentPlayer].name}.\n")

            is_computer_turn = ai is not None and currentPlayer == 1
            if is_computer_turn:
                rollChoice = "r"
                print("Computer chooses: ROLL")
            else:
                rollChoice = input("ENTER R TO ROLL: ").strip().lower()

            if rollChoice in ("r", "R"):
                die1 = self.dice.roll()
                die2 = self.dice.roll()
            else:
                print("INVALID CHOICE")
                continue

            checkValue = self.checkRolls(die1, die2)
            print(f"You rolled a {die1} and a {die2}\n")

            if checkValue == 1:
                print("OOPS! YOU ROLLED A ONE — YOU LOSE THIS ROUND SCORE.")
                players[currentPlayer].runningScore = 0
                currentPlayer = 1 - currentPlayer

            elif checkValue == 2:
                print("SNAKE EYES! YOU LOSE ALL YOUR POINTS.")
                players[currentPlayer].runningScore = 0
                players[currentPlayer].totalScore = 0
                currentPlayer = 1 - currentPlayer

            else:
                players[currentPlayer].runningScore = checkValue
                if is_computer_turn:
                    decision = ai.decide(players[currentPlayer].runningScore,
                                         players[currentPlayer].totalScore)
                    repeatChoice = "1" if decision == "h" else "2"
                    print(f"Computer chooses: {'HOLD' if repeatChoice == '1' else 'ROLL AGAIN'}")
                else:
                    repeatChoice = input("1.HOLD OR 2.AGAIN: ").strip()

                if repeatChoice == "2":
                    repeatTurn = True
                    while repeatTurn:
                        die1 = self.dice.roll()
                        die2 = self.dice.roll()
                        checkValueRepeat = self.checkRolls(die1, die2)

                        if checkValueRepeat == 1:
                            print(f"You rolled a {die1} and a {die2}")
                            print("OOPS! YOU LOSE THE ROUND SCORE.")
                            players[currentPlayer].runningScore = 0
                            currentPlayer = 1 - currentPlayer
                            repeatTurn = False
                        elif checkValueRepeat == 2:
                            print(f"You rolled a {die1} and a {die2}")
                            print("SNAKE EYES! YOU LOSE ALL POINTS.")
                            players[currentPlayer].runningScore = 0
                            players[currentPlayer].totalScore = 0
                            currentPlayer = 1 - currentPlayer
                            repeatTurn = False
                        else:
                            print(f"You rolled a {die1} and a {die2}")
                            players[currentPlayer].runningScore += checkValueRepeat
                            players[currentPlayer].totalScore = players[currentPlayer].runningScore
                            print(f"{players[currentPlayer].name}'s running score is {players[currentPlayer].runningScore}")

                            if is_computer_turn:
                                decision2 = ai.decide(players[currentPlayer].runningScore,
                                                      players[currentPlayer].totalScore)
                                nextChoice = "1" if decision2 == "h" else "2"
                                print(f"Computer chooses: {'HOLD' if nextChoice == '1' else 'ROLL AGAIN'}")
                            else:
                                nextChoice = input("1.HOLD or 2.REPEAT: ").strip()

                            if nextChoice == "1":
                                players[currentPlayer].totalScore += players[currentPlayer].runningScore
                                players[currentPlayer].runningScore = 0
                                print(f"{players[currentPlayer].name}'s TOTAL SCORE IS {players[currentPlayer].totalScore}\n")
                                repeatTurn = False
                            elif nextChoice == "2":
                                repeatTurn = True
                            else:
                                repeatTurn = False
                elif repeatChoice == "1":
                    players[currentPlayer].totalScore += players[currentPlayer].runningScore
                    print(f"{players[currentPlayer].name}'s total score is {players[currentPlayer].totalScore}")
                    players[currentPlayer].runningScore = 0
                    currentPlayer = 1 - currentPlayer

            # check for winner
            if players[0].totalScore >= self.target:
                print(f"🏆 CONGRATULATIONS {players[0].name} IS THE WINNER! 🏆")
                gameOver = True
            elif players[1].totalScore >= self.target:
                print(f"🏆 CONGRATULATIONS {players[1].name} IS THE WINNER! 🏆")
                gameOver = True
