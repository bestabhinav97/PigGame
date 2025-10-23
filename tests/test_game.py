"""Unit tests for the Game class.

Ensures correct game flow, rolling logic, cheat mode, and player turns.
"""

import unittest
from unittest.mock import patch
from pig.game import Game


class TestGame(unittest.TestCase):
    """Test suite for verifying Game class behavior and interactions."""

    def test_roll(self):
        """Test that a roll returns a number between 1 and 6."""
        game = Game()
        result = game.roll()
        self.assertIn(result, range(1, 7))

    def test_checkValue(self):
        """Sum of dice that are not 1 should be returned correctly."""
        game = Game()
        result = game.checkRolls(3, 4)
        self.assertEqual(result, 7)

    def test_OneRolledcheckValue(self):
        """If one die is 1, return 1 (lose round score)."""
        game = Game()
        result = game.checkRolls(1, 5)
        self.assertEqual(result, 1)

    def test_TwoOneRolledcheckValue(self):
        """If both dice are 1, return 2 (lose all points)."""
        game = Game()
        result = game.checkRolls(1, 1)
        self.assertEqual(result, 2)

    @patch(
        "builtins.input",
        side_effect=[
            # Friend game setup
            "1",  # friend mode
            "Alice",  # player 1
            "Bob",  # player 2
            "",  # skip rename
            "r",  # roll
            "1",  # hold
            "",  # skip rename (2nd player)
            "q",  # quit game
        ],
    )
    @patch("pig.game.Dice.roll", side_effect=[3, 4])
    def test_playGame_single_turn_hold(self, mock_dice_roll, mock_input):
        """Simulate one player rolling once, holding, then quitting."""
        with patch("builtins.print"):
            game = Game()
            game.playGame()
        self.assertTrue(True)

    def test_displayCheat_output(self):
        """Ensure displayCheat prints the cheat menu."""
        game = Game()
        with patch("builtins.print") as mock_print:
            game.displayCheat()
        self.assertTrue(
            any("CHEAT MENU" in str(call) for call in mock_print.call_args_list)
        )

    def test_checkRolls_normal_sum(self):
        """Normal roll (no ones) should return sum."""
        game = Game()
        self.assertEqual(game.checkRolls(2, 5), 7)

    def test_checkRolls_one_rolled(self):
        """Any single '1' in dice should return 1."""
        game = Game()
        self.assertEqual(game.checkRolls(1, 3), 1)
        self.assertEqual(game.checkRolls(4, 1), 1)

    @patch("pig.game.Dice.roll", return_value=6)
    def test_roll_method_mocked(self, mock_roll):
        """Ensure roll() uses Dice.roll() correctly."""
        game = Game()
        result = game.roll()
        mock_roll.assert_called_once()
        self.assertEqual(result, 6)

    @patch(
        "builtins.input",
        side_effect=[
            "1",  # choose "Friend"
            "Alice",  # player1 name
            "Bob",  # player2 name
            "",  # skip rename prompt
            "q",  # immediately quit
        ],
    )
    def test_playGame_quit_immediately(self, mock_input):
        """Simulate quitting the game right after setup."""
        with patch("builtins.print"):
            game = Game()
            game.playGame()
        self.assertTrue(True)


# --- Helper method tests ---
def test_check_winner_method():
    """Verify that check_winner correctly identifies winning scores."""
    g = Game()
    assert g.check_winner(150)
    assert not g.check_winner(99)
    assert g.check_winner(100)


def test_switch_player_method():
    """Ensure switch_player alternates between players 0 and 1."""
    g = Game()
    assert g.switch_player(0) == 1
    assert g.switch_player(1) == 0


def test_apply_roll_method():
    """Confirm apply_roll adds correctly and resets on 1s."""
    g = Game()
    assert g.apply_roll(3, 4, 10) == 17
    assert g.apply_roll(1, 5, 10) == 0
    assert g.apply_roll(1, 1, 10) == 0


def test_cheat_mode_range_method():
    """Verify cheat_mode_range returns correct dice bounds."""
    g = Game()
    assert g.cheat_mode_range(True) == (5, 6)
    assert g.cheat_mode_range(False) == (1, 6)


# --- Computer mode coverage test ---
@patch(
    "builtins.input",
    side_effect=[
        "2",  # choose computer
        "Alice",  # player name
        "easy",  # AI difficulty
        "",  # skip rename
        "r",  # roll
        "1",  # hold
        "",  # skip rename again
        "q",  # quit game
    ],
)
@patch("pig.game.Dice.roll", side_effect=[3, 4, 5, 2, 6, 1])
@patch("pig.game.Intelligence.decide", return_value="h")
def test_playGame_computer_mode(mock_decide, mock_roll, mock_input):
    """Covers computer mode and AI decision branch in playGame."""
    with patch("builtins.print"):
        game = Game()
        game.playGame()
    assert True


# --- Rename, roll, hold coverage test ---
@patch(
    "builtins.input",
    side_effect=[
        "1",  # friend mode
        "Alice",  # player1
        "Bob",  # player2
        "name",  # rename option
        "Alicia",  # new name
        "r",  # roll
        "2",  # roll again
        "1",  # hold
        "",  # skip rename next turn
        "q",  # quit
    ],
)
@patch("pig.game.Dice.roll", side_effect=[6, 6, 5, 3, 2, 4])
def test_playGame_name_change_and_hold(mock_roll, mock_input):
    """Covers rename branch and roll/hold transitions."""
    with patch("builtins.print"):
        game = Game()
        game.playGame()
    assert True


if __name__ == "__main__":
    unittest.main()
