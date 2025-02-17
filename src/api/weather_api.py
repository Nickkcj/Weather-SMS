import requests
from src.config.settings import OPENWEATHER_ENDPOINT, API_KEY

def fetch_weather(lat, lon, cnt=4):
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "cnt": cnt
    }
    response = requests.get(OPENWEATHER_ENDPOINT, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch weather data: {response.status_code}, {response.text}")
