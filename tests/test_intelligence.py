"""Unit tests for the Intelligence class.

Tests AI difficulty thresholds and roll/hold decision logic.
"""

import pytest
from pig.intelligence import Intelligence


class TestIntelligence:
    """Test suite for verifying Intelligence class logic."""

    @pytest.mark.parametrize(
        "difficulty,expected_threshold",
        [
            ("easy", 8),
            ("medium", 12),
            ("hard", 18),
        ],
    )
    def test_threshold_assignment_valid(self, difficulty, expected_threshold):
        """Ensure thresholds match expected difficulty levels."""
        ai = Intelligence(difficulty)
        assert ai.threshold == expected_threshold
        assert ai.difficulty == difficulty

    def test_invalid_difficulty_defaults_to_medium(self):
        """Ensure invalid difficulty defaults to 'medium'."""
        ai = Intelligence("impossible")
        assert ai.difficulty == "medium"
        assert ai.threshold == Intelligence._THRESHOLDS["medium"]

    def test_decide_hold_when_can_win(self):
        """AI should hold if it can win by holding."""
        ai = Intelligence("medium", target_score=100)
        result = ai.decide(turn_total=15, ai_score=90)
        assert result == "h"

    def test_decide_hold_when_reaching_threshold(self):
        """AI should hold when turn total reaches threshold."""
        ai = Intelligence("easy")
        result = ai.decide(turn_total=8, ai_score=50)
        assert result == "h"

    def test_decide_roll_when_below_threshold(self):
        """AI should roll again when below threshold."""
        ai = Intelligence("hard")
        result = ai.decide(turn_total=10, ai_score=50)
        assert result == "r"

    def test_decide_roll_when_far_from_win(self):
        """AI should roll if far from target score."""
        ai = Intelligence("medium", target_score=200)
        result = ai.decide(turn_total=10, ai_score=150)
        assert result == "r"

    def test_thresholds_dictionary_integrity(self):
        """Ensure difficulty thresholds are valid and positive integers."""
        ai = Intelligence()
        assert set(ai._THRESHOLDS.keys()) == {"easy", "medium", "hard"}
        for value in ai._THRESHOLDS.values():
            assert isinstance(value, int)
            assert value > 0
