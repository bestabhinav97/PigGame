
from pig.game import Game
from pig.highscore import HighScore


def main():
    while True:
        print("\n🎮 MAIN MENU 🎮")
        print("1. Play Game")
        print("2. Play with Cheat Mode 😏")
        print("3. Show Statistics / High Scores")
        print("4. Display Rules")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("Starting normal game...\n")
            game = Game()
            game.playGame(mode="normal")

        elif choice == "2":
            print("Starting CHEAT MODE... (be nice 😈)\n")
            game = Game()
            game.playGame(mode="cheat")

        elif choice == "3":
            print("Statistics / High Scores:\n")
            hs = HighScore()
            hs.display_scores()

        elif choice == "4":
            print("""
    🎲🐷 WELCOME TO THE GAME OF PIG! 🐷🎲
    ==========================================
    There are two main variations of Pig Dice:
    
    
    🎯 TWO-DICE PIG (2 Dice)
    ------------------------
    - Players roll two dice per turn.
    - If **no 1s** are rolled: sum of both dice is added to your turn total.
    - If **one die shows 1**: you lose all points for that turn (turn ends).
    - If **both dice show 1** (snake eyes): you lose **ALL** your accumulated points!
    - You can choose to HOLD anytime before rolling a 1.
    - First player to reach 100 wins.
    
    💡 TIPS:
    - Play strategically — holding too early may slow you down,
      but rolling too often might cost everything!
    ==========================================
    """)

        elif choice == "5":
            print("Exiting game... Goodbye!")
            break

        else:
            print("Invalid choice, please try again.\n")


if __name__ == "__main__":
    main()


# dumb ass nigga where is /src 
