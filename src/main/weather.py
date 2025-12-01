import requests

def getWeatherInfo() -> dict | Exception:
    lat: int = 60
    lon: int = 10
    key: str = "7be1f4f13ae9483c08b4762c1f473765"
    req = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}")
    if req.status_code == 200:
        return req.json()["main"]
    else:
        return Exception(f"Could not get weather info. Error code: {req.status_code}")