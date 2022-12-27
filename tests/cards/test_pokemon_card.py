from unittest import TestCase
from cards.pokemon_card import PokemonCard
from cards.energy_card import EnergyCard
from ability import Ability


class TestPokemonCard(TestCase):
    def test_add_ability(self):
        """
        GIVEN: A Pokémon and an ability object
        WHEN: add_ability is called
        THEN: ability is added to Pokémon
        """
        # arrange
        pokemon = PokemonCard(name='Pikachu', health_points=100, pokemon_type='electric')
        ability = Ability(name='Thundershock', damage=110, energy_reqs={'electric': 1})

        # act
        pokemon.add_ability(ability)

        # assert
        self.assertEqual(pokemon.abilities['Thundershock'], ability)

    def test_attach_energy(self):
        """
        GIVEN: A Pokémon and an energy object
        WHEN: attach_energy is calles
        THEN: energy is attached to Pokémon
        """
        # arrange
        pokemon = PokemonCard(name='Pikachu', health_points=100, pokemon_type='electric')
        energy = EnergyCard(name='thunder', energy_type='electric')

        # act
        pokemon.attach_energy(energy)

        # assert
        self.assertEqual(pokemon.energies[0], energy)

    def test_use_ability(self):
        """
        GIVEN: A pokemon and an ability object
        WHEN: use_ability is calles
        THEN: ability is used on pokemon
        """
        # arrange
        pokemon = PokemonCard(name='Kangaskhan', health_points=100, pokemon_type='normal')
        ability = Ability(name='My Hability', damage=50, energy_reqs={'electric': 2, 'normal': 2})
        energies = [EnergyCard(name='electric energy', energy_type='electric'),
                    EnergyCard(name='electric energy', energy_type='electric'),
                    EnergyCard(name='double normal energy', energy_type='normal', amount=1),
                    EnergyCard(name='double psychic energy', energy_type='psychic', amount=2)]

        pokemon.add_ability(ability)
        for energy in energies:
            pokemon.attach_energy(energy)

        # act
        pokemon.use_ability('My Hability', other_pokemon=pokemon)

        # assert
        self.assertEqual(pokemon.health_points, 50)

    def test_remove_energy(self):
        """
        GIVEN: A Pokémon and an energy object
        WHEN: Remove_energy is called
        THEN: Energy is removed from Pokémon
        """
        # arrange
        pokemon = PokemonCard(name='Pikachu', health_points=100, pokemon_type='electric')
        energies = [EnergyCard(name='thunder', energy_type='electric'),
                    EnergyCard(name='triple energy ', energy_type='electric'),
                    ]

        EnergyCard(name='triple energy ', energy_type='electric'),

        energy = EnergyCard(name='thunder', energy_type='electric')

        # act
        pokemon.attach_energy(energy)
        pokemon.remove_energy(energy)

        # assert
        self.assertEqual(pokemon.energies, [])

    def test_knock_out(self):
        self.fail()
