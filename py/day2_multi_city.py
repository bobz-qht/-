import requests

cities = {
    "대구": {"lat": 35.87, "lon": 128.60},
    "서울": {"lat": 37.57, "lon": 126.98},
    "부산": {"lat": 35.18, "lon": 129.08},
}

def get_weather(city_name):
    city = cities.get(city_name)  # 1. 도시 정보(딕셔너리) 꺼내기
    
    URL = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": city["lat"],      # 2. 그 안에서 위도 꺼내기
        "longitude": city["lon"],     # 3. 경도 꺼내기
        "current_weather": True,
    }
    
    response = requests.get(URL, params=params, timeout=10)
    response.raise_for_status()
    
    data = response.json()
    return data.get("current_weather", {})
print(get_weather("부산"))

result = get_weather("부산")

weather_map = {
    0: "맑음", 1: "대체로 맑음", 2: "부분적으로 흐림", 3: "흐림",
    45: "안개", 48: "옅은 안개",
    51: "가벼운 이슬비", 53: "보통 이슬비", 55: "진한 이슬비",
    61: "가벼운 비", 63: "보통 비", 65: "강한 비",
    71: "가벼운 눈", 73: "보통 눈", 75: "강한 눈",
    95: "천둥번개", 96: "천둥번개와 우박", 99: "강한 천둥번개와 우박",
}

code = result.get("weathercode")
print(f"기온: {result.get('temperature')}°C")
print(f"날씨: {weather_map.get(code, '알 수 없음')}")
print(f"바람: {result.get('windspeed')} km/h")