"""Unit tests for the Player class.

Checks initialization, score resetting, and name handling.
"""

from pig.player import Player


class TestPlayer:
    """Test suite for verifying Player class attributes and methods."""

    def test_initialization_sets_defaults(self):
        """Player should initialize with correct name and zero scores."""
        player = Player("Alice")
        assert player.name == "Alice"
        assert player.runningScore == 0
        assert player.totalScore == 0

    def test_change_name_valid(self):
        """Changing to a valid name should update successfully."""
        player = Player("Bob")
        player.change_name("Charlie")
        assert player.name == "Charlie"

    def test_change_name_strips_whitespace(self):
        """Name change should strip leading/trailing spaces."""
        player = Player("Eve")
        player.change_name("   Frank   ")
        assert player.name == "Frank"

    def test_change_name_invalid_empty_string(self, capsys):
        """Empty or space-only names should not change current name."""
        player = Player("Grace")
        player.change_name("   ")
        captured = capsys.readouterr().out
        assert "Invalid name" in captured
        assert player.name == "Grace"

    def test_reset_scores_sets_both_to_zero(self):
        """Resetting scores should zero both running and total scores."""
        player = Player("Heidi")
        player.runningScore = 15
        player.totalScore = 42
        player.reset_scores()
        assert player.runningScore == 0
        assert player.totalScore == 0
