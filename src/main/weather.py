import requests

def getWeatherInfo(lat: int, lon: int, key: str) -> dict | Exception:
    req = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}")
    if req.status_code == 200:
        return req.json()["main"]
    else:
        return Exception(f"Could not get weather info. Error code: {req.status_code}")