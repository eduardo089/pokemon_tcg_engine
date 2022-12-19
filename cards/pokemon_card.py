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
    is_ko: bool

    def __init__(self, name: str, health_points: int, pokemon_type: str) -> None:
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
        self.is_ko = False

    def add_ability(self, ability: Ability) -> None:
        # TODO: same as a trainer card, abilities should be able to be generalized
        # Add an ability to the Pokémon's abilities
        self.abilities.append(ability)

    def attach_energy(self, energy: EnergyCard) -> None:
        """
        Attaches an energy to a Pokemon card

        :param energy: The EnergyCard object to be attached
        :return: None
        """
        # TODO: add energy card amount (e.g. some cards have 2 energy)
        # Add an energy card_class to the Pokémon's energy types
        self.energies.append(energy)

    def remove_energy(self, energy: EnergyCard) -> None:
        """
        Removes an energy attached to a Pokemon card

        :param energy: The EnergyCard object to be removed
        :return: None
        """
        self.energies.remove(energy)

    def use_ability(self, ability: Ability, other_pokemon):
        if not isinstance(other_pokemon, PokemonCard):
            raise ValueError(f"Other Pokemon should be PokemonCard type but got {type(other_pokemon)} instead")




        # TODO: implement simple attack system with inputs
        # your pokemkn (self) and the other pokemon plus maybe the ability???
        # TODO: figure out how to attack with a card
        pass

    def knock_out(self):
        # TODO: logic for dead cards
        pass
