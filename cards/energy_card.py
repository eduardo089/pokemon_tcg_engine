from cards.card import Card
from enumerators import EnergyTypes


class EnergyCard(Card):
    energy_type: str
    amount: int

    def __init__(self, name: str, energy_type: str, amount: int = 1):
        """
        Instance an Energy Card

        :param name: Name of the card
        :param energy_type: Type of the card, should be one of EnergyTypes
        :param amount: Amount of energy the card is worth
        """
        super().__init__(name, "energy")
        # Check that the energy type is valid
        if energy_type not in EnergyTypes.list():
            raise ValueError(f"Invalid energy type: {energy_type} should be one of {EnergyTypes.list()}")
        self.energy_type = energy_type
        self.amount = amount

    def get_card_info(self) -> str:
        return f"Card name: {self.name}\n" \
               f"Card class: {self.card_class}\n" \
               f"Energy type: {self.energy_type}\n" \
               f"Amount: {self.amount}"
