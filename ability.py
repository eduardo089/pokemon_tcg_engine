from typing import List

from card import EnergyCard


class Ability:
    name: str
    description: str
    damage: int
    energy_req: List[EnergyCard]

    def __init__(self, name: str, description: str, damage: int, energy_req: List[EnergyCard]):
        self.name = name
        self.description = description
        self.damage = damage
        self.energy_req = energy_req

    def get_damage(self):
        return self.damage

    @staticmethod
    def has_required_energy(energy_req: List[EnergyCard], energy_list: List[EnergyCard]):
        # TODO: add logic to check energy requirements
        pass
