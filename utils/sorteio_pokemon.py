import random
from dados import pokemons

############## Sortiando Pokemon ##############
def sorteio_pokemon():
    return random.choice(list(pokemons.keys()))