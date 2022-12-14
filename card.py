from typing import Optional, List

from enumerators import EnergyTypes, CardClasses


class Card:
    name: str
    card_class: Optional[str]

    def __init__(self, name: str, card_class: str):
        self.name = name
        # Check that the energy card_class is valid
        if card_class not in CardClasses.list():
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
    amount: int
    energy_type: str

    def __init__(self, name: str, energy_type: str, amount: int = 1):
        """
        Instance an Energy Card

        :param name: Name of the card
        :param energy_type: Type of the card, should be one of EnergyTypes
        :param amount: Amount of energy the card is worth
        """
        super().__init__(name, "energy")
        # Check that the energy type is valid
        if energy_type not in EnergyTypes.list():
            raise ValueError(f"Invalid energy type: {energy_type} should be one of {EnergyTypes.list()}")
        self.energy_type = energy_type
        self.amount = amount


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
    # FIXME: import should be on top, this is a hack not to get circular imports
    from ability import Ability

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
        # TODO: figure out how to attack with a card
        self.abilities.append(ability)

    def remove_energy(self, energy: EnergyCard):
        self.energies.remove(energy)

    def knock_out(self):
        # TODO: logic for dead cards
        pass


