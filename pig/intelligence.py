from .dice import Dice

class Intelligence:
    """
    Very simple AI for Pig:
    - Uses a small "hold threshold" based on difficulty.
    - If the AI can win by holding, it holds.
    - Otherwise it keeps rolling until the turn total reaches the threshold.
    """

    def __init__(self):
        self.dice = Dice()

    _THRESHOLDS = {
        "easy": 8,
        "medium": 12,
        "hard": 18,
    }



    
    def __init__(self, difficulty: str = "medium", target_score: int = 100) -> None:
        if difficulty not in self._THRESHOLDS:
            difficulty = "medium"
        self.difficulty = difficulty
        self.threshold = self._THRESHOLDS[difficulty]
        self.target = target_score

    def decide(self, turn_total: int, ai_score: int) -> str:
        """
        Return 'r' (roll) or 'h' (hold).
        """
        # If AI can win by holding now
        if ai_score + turn_total >= self.target:
            return "h"

        # Hold when threshold reached
        if turn_total >= self.threshold:
            return "h"

        # Otherwise roll again
        return "r"
    
    
