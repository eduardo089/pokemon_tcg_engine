from typing import List, Dict

from ability import Ability
from cards.card import Card
from cards.energy_card import EnergyCard
from enumerators import EnergyTypes, CardClasses


class PokemonCard(Card):
    health_points: int
    abilities: Dict[str, Ability]
    energies: List[EnergyCard]
    pokemon_type: str
    is_ko: bool

    def __init__(self, name: str, health_points: int, pokemon_type: str, abilities: List[Ability]) -> None:
        """
        Instance a new Pokémon Card

        :param name: Name of the Pokémon Card
        :param health_points: Amount of health points
        :param pokemon_type: Type of the Pokémon, one of CardClasses.POKEMON values
        """
        if pokemon_type not in EnergyTypes.list():
            print(EnergyTypes)
            raise ValueError(f"Invalid pokemon type: {pokemon_type}")
        super().__init__(name, card_class=CardClasses.POKEMON.value)
        self.health_points = health_points
        # TODO: add abilities as strings
        abilities = {}
        for ability in abilities:
            self.abilities[ability.name] = ability
        self.abilities = {}
        self.energies = []
        self.pokemon_type = pokemon_type
        self.is_ko = False

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
        Removes an energy attached to a Pokémon card

        :param energy: The EnergyCard object to be removed
        :return: None
        """
        self.energies.remove(energy)

    def use_ability(self, ability_str: str, other_pokemon):
        if not isinstance(other_pokemon, PokemonCard):
            raise ValueError(f"Other Pokemon should be PokemonCard type but got {type(other_pokemon)} instead")
        if ability_str not in self.abilities.keys():
            raise ValueError(f"Ability {ability_str} not found")

        # TODO: Eventually you would need not only to pass the other pokemon but the whole game in order
        # to make the ability work
        self.abilities[ability_str].use(my_pokemon=self, other_pokemon=other_pokemon)

    def take_damage(self, damage) -> None:
        """
        Takes damage from the attack

        :param damage: The amount of damage to be taken
        :return: None
        """
        self.health_points -= damage
        self.check_ko()

    def check_ko(self) -> None:
        if self.health_points <= 0:
            self.is_ko = True
            print(f"Pokemon {self.name} is KO")

    def get_card_info(self) -> str:
        return f"Card name: {self.name}\n" \
               f"Card class: {self.card_class}\n" \
               f"Health Points: {self.health_points}"
        # TODO: add abilities as string

    # TODO: add evolution logic

