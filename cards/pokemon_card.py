from typing import List

from ability import Ability
from cards.card import Card
from cards.energy_card import EnergyCard
from enumerators import EnergyTypes, CardClasses


class PokemonCard(Card):
    name: str
    health_points: int
    abilities: List[Ability]
    energies:  List[EnergyCard]
    pokemon_type: str
    can_attack: bool

    def __init__(self, name: str, health_points: int, pokemon_type: str):
        """
        Instance a new Pokemon Card

        :param name: Name of the Pokemon Card
        :param health_points: Amount of health points
        :param pokemon_type: Type of the pokemon, one of CardClasses.POKEMON values
        """
        if pokemon_type not in EnergyTypes.list():
            print(EnergyTypes)
            raise ValueError(f"Invalid pokemon type: {pokemon_type}")
        super().__init__(name, card_class=CardClasses.POKEMON.value)
        self.health_points = health_points
        self.abilities = []
        self.energies = []
        self.pokemon_type = pokemon_type
        self.can_attack = True

    def add_ability(self, ability: Ability):
        # TODO: same as a trainer card, abilities should be able to be generalized
        # Add an ability to the Pokémon's abilities
        self.abilities.append(ability)

    def attach_energy(self, energy: EnergyCard):
        # TODO: add energy card amount (e.g. some cards have 2 energy)
        # Add an energy card_class to the Pokémon's energy types
        self.energies.append(energy)

    def use_ability(self, ability):
        # TODO: implement simple attack system with inputs
        # your pokemkn (self) and the other pokemon plus maybe the ability???
        # TODO: figure out how to attack with a card
        self.abilities.append(ability)

    def remove_energy(self, energy: EnergyCard):
        self.energies.remove(energy)

    def knock_out(self):
        # TODO: logic for dead cards
        pass
