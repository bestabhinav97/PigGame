# PigGame – Assignment 2: Test-Driven Development

This project was developed as part of the course Methods for Sustainable Programming at Kristianstad University. The assignment focused on creating and testing an object-oriented Python game using Test-Driven Development.

PigGame is a Python version of the traditional Pig Dice Game. Players take turns rolling two dice and try to reach 100 points first (the winning score can be changed in game.py line 18). Rolling a 1 ends the player’s turn and removes their round points, while rolling two 1s resets the total score. The game can be played against another player or against the computer using an AI opponent. The main goal of this project was to apply object-oriented design, continuous testing, and clean code practices throughout development.

The program follows a structure that includes the following classes: Game, Dice, Player, Intelligence, and Highscore. It also features an AI opponent with adjustable difficulty, a persistent high-score system using JSON, comprehensive unit tests for all components, UML diagrams and HTML documentation, and full PEP-compliant code formatting verified with flake8 and pylint.

## Installation

To install and run the game on your system, follow these steps:

INSTALATION FOR MAC
```bash
git clone https://github.com/bestabhinav97/PigGame.git
cd PigGame
python3 -m venv venv
source venv/bin/activate
pip install -r requirements-alt.txt
python main.py
```

INSTALLATION FOR WINDOWS
```cmdPrompt
git clone https://github.com/bestabhinav97/PigGame.git
cd pigGame
python venv -m venv
venv\scripts\activate
pip install -r requirements.txt
python main.py
```

## Testing

The project includes automated tests for all key components. To run the tests and verify coverage, use:

```bash
pytest --cov=pig --cov-report=term-missing
```

```cmdPrompt
pytest
```

You can also check code style with:

```bash
flake8 --max-line-length=120 --docstring-convention=google pig tests
pylint pig --disable=C0114,C0115,C0116
```

```cmdPropmt
flake8 .
pylint pig
```

All tests pass successfully

## Documentation

Documentation and diagrams are already included in the repository. The file docs/html/index.html opens the full HTML documentation in a browser. UML diagrams are located at docs/uml/classes.png (class diagram) and docs/uml/packages.png (package diagram). These were generated using pdoc and pyreverse.

CREATING HTML DOCUMENTATION
```CmdPrompt
pdoc --output-dir docs/html pig
```

```Bash
pdoc --output-dir docs/html pig
```

CREATING UML DIAGRAMS
!!! MAKE SURE YOUR COMPUTER HAS GRAPHIVIZ INSTALLED AND ADDED TO SYSTEM PATH !!!
```CmdPrompt
mkdir docs\uml
pyreverse -o png -p PigGame pig -d docs\uml
```

```Bash
mkdir -p docs/uml
pyreverse -o png -p PigGame pig -d docs/uml
```


## Project Structure

```
.
├── .flake8
├── .gitignore
├── LICENSE.md
├── README.md
├── docs
│   ├── html
│   │   ├── index.html
│   │   ├── pig
│   │   │   ├── dice.html
│   │   │   ├── game.html
│   │   │   ├── highscore.html
│   │   │   ├── intelligence.html
│   │   │   └── player.html
│   │   ├── pig.html
│   │   ├── search.js
│   │   ├── tests
│   │   │   ├── test_dice.html
│   │   │   ├── test_game.html
│   │   │   ├── test_highscore.html
│   │   │   ├── test_intelligence.html
│   │   │   └── test_player.html
│   │   └── tests.html
│   └── uml
│       ├── classes.png
│       └── packages.png
├── highscore.json
├── main.py
├── pig
│   ├── __init__.py
│   ├── dice.py
│   ├── game.py
│   ├── highscore.py
│   ├── intelligence.py
│   └── player.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── test_dice.py
    ├── test_game.py
    ├── test_highscore.py
    ├── test_intelligence.py
    └── test_player.py

8 directories, 35 files
```

## License

This project is licensed under the MIT License (see LICENSE.md for details).

## Authors

Developed by Fatih Celik, Abhinav Srinivasan, and Mateusz Plizga.

© 2025 Kristianstad University – Methods for Sustainable Programming (DA214A)
