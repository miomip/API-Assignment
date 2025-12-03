import requests
from util import getAndCheck


def getCatFact() -> str | Exception:
    data = getAndCheck("https://catfact.ninja/fact")
    return data["fact"]
