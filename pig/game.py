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

    def displayCheat(self):
        print(""" 
        🎲 CHEAT MENU 🎲
        1. Roll 6 and 6
        2. Manually set your total score
        3. Roll Normally
        """)

    def playGame(self, mode="normal"):
        cheatMode = (mode == "cheat")

        print("PLAY AGAINST FRIEND OR COMPUTER")
        print("1 - Friend")
        print("2 - Computer")
        gameChoice = input("Enter your choice: ").strip()
        
        ai = None
        if gameChoice == "1":
            p1Name = input("Enter player 1 name: ").strip() or "Player 1"
            player1 = Player(p1Name)
            p2Name = input("Enter player 2 name: ").strip() or "Player 2"
            player2 = Player(p2Name)
        elif gameChoice == "2":
            p1Name = input("Enter your name: ").strip() or "Player 1"
            player1 = Player(p1Name)
            diff = input("Choose AI difficulty (easy/medium/hard): ").strip().lower()
            if diff not in ("easy", "medium", "hard"):
                diff = "medium"
            ai = Intelligence(diff, target_score=self.target)
            player2 = Player(f"Computer({diff})")
        else:
            print("Invalid choice, defaulting to Friend mode.")
            p1Name = input("Enter player 1 name: ").strip() or "Player 1"
            player1 = Player(p1Name)
            p2Name = input("Enter player 2 name: ").strip() or "Player 2"
            player2 = Player(p2Name)

        players = [player1, player2]
        currentPlayer = 0
        gameOver = False

        while not gameOver:
            print(f"\n🎯 {players[currentPlayer].name}'s TURN 🎯")
            is_computer_turn = ai is not None and currentPlayer == 1

            # ==== CHEAT OPTIONS (only for Player 1 and cheat mode) ====
            if cheatMode and currentPlayer == 0:
                self.displayCheat()
                cheatInput = input("Enter choice: ").strip()
                if cheatInput == "1":
                    die1, die2 = 6, 6
                elif cheatInput == "2":
                    playerScore = int(input("Enter your total score manually: "))
                    players[currentPlayer].totalScore = playerScore
                    if players[currentPlayer].totalScore >= self.target:
                        print(f"🏆 {players[currentPlayer].name} WINS (Cheated 😏) 🏆")
                        break
                    currentPlayer = 1 - currentPlayer
                    continue
                else:
                    die1 = self.dice.roll()
                    die2 = self.dice.roll()
            elif is_computer_turn:
                print("Computer chooses: ROLL")
                die1 = self.dice.roll()
                die2 = self.dice.roll()
            else:
                input("Press ENTER to roll: ")
                die1 = self.dice.roll()
                die2 = self.dice.roll()

            print(f"You rolled a {die1} and a {die2}\n")
            checkValue = self.checkRolls(die1, die2)

            # === Handle roll results ===
            if checkValue == 1:
                print("❌ Rolled a ONE! Lose running score.")
                players[currentPlayer].runningScore = 0
                currentPlayer = 1 - currentPlayer
                continue
            elif checkValue == 2:
                print("🐍 Snake Eyes! Lose ALL points!")
                players[currentPlayer].runningScore = 0
                players[currentPlayer].totalScore = 0
                currentPlayer = 1 - currentPlayer
                continue
            else:
                players[currentPlayer].runningScore += checkValue
                print(f"{players[currentPlayer].name}'s running score: {players[currentPlayer].runningScore}")

            # === HOLD or ROLL AGAIN ===
            while True:
                if is_computer_turn:
                    decision = ai.decide(players[currentPlayer].runningScore, players[currentPlayer].totalScore)
                    repeatChoice = "1" if decision == "h" else "2"
                    print(f"Computer chooses: {'HOLD' if repeatChoice == '1' else 'ROLL AGAIN'}")
                else:
                    repeatChoice = input("1. HOLD or 2. ROLL AGAIN: ").strip()

                if repeatChoice == "1":
                    players[currentPlayer].totalScore += players[currentPlayer].runningScore
                    print(f"{players[currentPlayer].name}'s total score: {players[currentPlayer].totalScore}\n")
                    players[currentPlayer].runningScore = 0
                    break
                elif repeatChoice == "2":
                    # Allow cheat in repeat rolls too
                    if cheatMode and currentPlayer == 0:
                        self.displayCheat()
                        cheatInput = input("Enter choice: ").strip()
                        if cheatInput == "1":
                            die1, die2 = 6, 6
                        elif cheatInput == "2":
                            playerScore = int(input("Enter your total score manually: "))
                            players[currentPlayer].totalScore = playerScore
                            if players[currentPlayer].totalScore >= self.target:
                                print(f"🏆 {players[currentPlayer].name} WINS  🏆")
                                gameOver = True
                                break
                            currentPlayer = 1 - currentPlayer
                            continue
                        else:
                            die1 = self.dice.roll()
                            die2 = self.dice.roll()
                    else:
                        die1 = self.dice.roll()
                        die2 = self.dice.roll()

                    print(f"You rolled a {die1} and a {die2}")
                    checkValue = self.checkRolls(die1, die2)
                    if checkValue == 1:
                        print("❌ Rolled a ONE! Lose running score.")
                        players[currentPlayer].runningScore = 0
                        break
                    elif checkValue == 2:
                        print("🐍 Snake Eyes! Lose ALL points!")
                        players[currentPlayer].runningScore = 0
                        players[currentPlayer].totalScore = 0
                        break
                    else:
                        players[currentPlayer].runningScore += checkValue
                        print(f"{players[currentPlayer].name}'s running score: {players[currentPlayer].runningScore}")
                else:
                    print("Invalid choice, turn ends.")
                    players[currentPlayer].runningScore = 0
                    break

            # === Win Check ===
            if players[currentPlayer].totalScore >= self.target:
                print(f"🏆 CONGRATULATIONS {players[currentPlayer].name} IS THE WINNER! 🏆")
                break

            currentPlayer = 1 - currentPlayer
