# Define a Game class to represent the game itself
from player import Player


class Game:
    player1: Player
    player2: Player
    turn: Player

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.turn = player1

    def play_turn(self):
        # Allow the current player to take their turn
        # Check for game-ending conditions (e.g. one player has no cards left)
        # Switch to the next player's turn
        pass

    def check_winner(self):
        # Compare the players' scores and determine the winner
        pass
