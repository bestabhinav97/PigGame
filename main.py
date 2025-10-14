
from pig.game import Game

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
        print("Statistics - to be implemented.\n")
    elif choice == "3" or choice == "0":
        print("Exiting game...")
        break
    else:
        print("Invalid choice, please try again.\n")
