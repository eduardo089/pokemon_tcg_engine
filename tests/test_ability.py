import unittest

from ability import Ability
from cards.energy_card import EnergyCard


class TestCard(unittest.TestCase):
    def test_has_required_energy(self):
        """
        ARRANGE:
        ACT:
        ASSERT:
        """

        # arrange
        energy_reqs = {'fire': 2, 'water': 3, 'normal': 2}
        energies = [EnergyCard(name="fire", energy_type="fire", amount=2),
                    EnergyCard(name="water", energy_type="water", amount=1),
                    EnergyCard(name="water", energy_type="water", amount=2),
                    EnergyCard(name="psychic", energy_type="psychic", amount=3),
                    EnergyCard(name="normal", energy_type="normal", amount=1),
                    ]
        expected_result = True

        # act
        actual_result = Ability.has_required_energy(energy_reqs, energies)

        # assert
        self.assertEqual(expected_result, actual_result)