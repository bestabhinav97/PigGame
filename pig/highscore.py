"""High score management module for the Pig game.

Handles saving, loading, updating, and displaying player scores
using a local JSON file.
"""

import json
import os
import uuid


class HighScore:
    """Manages player statistics including wins, total games, and highest scores."""

    def __init__(self, filename="highscore.json"):
        """Initialize the HighScore manager with a filename and load existing scores."""
        self.filename = filename
        self.scores = self.load_scores()

    def load_scores(self):
        """Load player scores from a JSON file.

        Return an empty dict if file is missing or invalid.
        """
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return {}
        return {}

    def save_scores(self):
        """Save all player scores to the JSON file."""
        with open(self.filename, "w") as f:
            json.dump(self.scores, f, indent=4)

    def get_or_create_player(self, name):
        """Return player ID if found; otherwise, create a new player entry."""
        normalized_name = name.strip().lower()
        for pid, data in self.scores.items():
            if data["name"].strip().lower() == normalized_name:
                if data["name"] != name:
                    data["name"] = name
                    self.save_scores()
                return pid

        new_id = str(uuid.uuid4())
        self.scores[new_id] = {
            "name": name,
            "total_games": 0,
            "wins": 0,
            "highest_score": 0,
        }
        self.save_scores()
        return new_id

    def rename_player(self, player_id, new_name):
        """Rename player safely — if name already exists, merge stats and return final active ID."""
        if player_id not in self.scores:
            return player_id

        new_name_lower = new_name.strip().lower()
        existing_id = None
        for pid, data in self.scores.items():
            if pid != player_id and data["name"].strip().lower() == new_name_lower:
                existing_id = pid
                break

        if existing_id:
            existing = self.scores[existing_id]
            renamed = self.scores[player_id]
            existing["total_games"] += renamed["total_games"]
            existing["wins"] += renamed["wins"]
            if renamed["highest_score"] > existing["highest_score"]:
                existing["highest_score"] = renamed["highest_score"]
            existing["name"] = new_name
            del self.scores[player_id]
            self.save_scores()
            return existing_id
        else:
            self.scores[player_id]["name"] = new_name
            self.save_scores()
            return player_id  # ✅ return same ID if no merge

    def record_game(self, player_id, score, won=False):
        """Update player stats after each game, including wins and highest score."""
        if player_id in self.scores:
            player = self.scores[player_id]
            player["total_games"] += 1
            if won:
                player["wins"] += 1
            if score > player["highest_score"]:
                player["highest_score"] = score
            self.save_scores()

    def display_scores(self):
        """Print all recorded player statistics in a formatted leaderboard."""
        print("\n🏆 High Scores 🏆")
        print("----------------------------------------")
        for data in self.scores.values():
            print(
                f"{data['name']:<15} | Games: {data['total_games']:<3} | "
                f"Wins: {data['wins']:<3} | Highest: {data['highest_score']}"
            )
        print("----------------------------------------")
