# Import the Card and Deck classes from earlier
from cards.card import TrainerCard, PokemonCard
from cards.energy_card import EnergyCard
from deck import Deck

# Create a new deck
deck = Deck()

# Add 60 cards to the deck

# 20 Pokémon cards
pikachu = PokemonCard("Pikachu", "lightning", 40, 50, 60)
pikachu.add_ability("Thunder Shock")
pikachu.attach_energy("lightning")
deck.add_card(pikachu)

charmander = PokemonCard("Charmander", "fire", 50, 60, 70)
charmander.add_ability("Flame Tail")
charmander.attach_energy("fire")
deck.add_card(charmander)

...

# 20 energy cards
lightning_energy = EnergyCard("Lightning Energy", "energy", "lightning")
deck.add_card(lightning_energy)

fire_energy = EnergyCard("Fire Energy", "energy", "fire")
deck.add_card(fire_energy)

...

# 20 trainer cards
professor_oak = TrainerCard("Professor Oak", "trainer", "Search your deck for up to 3 cards and put them into your hand")
deck.add_card(professor_oak)

poke_ball = TrainerCard("Poke Ball", "trainer", "Flip a coin. If heads, search your deck for a basic Pokémon and put it onto your bench")
deck.add_card(poke_ball)

...
