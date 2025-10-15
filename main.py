
from pig.game import Game
from pig.highscore import HighScore


def main():
    while True:
        print("\n🎮 MAIN MENU 🎮")
        print("1. Play Game")
        print("2. Play with Cheat Mode 😏")
        print("3. Show Statistics / High Scores")
        print("4. Exit")

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
            print("Exiting game... Goodbye!")
            break

        else:
            print("Invalid choice, please try again.\n")


if __name__ == "__main__":
    main()
