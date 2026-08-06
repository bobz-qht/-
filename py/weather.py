import requests

URL = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 35.87,
    "longitude": 128.60,
    "current_weather": True,
}

response = requests.get(URL, params=params, timeout=10)
response.raise_for_status()

data = response.json()
current = data.get("current_weather", {})

weather_code = current.get("weathercode")
weather_map = {
    0: "맑음",
    1: "대체로 맑음",
    2: "부분적으로 흐림",
    3: "흐림",
    45: "안개",
    48: "엷은 안개",
    51: "가벼운 이슬비",
    53: "보통 이슬비",
    55: "진한 이슬비",
    61: "가벼운 비",
    63: "보통 비",
    65: "강한 비",
    71: "가벼운 눈",
    73: "보통 눈",
    75: "강한 눈",
    95: "천둥번개",
    96: "천둥번개와 우박",
    99: "강한 천둥번개와 우박",
}

print("대구 현재 날씨")
print(f"기온: {current.get('temperature')}°C")
print(f"날씨: {weather_map.get(weather_code, '알 수 없음')}")
print(f"바람: {current.get('windspeed')} km/h")

test = {"name": "bob"}
print(test.get("age"))