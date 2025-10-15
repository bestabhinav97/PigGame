
from pig.game import Game
from pig.highscore import HighScore  

def displayMenu():
    print("1.Play Game")
    print("2.Show statistics")
    print("3.Exit")

while True:
    displayMenu()
    choice = input("Enter your choice: ").strip()
    print("\n")

    if choice == "1":
        print("Starting game...\n")
        game = Game()
        game.playGame()

    elif choice == "2":
        print("Statistics / High Scores:\n")
        hs = HighScore()
        hs.display_scores()

    elif choice in ("3", "0"):
        print("Exiting game...")
        break

    else:
        print("Invalid choice, please try again.\n")
