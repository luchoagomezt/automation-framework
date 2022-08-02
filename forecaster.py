import requests
from requests.exceptions import HTTPError


class OpenWeather:
    APIPID:str = "55f5ab2e144704e42c8bf3522249b921"

    def __init__(self, city:str):
        self.weather = f"http://api.openweathermap.org/data/2.5/weather?" \
                       f"q={city},ca" \
                       f"&APPID={OpenWeather.APIPID}"
        self.coord = self.get_coordinates()
        self.forecast = f"http://api.openweathermap.org/data/2.5/forecast?" \
                        f"lat={self.coord[0]}" \
                        f"&lon={self.coord[1]}" \
                        f"&appid={OpenWeather.APIPID}"

    def get_coordinates(self) -> (str, str):
        try:
            response = requests.get(self.weather)
            lat = response.json()["coord"]["lat"]
            lon = response.json()["coord"]["lon"]
            return lat, lon
        except HTTPError as http_error:
            print(f"HTTPError : {http_error}")

    def get_current_weather_and_temperature(self) -> (str, float):
        try:
            response = requests.get(self.weather)
            weather_0_main = response.json()["weather"][0]["main"]
            main_temp = float(response.json()["main"]["temp"])
            return weather_0_main, main_temp
        except HTTPError as http_error:
            print(f"HTTPError : {http_error}")

    def get_forecast_temperature(self) -> float:
        try:
            response = requests.get(self.forecast)
            cnt = response.json()["cnt"]
            main_temp = float(response.json()["list"][cnt - 1]["main"]["temp"])
            return float(main_temp)
        except HTTPError as http_error:
            print(f"HTTPError : {http_error}")


class Forecaster:
    def __init__(self, weather_api: OpenWeather):
        self.api = weather_api
        self.weather_and_temperature_tendency:str = \
            self.calculate_temperature_tendency_and_weather()

    def __str__(self):
        return f"\n{self.weather_and_temperature_tendency[0]}" \
               f"\n{self.weather_and_temperature_tendency[1]}" \
               f"\n"

    def calculate_temperature_tendency_and_weather(self) -> (str, str):
        current_weather = self.api.get_current_weather_and_temperature()[0]
        current_temp  = self.api.get_current_weather_and_temperature()[1]
        forecast_temp = self.api.get_forecast_temperature()

        weather = ""
        if current_weather == "Clear":
            weather = "Steady green"
        elif current_weather == "Clouds":
            weather = "Steady red"
        elif current_weather == "Rain":
            weather = "Flashing red"
        elif current_weather == "Snow":
            weather = "Flashing white"

        temperature_tendency = ""
        if current_temp < forecast_temp:
            temperature_tendency = "UP"
        elif current_temp > forecast_temp:
            temperature_tendency = "DOWN"
        elif current_temp == forecast_temp:
            temperature_tendency = "SAME"

        return temperature_tendency, weather
