# Number Guessing Game

A simple command-line Number Guessing Game written in Python.

## Features

* Random number generation
* Three difficulty levels
* Limited attempts (3 guesses)
* Hint system
* Score calculation
* Scoreboard saved in CSV format
* Username validation

## Difficulty Modes

| Mode      | Range   |
| --------- | ------- |
| Easy      | 1 - 10  |
| Normal    | 1 - 50  |
| Difficult | 1 - 100 |

## How It Works

1. Select a difficulty mode.
2. Enter your name.
3. Guess the randomly generated number.
4. You have 3 attempts.
5. Hints are provided after incorrect guesses.
6. A score is calculated based on how close your guess is to the correct number.
7. Your highest score can be saved to a CSV leaderboard.

## Hint System

The game provides hints such as:

* Extremely close
* Far from the number
* Very far from the number
* Odd/Even hint
* Higher/Lower hint

## Score System

Score is calculated using:

```python
score = 100 - abs(random_number - guess)
```

The closer your guess is to the correct number, the higher your score.

## CSV Scoreboard

Scores are stored in:

```text
board.csv
```

Example:

```csv
Name,Score
Jahid,98
Alex,85
Sarah,91
```

## Requirements

Python 3.x

No external libraries are required.

## Running the Game

```bash
python p4.py
```

## Project Structure

```text
.
├── p4.py
├── board.csv
└── README.md
```

## Future Improvements

* Better input validation
* Custom number ranges
* Multiple rounds
* Persistent leaderboard sorting
* Difficulty-based scoring
* Graphical User Interface (GUI)

## Author

Created as a Python practice project to learn:

* Functions
* Loops
* Conditional statements
* File handling
* CSV data storage
* Random number generation
