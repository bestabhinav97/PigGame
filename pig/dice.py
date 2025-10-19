import random

class Dice:
   
    def roll(self):
        number = random.randint(1,6)
        return number
    
    def cheatDiceRoll(self):
        number = random.randint(5,6)
        return number
    
    def __init__(self):
        # 🎲 ASCII dice face templates
        self.dice_faces = {
          1: (
            "┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘"
        ),
        2: (
            "┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘"
        ),
        3: (
            "┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘"
        ),
        4: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘"
        ),
        5: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘"
        ),
        6: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘"
        )
    }
    def show(self, die1, die2):
        """Display two dice side by side using ASCII art."""
        d1_lines = self.dice_faces[die1]
        d2_lines = self.dice_faces[die2]
        for line1, line2 in zip(d1_lines, d2_lines):
            print(line1 + "   " + line2)        
    
        

