import requests

req = requests.get("https://catfact.ninja/fact")

if req.status_code == 200:
    print(req.json()["fact"])
else:
    print(f"Error: {req.status_code}")