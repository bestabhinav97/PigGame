"""Dice module for the Pig game.

This module defines the `Dice` class used to simulate rolling dice
and display their faces in ASCII format for the Pig game.
"""

import random


class Dice:
    """Represents the dice used in the Pig game, including ASCII display and roll methods."""

    def roll(self):
        """Return a random integer between 1 and 6 to simulate a normal dice roll."""
        number = random.randint(1, 6)
        return number

    def cheatDiceRoll(self):
        """Return a random integer between 5 and 6 to simulate a biased dice roll (cheat mode)."""
        number = random.randint(5, 6)
        return number

    def __init__(self):
        """Initialize dice with ASCII art for all possible faces."""
        # 🎲 ASCII dice face templates
        self.dice_faces = {
            1: (
                "┌─────────┐",
                "│         │",
                "│    ●    │",
                "│         │",
                "└─────────┘",
            ),
            2: (
                "┌─────────┐",
                "│  ●      │",
                "│         │",
                "│      ●  │",
                "└─────────┘",
            ),
            3: (
                "┌─────────┐",
                "│  ●      │",
                "│    ●    │",
                "│      ●  │",
                "└─────────┘",
            ),
            4: (
                "┌─────────┐",
                "│  ●   ●  │",
                "│         │",
                "│  ●   ●  │",
                "└─────────┘",
            ),
            5: (
                "┌─────────┐",
                "│  ●   ●  │",
                "│    ●    │",
                "│  ●   ●  │",
                "└─────────┘",
            ),
            6: (
                "┌─────────┐",
                "│  ●   ●  │",
                "│  ●   ●  │",
                "│  ●   ●  │",
                "└─────────┘",
            ),
        }

    def show(self, die1, die2):
        """Display two dice side by side using ASCII art."""
        d1_lines = self.dice_faces[die1]
        d2_lines = self.dice_faces[die2]
        for line1, line2 in zip(d1_lines, d2_lines):
            print(line1 + "   " + line2)
