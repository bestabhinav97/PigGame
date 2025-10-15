
class Player:
    def __init__(self, name):
        """Initialize a player with a name, running and total scores."""
        self.name = name
        self.runningScore = 0
        self.totalScore = 0

    def change_name(self, new_name):
        """Change player's name."""
        new_name = new_name.strip()
        if new_name:
            self.name = new_name
        else:
            print("⚠️ Invalid name. Keeping previous name.")

    def reset_scores(self):
        """Reset the player's scores."""
        self.runningScore = 0
        self.totalScore = 0
