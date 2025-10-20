"""AI logic for the Pig game.

Defines the Intelligence class that controls AI decisions such as
when to roll or hold, based on difficulty and current scores.
"""


class Intelligence:
    """Very simple AI for Pig.

    - Uses a small "hold threshold" based on difficulty.
    - If the AI can win by holding, it holds.
    - Otherwise it keeps rolling until the turn total reaches the threshold.
    """

    _THRESHOLDS = {
        "easy": 8,
        "medium": 12,
        "hard": 18,
    }

    def __init__(self, difficulty: str = "medium", target_score: int = 100) -> None:
        """Initialize AI with chosen difficulty level and target score."""
        if difficulty not in self._THRESHOLDS:
            difficulty = "medium"
        self.difficulty = difficulty
        self.threshold = self._THRESHOLDS[difficulty]
        self.target = target_score

    def decide(self, turn_total: int, ai_score: int) -> str:
        """Decide whether to roll ('r') or hold ('h').

        The decision is based on the current score and the AI's difficulty threshold.

        Args:
            turn_total (int): The points accumulated in the current turn.
            ai_score (int): The AI player's total score so far.

        Returns:
            str: 'h' to hold or 'r' to roll again.
        """
        # If AI can win by holding now
        if ai_score + turn_total >= self.target:
            return "h"

        # Hold when threshold reached
        if turn_total >= self.threshold:
            return "h"

        # Otherwise roll again
        return "r"
