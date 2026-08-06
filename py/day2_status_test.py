import requests

URL = "https://api.open-meteo.com/v1/forecast2"
params = {
    "latitude": 35.87,
    "longitude": 128.60,
    "current_weather": True,
}

response = requests.get(URL, params=params, timeout=10)
response.raise_for_status()
print(response.status_code)