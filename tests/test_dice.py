import pytest
from pig.dice import Dice
import random


class TestDice:
    def test_roll_returns_integer_between_1_and_6(self, monkeypatch):
        dice = Dice()

        # Mock randint to ensure consistent result
        monkeypatch.setattr(random, "randint", lambda a, b: 4)
        result = dice.roll()
        assert result == 4
        assert isinstance(result, int)

    def test_roll_randomness_in_range(self):
        dice = Dice()
        results = [dice.roll() for _ in range(100)]
        # All rolls should be between 1–6
        assert all(1 <= r <= 6 for r in results)

    def test_cheatDiceRoll_returns_5_or_6(self, monkeypatch):
        dice = Dice()
        monkeypatch.setattr(random, "randint", lambda a, b: 6)
        assert dice.cheatDiceRoll() == 6

        monkeypatch.setattr(random, "randint", lambda a, b: 5)
        assert dice.cheatDiceRoll() == 5

    def test_cheatDiceRoll_randomness_in_range(self):
        dice = Dice()
        results = [dice.cheatDiceRoll() for _ in range(100)]
        assert all(5 <= r <= 6 for r in results)

    def test_dice_faces_contains_all_faces(self):
        dice = Dice()
        # should have faces 1–6
        assert set(dice.dice_faces.keys()) == {1, 2, 3, 4, 5, 6}

        # each face should be 5 lines of ASCII
        for face in dice.dice_faces.values():
            assert isinstance(face, tuple)
            assert len(face) == 5

    def test_show_prints_correct_lines(self, capsys):
        dice = Dice()
        die1, die2 = 2, 5
        dice.show(die1, die2)
        output = capsys.readouterr().out.strip().splitlines()

        # Should print 5 lines
        assert len(output) == 5

        # Verify parts of ASCII borders are present
        assert output[0].startswith("┌")
        assert output[-1].startswith("└")
        assert "●" in output[2]
