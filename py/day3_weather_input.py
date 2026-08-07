import requests

cities = {
    "대구": {"lat": 35.8714, "lon": 128.6014},
    "서울": {"lat": 37.5665, "lon": 126.9780},
    "부산": {"lat": 35.1796, "lon": 129.0756},
}

def get_weather(city_name):
    city_info = cities.get(city_name)
    
    if city_info is None:
        print(f"'{city_name}'은(는) 목록에 없는 도시입니다.")
        return
    
    URL = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": city_info["lat"],      # 2. 그 안에서 위도 꺼내기
        "longitude": city_info["lon"],     # 3. 경도 꺼내기
        "current_weather": True,
    }
 # 여기에 API 요청 코드 (day2_multi_city.py에서 가져오기)
    try:
        response = requests.get(URL, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        result = data.get("current_weather", {})

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

    except Exception as e:
        print(f"에러 발생: {e}")# try/except로 감싸기

# 사용자 입력 받는 부분
user_input = input("날씨를 확인할 도시를 입력하세요: ")
get_weather(user_input)