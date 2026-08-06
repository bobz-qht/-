import requests

URL = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 35.87,
    "longitude": 128.60,
    "current_weather": True,
}

response = requests.get(URL, params=params, timeout=10)
print(response.status_code)