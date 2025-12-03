import requests


def getAndCheck(url: str):
    req = requests.get(url)
    if req.status_code != 200:
        return Exception(f"Request failed with status code: {req.status_code}")
    return req.json()
