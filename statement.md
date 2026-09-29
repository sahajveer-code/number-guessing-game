# Project Statement: Number Guessing Game

## 1. Problem Statement

Beginners learning Python often struggle to connect isolated concepts such as variables, loops, conditionals, functions, lists and exception handling into a single working program. Reading about these ideas is not the same as applying them together, and many practice exercises are either too trivial or too large for a first-year learner.

This project addresses that gap by building a small, interactive command-line game, the **Number Guessing Game**. The computer picks a secret number between 1 and 100, and the player must find it within a limited number of attempts. The game must respond to every kind of player input, including valid guesses, out-of-range numbers, repeated guesses and non-numeric text, without crashing.

## 2. Scope of the Project

### In Scope
- A command-line game written in Python 3 using only the standard library (`random`).
- A randomly generated secret number between 1 and 100 for every round.
- A maximum of 7 attempts per round.
- Feedback after each guess: too high, too low, or correct.
- Input validation for:
  - non-numeric input,
  - numbers outside the range 1 to 100,
  - duplicate guesses within the same round.
- Tracking and display of previous guesses and remaining chances.
- A replay option so the player can start a new round without restarting the program.

### Out of Scope
- Graphical user interface or web/mobile version.
- Multiplayer mode, user accounts or online leaderboards.
- Persistent storage of scores or game history.
- Adjustable difficulty levels or custom number ranges.

## 3. Target Users

- **Beginner Python learners** who want a practical example of core programming concepts working together.
- **Students and instructors** who need a simple, readable reference project for teaching control flow, functions, lists and input handling.
- **Casual players** who want a quick, lightweight game that runs in any terminal.

## 4. High-Level Features

| # | Feature | Description |
|---|---------|-------------|
| 1 | Random number generation | Picks a secret number from 1 to 100 using `random.randint()`. |
| 2 | Limited attempts | Gives the player 7 chances per round and shows the number remaining. |
| 3 | Hints | Tells the player whether each guess is too high or too low. |
| 4 | Input validation | Handles non-numeric and out-of-range entries with clear messages, without using up an attempt. |
| 5 | Duplicate guess prevention | Rejects a number that was already guessed in the current round. |
| 6 | Guess history | Displays all previous guesses after each attempt. |
| 7 | Win/lose result | Shows the number of guesses on a win, or reveals the secret number on a loss. |
| 8 | Replay | Asks whether the player wants another round after each game ends. |

## 5. Technology

- **Language:** Python 3
- **Libraries:** `random` (Python standard library, no external dependencies)
- **Interface:** Command-line / terminal
