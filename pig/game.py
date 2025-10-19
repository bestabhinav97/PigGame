
from .player import Player
from .dice import Dice
from .intelligence import Intelligence
from .highscore import HighScore


class Game:
    def __init__(self):
        self.dice = Dice()
        self.target = 100  # Winning score 
        self.highscore = HighScore()  # Highscore manager

    def roll(self):
        return self.dice.roll()

    def checkRolls(self, die1, die2):
        """Return the result of dice rolls based on Pig rules."""
        if die1 == 1 and die2 == 1:
            return 2  # Double 1s
        if die1 == 1 or die2 == 1:
            return 1  # One die rolled a 1
        return die1 + die2
        
    def displayCheat(self):
        print("""
        🎲 CHEAT MENU 🎲
        1. Roll 6 and 6
        2. Manually set your total score
        3. Roll Normally
        q. Quit
        """)

    def playGame(self, mode="normal"):
        cheatMode = (mode == "cheat")

        print("PLAY AGAINST FRIEND OR COMPUTER\n")
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

            print(f"\n🎯 {roller_name}'s TURN 🎯")

            # Allow name change for human players
            if not is_computer_turn:
                name_choice = input("Press ENTER to continue or type 'name' to change your name: ").strip().lower()
                if name_choice == "name":
                    new_name = input("Enter your new name: ").strip()
                    player_ids[currentPlayer] = self.highscore.rename_player(player_ids[currentPlayer], new_name)
                    current_player_obj.change_name(new_name)
                    print(f"✅ Name changed successfully to {current_player_obj.name}")
                    roller_name = current_player_obj.name
                    roller_pronoun = "You"

            # === Handle Roll Phase ===
            if cheatMode and currentPlayer == 0:
                self.displayCheat()
                cheatInput = input("Enter choice: ").strip()
                if cheatInput == "1":
                    die1, die2 = 6, 6
                elif cheatInput == "2":
                    playerScore = int(input("Enter your total score manually: "))
                    current_player_obj.totalScore = playerScore
                    if playerScore >= self.target:
                        print(f"🏆 {roller_name} WINS (Cheated 😏) 🏆")
                        # record winner/loser correctly
                        self.highscore.record_game(player_ids[currentPlayer], playerScore, won=True)
                        loser_index = 1 - currentPlayer
                        self.highscore.record_game(player_ids[loser_index], players[loser_index].totalScore, won=False)
                        gameOver = True
                        continue
                    # no win: pass the turn
                    currentPlayer = 1 - currentPlayer
                    continue
                elif cheatInput == "q":
                    gameOver = True
                    break
                else:
                    die1, die2 = self.dice.roll(), self.dice.roll()
            elif is_computer_turn:
                print(f"{roller_name} chooses: ROLL")
                die1, die2 = self.dice.roll(), self.dice.roll()
            else:
                rollChoice = input("ENTER R TO ROLL or q to quit: ").strip().lower()
                if rollChoice == "r":
                    die1, die2 = self.dice.roll(), self.dice.roll()
                elif rollChoice == "q":
                    gameOver = True
                    break
                else:
                    print("INVALID CHOICE")
                    continue
                

            print(f"\n{roller_name} rolled a {die1} and a {die2}, roll total = {die1 + die2}")
            checkValue = self.checkRolls(die1, die2)
            self.dice.show(die1, die2)

            # === Roll outcomes ===
            if checkValue == 1:
                print(f"OOPS! {roller_pronoun.upper()} ROLLED A ONE — LOSE THIS ROUND SCORE.")
                self.dice.show(die1, die2)
                current_player_obj.runningScore = 0
                currentPlayer = 1 - currentPlayer
                continue
            elif checkValue == 2:
                print(f"DOUBLE 1s! {roller_pronoun.upper()} LOSE ALL POINTS.")
                self.dice.show(die1, die2)
                current_player_obj.runningScore = 0
                current_player_obj.totalScore = 0
                currentPlayer = 1 - currentPlayer
                continue
            else:
                current_player_obj.runningScore += checkValue
                print(f"{roller_name}'s running score is {current_player_obj.runningScore}\n")

            # === Hold or Repeat ===
            while True:
                if is_computer_turn:
                    decision = ai.decide(current_player_obj.runningScore, current_player_obj.totalScore)
                    repeatChoice = "1" if decision == "h" else "2"
                    print(f"{roller_name} chooses: {'HOLD' if repeatChoice == '1' else 'ROLL AGAIN'}")
                else:
                    repeatChoice = input("1. HOLD or 2. ROLL AGAIN: ").strip()

                if repeatChoice == "1":
                    # Add running to total
                    current_player_obj.totalScore += current_player_obj.runningScore
                    current_player_obj.runningScore = 0
                    print(f"{roller_name}'s TOTAL SCORE IS {current_player_obj.totalScore}\n")

                    # ✅ WIN CHECK BEFORE CHANGING TURN
                    if current_player_obj.totalScore >= self.target:
                        print(f"🏆 CONGRATULATIONS {roller_name} IS THE WINNER! 🏆")
                        # Record using the *current* player (winner)
                        self.highscore.record_game(player_ids[currentPlayer], current_player_obj.totalScore, won=True)
                        loser_index = 1 - currentPlayer
                        self.highscore.record_game(
                            player_ids[loser_index],
                            players[loser_index].totalScore,
                            won=False
                        )
                        gameOver = True
                    else:
                        # No win: pass the turn
                        currentPlayer = 1 - currentPlayer
                    break

                elif repeatChoice == "2":
                    die1, die2 = self.dice.roll(), self.dice.roll()
                    checkValueRepeat = self.checkRolls(die1, die2)
                    print(f"\n{roller_name} rolled a {die1} and a {die2}, roll total = {die1 + die2}")
                    self.dice.show(die1, die2)

                    if checkValueRepeat == 1:
                        print(f"OOPS! {roller_pronoun.upper()} LOSE THE ROUND SCORE.")
                        current_player_obj.runningScore = 0
                        currentPlayer = 1 - currentPlayer
                        break
                    elif checkValueRepeat == 2:
                        print(f"DOUBLE 1s! {roller_pronoun.upper()} LOSE ALL POINTS.")
                        self.dice.show(die1, die2)
                        current_player_obj.runningScore = 0
                        current_player_obj.totalScore = 0
                        currentPlayer = 1 - currentPlayer
                        break
                    else:
                        current_player_obj.runningScore += checkValueRepeat
                        print(f"{roller_name}'s running score is {current_player_obj.runningScore}\n")
                else:
                    print("INVALID CHOICE, turn ends.")
                    current_player_obj.runningScore = 0
                    currentPlayer = 1 - currentPlayer
                    break
