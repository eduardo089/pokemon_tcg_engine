from cards.card import Card
from enumerators import CardClasses


class TrainerCard(Card):
    def __init__(self, name, effect):
        super().__init__(name, card_class=CardClasses.TRAINER.value)
        self.effect = effect

    def use(self, game, player):
        # TODO: (Very hard) figure how to generalize the abilites of a trainer card
        # Perform actions specific to trainer cards, such as
        # applying the card's effect to the game state
        pass

    def get_card_info(self):
        pass

