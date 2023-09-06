# Define a Player class to represent the players in the game
from typing import List

from config import HAND_SIZE, PRIZE_AMOUNT
from cards.card import Card
from cards.pokemon_card import PokemonCard
from deck import Deck


class Player:
    name: str
    hand: List[Card]
    bench: List[PokemonCard]
    prize_cards: List[Card]
    deck: Deck
    discard_pile: Deck

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.bench = []
        self.prize_cards = []
        self.deck = Deck()
        self.discard_pile = Deck()

        self.deck.shuffle()

    def draw_card(self, amount: int = 1):
        self.hand += self.deck.draw(amount=amount)

    def has_pokemon_in_hand(self) -> bool:
        """
        Checks if user has a Pokémon card in their hand

        :return: Bool
        """
        result = any(isinstance(x, PokemonCard) for x in self.hand)
        if result is False:
            print(f"{self.name} has no pokemon in hand")
        return result

    def show_cards(self):
        for i, card in enumerate(self.hand):
            print(f"[{i}]: {card.name}, {card.card_class} ")


    def choose_pokemon(self):
        """
        Lets user choose a pokemon from their hand to play
        """
        if self.has_pokemon_in_hand():
            print(f"{self.name}'s hand: {self.hand}")
            pokemon_index = int(input("Choose a pokemon to play: "))
            self.bench.append(self.hand.pop(pokemon_index))
        else:
            print(f"{self.name} has no pokemon in hand")


    def setup(self):
        self.draw_card(amount=HAND_SIZE)
        has_pokemon = self.has_pokemon_in_hand()
        while not has_pokemon:
            self.deck.add_cards(self.hand)
            self.hand = []
            self.deck.shuffle()
            self.hand = self.deck.draw(amount=HAND_SIZE)
            has_pokemon = self.has_pokemon_in_hand()

        # TODO: Select active and benched pokemon
        self.prize_cards = self.deck.draw(amount=PRIZE_AMOUNT)

    def play_card(self, card, position):
        if position == "active":
            self.active = card
        elif position == "bench":
            self.bench.append(card)
