from enum import Enum

class EnergyTypes(Enum):
    FIRE = "fire"
    WATER = "water"
    GRASS = "grass"
    LIGHTNING = "lightning"
    PSYCHIC = "psychic"
    FIGHTING = "fighting"
    DARKNESS = "darkness"
    METAL = "metal"
    FAIRY = "fairy"
    TRAINER = "trainer"


class CardClasses(Enum):
    TRAINER = "trainer"
    ENERGY = "energy"
    POKEMON = "pokemon"