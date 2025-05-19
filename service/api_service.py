import requests

BASE_URL = "http://api.open-notify.org"

def get_location():
    response = requests.get(f"{BASE_URL}/iss-now.json")
    response.raise_for_status()
    return response.json()

def get_users():
    response = requests.get(f"{BASE_URL}/astros.json")
    response.raise_for_status()
    return response.json()