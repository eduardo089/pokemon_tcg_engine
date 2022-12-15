from enum import Enum


class ExtendedEnum(Enum):
    # This is so you can check if a value is in all possible values of an enum
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class EnergyTypes(ExtendedEnum):
    FIRE = "fire"
    WATER = "water"
    GRASS = "grass"
    LIGHTNING = "electric"
    PSYCHIC = "psychic"
    FIGHTING = "fighting"
    DARKNESS = "darkness"
    METAL = "metal"
    FAIRY = "fairy"
    NORMAL = "normal"
    TRAINER = "trainer"


class CardClasses(ExtendedEnum):
    TRAINER = "trainer"
    ENERGY = "energy"
    POKEMON = "pokemon"
