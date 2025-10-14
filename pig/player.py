
class Player:
    def __init__(self, name):
        """Initialize a player with a name, running and total scores."""
        self.name = name
        self.runningScore = 0
        self.totalScore = 0

    def change_name(self, new_name):
        """Change player's name."""
        if new_name.strip():
            self.name = new_name.strip()
            print(f"✅ Name changed successfully to {self.name}")
        else:
            print("⚠️ Invalid name. Keeping previous name.")

    def reset_scores(self):
        """Reset the player's scores."""
        self.runningScore = 0
        self.totalScore = 0
