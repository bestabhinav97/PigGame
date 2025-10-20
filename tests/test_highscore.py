"""Unit tests for the HighScore class.

Verifies saving, loading, renaming, and tracking of player stats.
"""

import unittest
from unittest.mock import mock_open, patch
from pig.highscore import HighScore
import json


class TestHighScore(unittest.TestCase):
    """Test suite for verifying HighScore class behavior."""

    # ---------- Setup ----------
    def setUp(self):
        """Initialize mock data for repeated test usage."""
        self.mock_data = {
            "123": {"name": "Alice", "total_games": 3, "wins": 2, "highest_score": 80},
            "456": {"name": "Bob", "total_games": 2, "wins": 1, "highest_score": 60},
        }

    # ---------- 1. load_scores ----------
    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data=json.dumps({"x": {"name": "Test"}}),
    )
    @patch("os.path.exists", return_value=True)
    def test_load_scores_valid_file(self, mock_exists, mock_opened):
        """Test loading scores from a valid JSON file."""
        hs = HighScore("fakefile.json")
        self.assertIn("x", hs.scores)
        self.assertEqual(hs.scores["x"]["name"], "Test")

    # ---------- 2. load_scores invalid JSON ----------
    @patch("builtins.open", new_callable=mock_open, read_data="{invalid_json}")
    @patch("os.path.exists", return_value=True)
    def test_load_scores_invalid_json(self, mock_exists, mock_opened):
        """Ensure invalid JSON returns an empty dictionary."""
        hs = HighScore("fake.json")
        self.assertEqual(hs.scores, {})

    # ---------- 3. get_or_create_player new ----------
    @patch("pig.highscore.HighScore.save_scores")
    def test_get_or_create_player_new(self, mock_save):
        """Create a new player if not found in scores."""
        hs = HighScore()
        hs.scores = {}
        new_id = hs.get_or_create_player("Charlie")
        self.assertIn(new_id, hs.scores)
        self.assertEqual(hs.scores[new_id]["name"], "Charlie")

    # ---------- 4. get_or_create_player existing (case-insensitive) ----------
    @patch("pig.highscore.HighScore.save_scores")
    def test_get_or_create_player_existing_case_insensitive(self, mock_save):
        """Return existing player ID even if name case differs."""
        hs = HighScore()
        hs.scores = {
            "123": {"name": "Alice", "total_games": 1, "wins": 0, "highest_score": 20}
        }
        pid = hs.get_or_create_player("alice")
        self.assertEqual(pid, "123")

    # ---------- 5. rename_player simple ----------
    @patch("pig.highscore.HighScore.save_scores")
    def test_rename_player_no_conflict(self, mock_save):
        """Rename a player when there is no name conflict."""
        hs = HighScore()
        hs.scores = {
            "111": {"name": "OldName", "total_games": 1, "wins": 0, "highest_score": 10}
        }
        result = hs.rename_player("111", "NewName")
        self.assertEqual(result, "111")
        self.assertEqual(hs.scores["111"]["name"], "NewName")

    # ---------- 6. rename_player merge existing ----------
    @patch("pig.highscore.HighScore.save_scores")
    def test_rename_player_merge(self, mock_save):
        """Merge stats if renaming conflicts with another player's name."""
        hs = HighScore()
        hs.scores = {
            "a1": {"name": "Player1", "total_games": 2, "wins": 1, "highest_score": 50},
            "b2": {"name": "Target", "total_games": 3, "wins": 2, "highest_score": 60},
        }
        merged_id = hs.rename_player("a1", "Target")
        self.assertEqual(merged_id, "b2")
        self.assertNotIn("a1", hs.scores)
        self.assertEqual(hs.scores["b2"]["total_games"], 5)
        self.assertEqual(hs.scores["b2"]["wins"], 3)
        self.assertEqual(hs.scores["b2"]["highest_score"], 60)

    # ---------- 7. record_game win ----------
    @patch("pig.highscore.HighScore.save_scores")
    def test_record_game_win(self, mock_save):
        """Ensure record_game updates wins and highest score when applicable."""
        hs = HighScore()
        hs.scores = {
            "id1": {"name": "Alice", "total_games": 1, "wins": 0, "highest_score": 40}
        }
        hs.record_game("id1", 70, won=True)
        player = hs.scores["id1"]
        self.assertEqual(player["total_games"], 2)
        self.assertEqual(player["wins"], 1)
        self.assertEqual(player["highest_score"], 70)

    # ---------- 8. record_game higher_score ----------
    @patch("pig.highscore.HighScore.save_scores")
    def test_record_game_highest_score_update(self, mock_save):
        """Do not update highest score if new score is lower."""
        hs = HighScore()
        hs.scores = {
            "id1": {"name": "Bob", "total_games": 0, "wins": 0, "highest_score": 90}
        }
        hs.record_game("id1", 50, won=False)
        self.assertEqual(hs.scores["id1"]["highest_score"], 90)

    # ---------- 9. record_game nonexistent_id ----------
    @patch("pig.highscore.HighScore.save_scores")
    def test_record_game_nonexistent(self, mock_save):
        """Ensure record_game ignores nonexistent player IDs gracefully."""
        hs = HighScore()
        hs.scores = {}
        hs.record_game("ghost", 50, won=True)
        self.assertEqual(hs.scores, {})

    # ---------- 10. display_scores prints properly ----------
    def test_display_scores_output(self):
        """Ensure display_scores prints expected output with player info."""
        hs = HighScore()
        hs.scores = {
            "1": {"name": "Alice", "total_games": 3, "wins": 1, "highest_score": 80},
            "2": {"name": "Bob", "total_games": 2, "wins": 1, "highest_score": 60},
        }
        with patch("builtins.print") as mock_print:
            hs.display_scores()
        printed = " ".join([str(call) for call in mock_print.call_args_list])
        self.assertIn("Alice", printed)
        self.assertIn("High Scores", printed)


if __name__ == "__main__":
    unittest.main()
