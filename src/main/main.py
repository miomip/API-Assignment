from weather import getWeatherInfo
from pokemon import getPokemon
from catfact import getCatFact

operations = {
    "weather": getWeatherInfo,
    "pokemon": getPokemon,
    "catfact": getCatFact
}

if __name__ == '__main__':
    while True:
        userInput = input().lower()
        if userInput not in operations:
            print(f"{userInput} is not a valid operation")
            continue
        break
    if userInput == "pokemon":
        print(operations[userInput](input("Pokemon name: ").lower()))
    else:
        print(operations[userInput]())