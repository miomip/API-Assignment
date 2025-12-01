import requests


def getCatFact() -> str | Exception:
    req = requests.get("https://catfact.ninja/fact")

    if req.status_code == 200:
        return req.json()["fact"]
    else:
        return Exception(f"Could not get catfact. Error: {req.status_code}")