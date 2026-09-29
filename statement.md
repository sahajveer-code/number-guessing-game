# Project Statement: Number Guessing Game

## 1. Problem Statement

Novices who start to learn Python sometimes have difficulties putting together the separate elements like variables, loops, conditionals, functions, lists, and error handling to create an application that works properly. Studying these elements is quite different from combining them in one solution, and many exercises are either too simple or too complex for the beginning of a first year.

To overcome these difficulties, I am going to create a simple interactive game on the command line called the **Number Guessing Game**. It will generate a random number from 1 to 100, and the player should guess what it is using a certain amount of tries. This application should work with any user input without breaking down.

## 2. Scope of the Project

### In Scope
- A command-line game implemented in Python 3 language with the usage of only built-in modules (`random` module).
- A randomly chosen secret number within the 1-100 range in every round.
- A limit of 7 attempts per round.
- Providing feedback after every guess about whether the guess is higher, lower or equal to the secret number.
- Checking user's input for:
  - non-numeric values,
  - guessing outside of the 1-100 range,
  - repeated guess in one round.
- Keeping track of previously guessed numbers and chances left.
- An ability to play another round without restarting the program.

### Out of Scope
- Graphical user interface or web/mobile variant.
- Multiplayer option, user account creation, or online leaderboard support.
- Saving score history or game history.
- Difficulty settings or range customization options.

## 3. Target Users

- **Novice Python students** seeking an illustrative case study in how fundamental programming principles work in tandem.
- **Teachers and learners** who require a basic, easy-to-read project to demonstrate control structures, functions, lists, and user input.
- **Gaming enthusiasts** desiring a quick, lightweight game to be played on any command-line interface.

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
