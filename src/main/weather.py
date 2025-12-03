import requests
from util import getAndCheck

def getWeatherInfo() -> str | Exception:
    key = "7be1f4f13ae9483c08b4762c1f473765"
    req = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat=60&lon=10&appid={key}&units=metric")
    if req.status_code != 200:
        return Exception(f"Could not get weather info. Error code: {req.status_code}")

    return f"It's {req.json()["main"]["temp"]} degrees celsius"