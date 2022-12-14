from card import EnergyCard, TrainerCard, PokemonCard
from deck import Deck
from player import Player

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    pikachu = PokemonCard(name='Pikachu', health_points=100, pokemon_type='electric')
    charmander = PokemonCard(name='Charmander', health_points=100, pokemon_type='fire')

    electric_energy = EnergyCard(name='Electric Energy', energy_type='electric')
    fire_energy = EnergyCard(name='Fire Energy', energy_type='fire')
    pikachu.attach_energy(electric_energy)
    charmander.attach_energy(fire_energy)



