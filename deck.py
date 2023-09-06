import random
from typing import List, Optional, Union, Type

import pydantic

from cards.card import Card
from pydantic import BaseModel as PydanticBaseModel

class BaseModel(PydanticBaseModel):
    class Config:
        arbitrary_types_allowed = True


class Deck(BaseModel):
    cards: List[Card]

    def __init__(self, cards: Optional[List[Card]] = None):
        if cards is None:
            cards = []
        self.cards = cards

    def add_cards(self, cards: List[Card]) -> None:
        # Add a card to top of the deck
        for card in cards:
            self.cards.insert(0, card)
        print(f"Added {len(cards)} cards to deck")

    def remove_card(self, discard_pile, cards: List[Card]) -> None:
        if not isinstance(discard_pile, Deck):
            raise TypeError("discard_pile must be o type Deck")
        # Remove a card from the deck
        for card in cards:
            self.cards.remove(card)
            discard_pile.add_cards([card])

    def shuffle(self) -> None:
        # Shuffle the cards in the deck
        print("Shuffling...")
        random.shuffle(self.cards)

    def draw(self, amount: int = 1) -> List[Card]:
        print(f"Drawing {amount} cards")
        return [self.cards.pop(0) for _ in range(amount)]
