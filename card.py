from typing import Optional, List

from ability import Ability
from enumerators import EnergyTypes, CardClasses


class Card:
    name: str
    card_class: Optional[str]

    def __init__(self, name: str, card_class: str):
        self.name = name
        # Check that the energy card_class is valid
        if card_class not in CardClasses:
            raise ValueError(f"Invalid card class: {card_class} should be one of either trainer, energy or pokemon")
        self.card_class = card_class

    def play(self, game, player):
        # TODO: add play actions
        # Perform common actions when a card is played, such as
        # removing the card from the player's hand and adding it
        # to the game state
        pass

    def discard(self, game, player):
        # TODO: add discard actions
        # Perform common actions when a card is discarded, such as
        # removing the card from the game and adding it to the
        # discard pile
        pass


class EnergyCard(Card):
    def __init__(self, name, energy_type):
        # Call the parent class's constructor to initialize the card
        super().__init__(name, card_class=CardClasses.ENERGY.value)

        # Check that the energy card_class is valid
        if energy_type not in EnergyTypes:
            raise ValueError(f"Invalid energy type: {energy_type}")
        self.energy_type = energy_type

    def attach(self, game, player, pokemon):
        # TODO: figure out how to attach energies to cards
        # Perform actions specific to energy cards, such as
        # attaching the card to a Pokémon in play
        pass


class TrainerCard(Card):
    def __init__(self, name, effect):
        super().__init__(name, card_class=CardClasses.TRAINER.value)
        self.effect = effect

    def use(self, game, player):
        # TODO: (Very hard) figure how to generalize the abilites of a trainer card
        # Perform actions specific to trainer cards, such as
        # applying the card's effect to the game state
        pass


class PokemonCard(Card):
    name: str
    health_points: int
    abilities: List[Ability]
    energies:  List[EnergyCard]
    pokemon_type: str
    can_attack: bool

    def __init__(self, name: str, health_points: int, pokemon_type: str):
        if pokemon_type not in EnergyTypes:
            raise ValueError(f"Invalid pokemon type: {pokemon_type}")
        super().__init__(name, card_class=CardClasses.POKEMON.value)
        self.health_points = health_points
        self.pokemon_type = pokemon_type
        self.abilities = []

    def add_ability(self, ability: Ability):
        # TODO: same as a trainer card, abilities should be able to be generalized
        # Add an ability to the Pokémon's abilities
        self.abilities.append(ability)

    def add_energy_type(self, energy: EnergyCard):
        # TODO: add energy card amount (e.g. some cards have 2 energy)
        # Add an energy card_class to the Pokémon's energy types
        self.energies.append(energy)

    def use_ability(self, ability):
        # TODO: figure out how to attack with a card
        self.abilities.append(ability)

    def remove_energy(self, energy: EnergyCard):
        self.energies.remove(energy)

    def knock_out(self):
        # TODO: logic for dead cards
        pass
