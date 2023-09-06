from typing import List

from cards.card import Card
from cards.pokemon_card import PokemonCard
from cards.energy_card import EnergyCard
from ability import Ability

from config import pokemon_data, energy_data
from deck import Deck

if __name__ == '__main__':
    # Instance the mock cards
    pokemon_cards = []
    energy_cards = []

    for data in pokemon_data:
        abilities = []
        for ability_data in data["abilities"]:
            ability = Ability(**ability_data)
            abilities.append(ability)
        # Remove the abilities key from the data dictionary
        data.pop("abilities")
        pokemon_card = PokemonCard(**data, abilities=abilities)
        pokemon_cards.append(pokemon_card)

    for data in energy_data:
        energy_card = EnergyCard(**data)
        energy_cards.append(energy_card)

    # Combine the cards into a single list
    cards: List[Card] = pokemon_cards + energy_cards

    print(type(cards))

    # Instance the deck
    deck = Deck(cards=cards)






