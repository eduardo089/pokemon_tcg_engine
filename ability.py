from typing import List, Dict
from cards.energy_card import EnergyCard


class Ability:
    name: str
    description: str
    damage: int
    energy_req: Dict[str, int]

    def __init__(self, name: str, description: str, damage: int, energy_req: Dict[str, int]):
        self.name = name
        self.description = description
        self.damage = damage
        self.energy_req = energy_req

    def get_damage(self):
        return self.damage

    @staticmethod
    def has_required_energy(energy_reqs: Dict[str, int], energy_list: List[EnergyCard]) -> bool:
        # TODO: add logic to check energy requirements
        # List to dict:
        dict_energies = {}
        for energy in energy_list:
            try:
                dict_energies[energy.name] += energy.amount
            except KeyError:
                dict_energies[energy.name] = energy.amount

        # Check energies that aren't normal type:
        for energy_req, amount_req in energy_reqs.items():
            if energy_req.startswith('normal'):
                continue
            if dict_energies[energy_req] < amount_req:
                return False
            else:
                dict_energies[energy_req] -= amount_req

        # Check normal type energies:
        if "normal" in energy_reqs:
            if energy_reqs["normal"] <= sum([value for key, value in dict_energies.items()]):
                return True
            else:
                return False

