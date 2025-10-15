
from .player import Player
from .dice import Dice
from .intelligence import Intelligence
from .highscore import HighScore


class Game:
    def __init__(self):
        self.dice = Dice()
        self.target = 100  # Winning score 
        self.highscore = HighScore()  # highscore manager

    def roll(self):
        return self.dice.roll()

    def checkRolls(self, die1, die2):
        """Return the result of dice rolls based on Pig rules."""
        if die1 == 1 and die2 == 1:
            return 2  # Double 1s
        if die1 == 1 or die2 == 1:
            return 1  # One die rolled a 1
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
            print("Invalid choice, defaulting to Friend mode.")
            p1Name = input("Enter player 1 name: \n").strip() or "Player 1"
            player1 = Player(p1Name)
            p2Name = input("Enter player 2 name: \n").strip() or "Player 2"
            player2 = Player(p2Name)

        # Register players in highscore
        player1_id = self.highscore.get_or_create_player(player1.name)
        player2_id = self.highscore.get_or_create_player(player2.name)

        players = [player1, player2]
        player_ids = [player1_id, player2_id]

        currentPlayer = 0
        gameOver = False

        while not gameOver:
            current_player_obj = players[currentPlayer]
            roller_name = current_player_obj.name
            is_computer_turn = ai is not None and currentPlayer == 1
            roller_pronoun = "You" if not is_computer_turn else roller_name

            print(f"\n{roller_name}'s TURN")

            # Allow name change only for human players
            if not is_computer_turn:
                name_choice = input("Press ENTER to continue or type 'name' to change your name: ").strip().lower()
                if name_choice == "name":
                    new_name = input("Enter your new name: ").strip()
                    # Save/merge and update the active ID
                    player_ids[currentPlayer] = self.highscore.rename_player(player_ids[currentPlayer], new_name)
                    current_player_obj.change_name(new_name)
                    print(f"✅ Name changed successfully to {current_player_obj.name}")
                    roller_name = current_player_obj.name
                    roller_pronoun = "You"

            if is_computer_turn:
                rollChoice = "r"
                print(f"{roller_name} chooses: ROLL")
            else:
                rollChoice = input("ENTER R TO ROLL: ").strip().lower()

            if rollChoice not in ("r", "R"):
                print("INVALID CHOICE")
                continue

            die1 = self.dice.roll()
            die2 = self.dice.roll()
            checkValue = self.checkRolls(die1, die2)
            print(f"{roller_name} rolled a {die1} and a {die2}\n")

            if checkValue == 1:
                print(f"OOPS! {roller_pronoun.upper()} ROLLED A ONE — LOSE THIS ROUND SCORE.")
                current_player_obj.runningScore = 0
                currentPlayer = 1 - currentPlayer

            elif checkValue == 2:
                print(f"DOUBLE 1s! {roller_pronoun.upper()} LOSE ALL POINTS.")
                current_player_obj.runningScore = 0
                current_player_obj.totalScore = 0
                currentPlayer = 1 - currentPlayer

            else:
                current_player_obj.runningScore = checkValue
                if is_computer_turn:
                    decision = ai.decide(current_player_obj.runningScore, current_player_obj.totalScore)
                    repeatChoice = "1" if decision == "h" else "2"
                    print(f"{roller_name} chooses: {'HOLD' if repeatChoice == '1' else 'ROLL AGAIN'}")
                else:
                    repeatChoice = input("1.HOLD OR 2.AGAIN: ").strip()

                if repeatChoice == "2":
                    repeatTurn = True
                    while repeatTurn:
                        die1 = self.dice.roll()
                        die2 = self.dice.roll()
                        checkValueRepeat = self.checkRolls(die1, die2)
                        roller_name = players[currentPlayer].name
                        roller_pronoun = "You" if not (ai and currentPlayer == 1) else roller_name

                        print(f"{roller_name} rolled a {die1} and a {die2}\n")

                        if checkValueRepeat == 1:
                            print(f"OOPS! {roller_pronoun.upper()} LOSE THE ROUND SCORE.")
                            players[currentPlayer].runningScore = 0
                            currentPlayer = 1 - currentPlayer
                            repeatTurn = False
                        elif checkValueRepeat == 2:
                            print(f"DOUBLE 1s! {roller_pronoun.upper()} LOSE ALL POINTS.")
                            players[currentPlayer].runningScore = 0
                            players[currentPlayer].totalScore = 0
                            currentPlayer = 1 - currentPlayer
                            repeatTurn = False
                        else:
                            players[currentPlayer].runningScore += checkValueRepeat
                            print(f"{roller_name}'s running score is {players[currentPlayer].runningScore}")

                            if is_computer_turn:
                                decision2 = ai.decide(players[currentPlayer].runningScore,
                                                      players[currentPlayer].totalScore)
                                nextChoice = "1" if decision2 == "h" else "2"
                                print(f"{roller_name} chooses: {'HOLD' if nextChoice == '1' else 'ROLL AGAIN'}")
                            else:
                                nextChoice = input("1.HOLD or 2.REPEAT: ").strip()

                            if nextChoice == "1":
                                # ✅ HOLD inside repeat: add, reset, PRINT, THEN PASS TURN
                                players[currentPlayer].totalScore += players[currentPlayer].runningScore
                                players[currentPlayer].runningScore = 0
                                print(f"{roller_name}'s TOTAL SCORE IS {players[currentPlayer].totalScore}\n")
                                currentPlayer = 1 - currentPlayer   # pass the turn after holding
                                repeatTurn = False
                            elif nextChoice == "2":
                                repeatTurn = True
                            else:
                                repeatTurn = False
                elif repeatChoice == "1":
                    current_player_obj.totalScore += current_player_obj.runningScore
                    print(f"{roller_name}'s TOTAL SCORE IS {current_player_obj.totalScore}")
                    current_player_obj.runningScore = 0
                    currentPlayer = 1 - currentPlayer

            # Check for winner (after every turn/hold/bust)
            if players[0].totalScore >= self.target:
                print(f"🏆 CONGRATULATIONS {players[0].name} IS THE WINNER! 🏆")
                self.highscore.record_game(player_ids[0], players[0].totalScore, won=True)
                self.highscore.record_game(player_ids[1], players[1].totalScore, won=False)
                gameOver = True
            elif players[1].totalScore >= self.target:
                print(f"🏆 CONGRATULATIONS {players[1].name} IS THE WINNER! 🏆")
                self.highscore.record_game(player_ids[1], players[1].totalScore, won=True)
                self.highscore.record_game(player_ids[0], players[0].totalScore, won=False)
                gameOver = True
