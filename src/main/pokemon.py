import requests


def getPokemon(pokemon: str) -> dict | Exception:
    req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")

    if req.status_code == 200:
        json_data = req.json()
        print(f"{int(json_data["height"]) / 10} meter")
        print(f"{int(json_data["weight"]) / 10} kg")
        return json_data
    else:
        return Exception(f"Pokemon {pokemon} not found. Error code: {req.status_code}")