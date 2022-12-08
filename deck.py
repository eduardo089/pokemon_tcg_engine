# Define a Deck class to manage a collection of cards
import random


class Deck:
  def __init__(self):
    self.cards = []

  def add_card(self, card):
    # Add a card to the deck
    self.cards.append(card)

  def remove_card(self, card):
    # Remove a card from the deck
    self.cards.remove(card)

  def shuffle(self):
    # Shuffle the cards in the deck
    random.shuffle(self.cards)

  def draw(self):
    # Draw a card from the top of the deck
    return self.cards.pop()