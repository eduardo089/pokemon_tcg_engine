from card import EnergyCard, TrainerCard, PokemonCard
from deck import Deck
from player import Player

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pikachu = PokemonCard(name='Pikachu', attack=10, defense=10, health_points=100)
    charmander = PokemonCard(name='Charmander', attack=10, defense=10, health_points=100)

    pikachu.add_energy_type('electric')
    charmander.add_energy_type('fire')

