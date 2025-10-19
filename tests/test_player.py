import pytest
from pig.player import Player


class TestPlayer:

    def test_initialization_sets_defaults(self):
        player = Player("Alice")
        assert player.name == "Alice"
        assert player.runningScore == 0
        assert player.totalScore == 0

    def test_change_name_valid(self):
        player = Player("Bob")
        player.change_name("Charlie")
        assert player.name == "Charlie"

    def test_change_name_strips_whitespace(self):
        player = Player("Eve")
        player.change_name("   Frank   ")
        assert player.name == "Frank"

    def test_change_name_invalid_empty_string(self, capsys):
        player = Player("Grace")
        player.change_name("   ")  # invalid (only spaces)
        captured = capsys.readouterr().out
        assert "Invalid name" in captured
        assert player.name == "Grace"  # name should remain unchanged

    def test_reset_scores_sets_both_to_zero(self):
        player = Player("Heidi")
        player.runningScore = 15
        player.totalScore = 42
        player.reset_scores()
        assert player.runningScore == 0
        assert player.totalScore == 0
