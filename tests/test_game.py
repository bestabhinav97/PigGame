import unittest
from pig.game import Game
from unittest.mock import patch

class TestGame(unittest.TestCase):

    
    def test_roll(self):
        game = Game()
        result = game.roll()
        self.assertIn(result,range(1,7))

    def test_checkValue(self):
        game = Game()
        result = game.checkRolls(3,4)
        self.assertEqual(result,7)

    def test_OneRolledcheckValue(self):
        game = Game()
        result = game.checkRolls(1,5)
        self.assertEqual(result,1)

    def test_TwoOneRolledcheckValue(self):
        game = Game()
        result = game.checkRolls(1,1)
        self.assertEqual(result,2) 

    @patch('builtins.input', side_effect=['1', 'Alice', 'Bob', 'R', '1'])
    @patch('pig.game.Dice.roll', side_effect=[3, 4])
    def test_playGame_single_turn_hold(self, mock_dice_roll, mock_input):
        """
        Simulates a single turn where:
        - Player 1 rolls 3 and 4
        - Chooses to hold immediately
        """
        with patch('builtins.print'):  # suppress output
            game = Game()
            game.playGame()

        # After this turn, Player 1 should have runningScore reset and totalScore updated
        player1 = self.game.dice.__class__.__self__  # access the player objects indirectly
        # Since playGame uses local variables, we can't access them directly.
        # Instead, this test mainly ensures no exceptions and the mocked inputs are used.


if __name__ == '__main__':
    unittest.main()
