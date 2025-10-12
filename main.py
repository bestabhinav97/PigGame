from pig.dice import Dice
from pig.game import Game

def displayMenu():
    print("1.Play Game")
    print("2.Show statistics")
    print("3.Cheat Mode")
    print("4. Display Rules of the Game")
    
    
while True:
    displayMenu()
    choice = input("Enter your choice: ")
    
    if choice == "1":
        print("Starting game...")  # Debug line to see if this runs
        game = Game()
        game.playGame()
    elif choice == "2":
        print("Statistics - to be implemented")
    elif choice == "3":
        print("Running in cheat mode")
        game = Game()
        game.cheatMode()
    elif choice == "0":
        print("EXITING")
        break
    else:
        print("Invalid choice")

    


    

