import requests
from util import getAndCheck


def getPokemon() -> str | Exception:
    pokemon = input("Pokemon name: ").lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

    data = getAndCheck(url)

    height = int(data["height"]) / 10
    weight = int(data["weight"]) / 10

    return f"Height is {height} meter \nand it weighs {weight} kg"