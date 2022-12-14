import unittest

from card import Card, EnergyCard


class TestCard(unittest.TestCase):
    def test_card(self):
        # Create a Card instance
        card = Card("Pikachu", "pokemon")

        # Check that the card's attributes are set correctly
        self.assertEqual(card.name, "Pikachu")
        self.assertEqual(card.card_class, "pokemon")

    def test_play(self):
        # Create a Card instance
        card = Card("Pikachu", "pokemon")

        # Check that the play method raises a NotImplementedError
        with self.assertRaises(NotImplementedError):
            card.play()

    def test_use_effect(self):
        # Create a Card instance
        card = Card("Pikachu", "pokemon")

        # Check that the use_effect method raises a NotImplementedError
        with self.assertRaises(NotImplementedError):
            card.use_effect()

    def test_discard(self):
        # Create a Card instance
        card = Card("Pikachu", "pokemon")

        # Check that the discard method returns True
        self.assertTrue(card.discard())


class TestEnergyCard(unittest.TestCase):
    def test_energy_card(self):
        # Create an EnergyCard instance
        card = EnergyCard(name="Fire Energy", energy_type="fire")

        # Check that the card's attributes are set correctly
        self.assertEqual(card.name, "Fire Energy")
        self.assertEqual(card.energy_type, "fire")
        self.assertEqual(card.amount, 1)


if __name__ == "__main__":
    unittest.main()
