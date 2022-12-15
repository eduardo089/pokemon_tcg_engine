import unittest

from cards.energy_card import EnergyCard


class TestEnergyCard(unittest.TestCase):
    def test_energy_card(self):
        # Create an EnergyCard instance
        card = EnergyCard(name="Fire Energy", energy_type="fire")

        # Check that the card's attributes are set correctly
        self.assertEqual(card.name, "Fire Energy")
        self.assertEqual(card.energy_type, "fire")
        self.assertEqual(card.amount, 1)
