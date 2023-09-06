from typing import List, Dict

from pydantic import BaseModel

from cards.energy_card import EnergyCard


class Ability(BaseModel):
    name: str
    description: str
    damage: int
    energy_reqs: Dict[str, int]

    def __init__(self, name: str, damage: int, energy_reqs: Dict[str, int], description: str = ''):
        super().__init__()
        self.name = name
        self.damage = damage
        self.energy_reqs = energy_reqs
        self.description = description

    def _has_required_energy(self, energy_list: List[EnergyCard]) -> bool:
        dict_energies: Dict[str, int] = {}  # type: ignore
        for energy in energy_list:
            try:
                dict_energies[energy.energy_type] += energy.amount
            except KeyError:
                dict_energies[energy.energy_type] = energy.amount

        # Check energies that aren't normal type:
        for energy_req, amount_req in self.energy_reqs.items():
            if energy_req.startswith('normal'):
                continue
            if dict_energies[energy_req] < amount_req:
                return False
            else:
                dict_energies[energy_req] -= amount_req

        # Check normal type energies:
        if "normal" in self.energy_reqs:
            if self.energy_reqs["normal"] > sum([value for key, value in dict_energies.items()]):
                return False

        return True

    def use(self, my_pokemon, other_pokemon) -> None:
        from cards.pokemon_card import PokemonCard
        if not isinstance(my_pokemon, PokemonCard) or not isinstance(other_pokemon, PokemonCard):
            raise TypeError(f"Ability {self.name} can only be used on PokemonCards but {my_pokemon} and"
                            f" {other_pokemon} were given")

        if not self._has_required_energy(energy_list=my_pokemon.energies):
            print(f"Pokemon {my_pokemon.name} doesn't have enough energy to use {self.name}")
        else:
            other_pokemon.take_damage(self.damage)

    # TODO: implement ability effects:
    # all abilities are simplified into either:
    # draw cards
    # flip coins
    # heal
    # add or remove pokemon
    # add or remove energies

