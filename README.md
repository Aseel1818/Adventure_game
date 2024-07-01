
# Adventure Game

This is a text-based adventure game implemented in Python. The game is designed to take the player through various scenarios, making choices that will determine the outcome of the game.

## Features

- **Random Encounters**: The game uses the `random` module to create unpredictable encounters with enemies.
- **Timed Pauses**: The `time` module is used to add pauses between messages for a better user experience.
- **Interactive Gameplay**: Players make choices using loops and `if` statements to navigate through the game.
- **Combat System**: The game includes a simple combat system where the player can fight or run away from enemies.

## Requirements

- Python 3

## How to Play

1. Clone the repository or download the `adventure_game.py` file.
2. Open a terminal and navigate to the directory containing `adventure_game.py`.
3. Run the game using the command:
   ```
   python3 adventure_game.py
   ```
4. Follow the on-screen prompts to play the game.

## Game Structure

- The game starts with the player in an open field.
- The player will encounter various scenarios and must choose how to react.
- The game uses random events to keep the experience engaging and unpredictable.
- The player can encounter enemies and engage in combat or choose to run away.

## Code Overview

- **Modules Used**:
  - `random`: For generating random events and enemy encounters.
  - `time`: For adding delays between messages to improve user experience.
- **Key Components**:
  - Functions to handle different parts of the game such as `combat()`, `encounter_monster()`, `fight()` , `game_over()`,`play_again()`,`player_choices()`,`cave()`,`house()`and `print_pause()`.
  - Use of loops and `if` statements to manage the game's flow and player decisions.
## Aseel Hamayel
