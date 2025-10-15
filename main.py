
from pig.game import Game



def main():
    game = Game()

    while True:
        print("\n🎮 MAIN MENU 🎮")
        print("1. Play Normally")
        print("2. Play with Cheat Mode")
        print("3. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            game.playGame("normal")
        elif choice == "2":
            game.playGame("cheat")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()


