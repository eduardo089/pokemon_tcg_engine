from typing import Optional

from enumerators import CardClasses


class Card:
    name: str
    card_class: Optional[str]

    def __init__(self, name: str, card_class: str):
        self.name = name
        # Check that the energy card_class is valid
        if card_class not in CardClasses.list():
            raise ValueError(f"Invalid card class: {card_class} should be one of either trainer, energy or pokemon")
        self.card_class = card_class

    def play(self, game, player):
        # TODO: add play actions
        # Perform common actions when a card is played, such as
        # removing the card from the player's hand and adding it
        # to the game state
        pass

    def discard(self, game, player):
        # TODO: add discard actions
        # Perform common actions when a card is discarded, such as
        # removing the card from the game and adding it to the
        # discard pile
        pass




