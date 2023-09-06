HAND_SIZE = 7
PRIZE_AMOUNT = 6

pokemon_data = [
    {
        "name": "Bulbasaur", "health_points": 50, "pokemon_type": "grass",
        "abilities": [{"name": "Tackle",
                       "description": "A physical attack that deals 10 damage.",
                       "damage": 10,
                       "energy_reqs": {"normal": 1}
                        },
                      {"name": "Vine Whip",
                       "description": "A physical attack that deals 15 damage.",
                       "damage": 15,
                       "energy_reqs": {"grass": 1}
                       }]
    },
    {
        "name": "Charmander",
        "health_points": 50,
        "pokemon_type": "fire",
        "abilities": [
            {
                "name": "Scratch",
                "description": "A physical attack that deals 5 damage.",
                "damage": 5,
                "energy_reqs": {"normal": 1}
            }
        ]
    },
    {
        "name": "Squirtle",
        "health_points": 50,
        "pokemon_type": "water",
        "abilities": [
            {
                "name": "Tail Whip",
                "description": "A physical attack that deals 5 damage.",
                "damage": 5,
                "energy_reqs": {"normal": 1}
            }
        ]
    },
    {
        "name": "Pikachu",
        "health_points": 50,
        "pokemon_type": "electric",
        "abilities": [
            {
                "name": "Thunder Shock",
                "description": "An electric attack that deals 5 damage.",
                "damage": 5,
                "energy_reqs": {"electric": 1}
            }
        ]
    },
    {
        "name": "Abra",
        "health_points": 50,
        "pokemon_type": "psychic",
        "abilities": [
            {
                "name": "Confusion",
                "description": "A psychic attack that deals 5 damage.",
                "damage": 5,
                "energy_reqs": {"psychic": 1}
            }
        ]
    }
]



energy_data = [
    {
        "name": "Grass Energy",
        "energy_type": "grass",
        "amount": 1
    },
    {
        "name": "Fire Energy",
        "energy_type": "fire",
        "amount": 1
    },
    {
        "name": "Water Energy",
        "energy_type": "water",
        "amount": 1
    },
    {
        "name": "Lightning Energy",
        "energy_type": "electric",
        "amount": 1
    },
    {
        "name": "Psychic Energy",
        "energy_type": "psychic",
        "amount": 1
    }
]

