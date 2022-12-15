import unittest

from cards.card import Card


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


if __name__ == "__main__":
    unittest.main()
