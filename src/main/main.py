from weather import getWeatherInfo
from pokemon import getPokemon
from catfact import getCatFact

operations = {
    "weather": getWeatherInfo,
    "pokemon": getPokemon,
    "catfact": getCatFact
}

if __name__ == '__main__':
    userInput = input().lower()
    if userInput not in operations:
        print(f"{userInput} is not a valid operation")
        exit()
    if userInput == "pokemon":
        operations[userInput](input("Pokemon name: ").lower())
    else:
        operations[userInput]()