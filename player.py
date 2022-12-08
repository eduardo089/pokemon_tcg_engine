# Define a Player class to represent the players in the game
class Player:
  def __init__(self, name):
    self.name = name
    self.hand = []
    self.bench = []
    self.active = None
    self.prize_cards = []

  def draw_card(self, deck):
    self.hand.append(deck.draw())

  def play_card(self, card, position):
    if position == "active":
      self.active = card
    elif position == "bench":
      self.bench.append(card)
