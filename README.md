
# PRODIGY_SD_02 - Guessing Game

This repository contains two Python programs that implement a guessing game where the user has to guess a randomly generated number between 1 and 100:
1. **Command-Line Version**: A terminal-based guessing game.
2. **GUI Version**: A graphical user interface (GUI) version using Tkinter.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Programs](#running-the-programs)
  - [Command-Line Version](#command-line-version)
  - [GUI Version](#gui-version)
- [Usage Examples](#usage-examples)
  - [Command-Line Example](#command-line-example)
  - [GUI Example](#gui-example)
- [License](#license)

## Features
- Guess a randomly generated number between 1 and 100.
- Command-line interface and graphical user interface versions available.
- Provides feedback on whether guesses are too high or too low.
- Displays the number of attempts it took to guess the correct number.

## Prerequisites
Before you begin, ensure you have the following installed:
- [Python 3.x](https://www.python.org/downloads/) (with `Tkinter` for the GUI version)
- [VS Code](https://code.visualstudio.com/) or another Python IDE (optional but recommended)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/PRODIGY_SD_02.git
   ```

2. Navigate to the project directory:
   ```bash
   cd PRODIGY_SD_02
   ```

## Running the Programs

### Command-Line Version
To run the command-line version of the guessing game:

1. Open a terminal and navigate to the project folder.
2. Run the following command:
   ```bash
   python guessing_game.py
   ```

### GUI Version
To run the GUI version of the guessing game:

1. Open a terminal and navigate to the project folder.
2. Run the following command:
   ```bash
   python guessing_game_gui.py
   ```

## Usage Examples

### Command-Line Example
```bash
Welcome to the Guessing Game!
I have chosen a number between 1 and 100. Can you guess it?
Enter your guess: 50
Too high! Try again.
Enter your guess: 25
Too low! Try again.
Enter your guess: 40
Congratulations! You've guessed the number 40 in 3 attempts.
```

### GUI Example
In the GUI window:

1. Input a number (e.g., 25) in the guess box.
2. Click the "Submit Guess" button.
3. The result will appear below the button.

## License
This project is licensed under the MIT License.
