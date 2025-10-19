import unittest
from unittest.mock import patch
from pig.game import Game


class TestGame(unittest.TestCase):

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

    @patch('builtins.input', side_effect=[
        # Friend game setup
        '1',         
        'Alice',     
        'Bob',       
        '',          
        'r',         
        '1',         
        '',          
        'q'          
    ])
    @patch('pig.game.Dice.roll', side_effect=[3, 4])
    def test_playGame_single_turn_hold(self, mock_dice_roll, mock_input):
        """Simulate one player rolling once, holding, then quitting."""
        with patch('builtins.print'):
            game = Game()
            game.playGame()
        # Passes if no StopIteration or exceptions occur
        self.assertTrue(True)



    def test_displayCheat_output(self):
        """Ensure displayCheat prints the cheat menu."""
        game = Game()
        with patch('builtins.print') as mock_print:
            game.displayCheat()
        self.assertTrue(any("CHEAT MENU" in str(call) for call in mock_print.call_args_list))

    def test_checkRolls_normal_sum(self):
        """Normal roll (no ones) should return sum."""
        game = Game()
        self.assertEqual(game.checkRolls(2, 5), 7)

    def test_checkRolls_one_rolled(self):
        """Any single '1' in dice should return 1."""
        game = Game()
        self.assertEqual(game.checkRolls(1, 3), 1)
        self.assertEqual(game.checkRolls(4, 1), 1)

    
    
    @patch('pig.game.Dice.roll', return_value=6)
    def test_roll_method_mocked(self, mock_roll):
        """Ensure roll() uses Dice.roll() correctly."""
        game = Game()
        result = game.roll()
        mock_roll.assert_called_once()
        self.assertEqual(result, 6)

    @patch('builtins.input', side_effect=[
        # Setup for quit test
        '1',         # choose "Friend"
        'Alice',     # player1 name
        'Bob',       # player2 name
        '',          # skip rename prompt
        'q'          # immediately quit
    ])
    def test_playGame_quit_immediately(self, mock_input):
        """Simulate quitting the game right after setup."""
        with patch('builtins.print'):
            game = Game()
            game.playGame()
        # Just verifying graceful termination
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
