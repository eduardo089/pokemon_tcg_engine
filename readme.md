# Pokémon Trading Card Game
Author: Edu Grove (edo.grove@gmail.com)

This project is a Python implementation of the Pokémon trading card game. It includes classes and functions for representing and managing cards, decks, and game mechanics. Eventually the idea is to add additional features for AI opponents, a user interface, and online multiplayer support.

*Special Thanks to [openai](https://chat.openai.com/chat) for helping with the folder organization and the readme file

## Requirements

- Python 3.10.8
- pygame (for the user interface)
- requests (for online multiplayer support)

## Installation

To install the project and its requirements, clone the repository and run the following command in the root directory:

```
pip install -r requirements.txt
```

## Usage

To play the game, run the `game.py` script in the root directory:

```
python game.py
```
This will start the game in the terminal, allowing you to play against an AI opponent. To use the graphical user interface, run the `ui.py` script instead:

```
python ui.py
```


To play online against other players, run the `online.py` script and follow the instructions to connect to the game server.

## Documentation

The project is organized into the following files and folders:

- `card.py`: Contains the `Card`, `EnergyCard`, `TrainerCard`, and `PokemonCard` classes, which represent different types of cards in the game.
- `deck.py`: Contains the `Deck` class, which represents a deck of cards and provides methods for shuffling, drawing, and adding/removing cards.
- `game.py`: Contains the `play_game` function, which implements the main game loop and the rules for playing cards, using abilities, and attacking.
- `ai.py`: Contains the `AI` class, which implements an AI opponent that can play the game using different strategies.
- `ui.py`: Contains the `UI` class, which provides a graphical user interface for playing the game.
- `online.py`: Contains the `Online` class, which provides online multiplayer support for the game.
- `data`: Contains JSON files with data for the cards, abilities, energy types, and decks used in the game.
- `tests`: Contains unit tests for the different classes and functions in the game.
- `images`: Contains image files used in the game, such as card backs, energy symbols, and card art.
- `README.md`: This file.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
