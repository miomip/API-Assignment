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
        userInput = input("What do you want to do? ").lower()
        if userInput not in operations:
            print(f"{userInput} is not a valid operation")
            continue
        break
    print(operations[userInput]())