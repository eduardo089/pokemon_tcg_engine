from cards.pokemon_card import PokemonCard
from cards.energy_card import EnergyCard
from ability import Ability

if __name__ == '__main__':

    pikachu = PokemonCard(name='Pikachu', health_points=100, pokemon_type='electric')
    charmander = PokemonCard(name='Charmander', health_points=100, pokemon_type='fire')

    print(charmander.health_points)
    electric_energy = EnergyCard(name='Electric Energy', energy_type='electric')
    fire_energy = EnergyCard(name='Fire Energy', energy_type='fire')
    pikachu.attach_energy(electric_energy)
    charmander.attach_energy(fire_energy)

    thundershock = Ability(name='Thundershock', damage=110, energy_reqs={'electric': 1})
    pikachu.add_ability(thundershock)

    pikachu.use_ability('Thundershock', charmander)

    print(charmander.health_points)



