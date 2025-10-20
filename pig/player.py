"""Player class for the Pig game.

Defines a Player with name and score-tracking methods.
"""


class Player:
    """Represents a player in the Pig Dice Game, storing their name and scores."""

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
        """Reset both running and total scores to zero."""
        self.runningScore = 0
        self.totalScore = 0
