import pytest


@pytest.fixture()
def forecaster():
    from forecaster import Forecaster
    from forecaster import OpenWeather

    openWeather = OpenWeather("hamilton")
    return Forecaster(openWeather)


@pytest.fixture()
def same_clouds_forecaster():
    from forecaster import Forecaster

    class MockOpenWeather:
        def get_current_weather_and_temperature(self) -> (str, float):
            return "Clouds", 288.91

        def get_forecast_temperature(self) -> float:
            return 288.91

    return Forecaster(MockOpenWeather())


@pytest.fixture()
def up_rain_forecaster():
    from forecaster import Forecaster

    class MockOpenWeather:
        def get_current_weather_and_temperature(self) -> (str, float):
            return "Rain", 288.91

        def get_forecast_temperature(self) -> float:
            return 290.91

    return Forecaster(MockOpenWeather())


@pytest.fixture()
def down_snow_forecaster():
    from forecaster import Forecaster

    class MockOpenWeather:
        def get_current_weather_and_temperature(self) -> (str, float):
            return "Snow", 288.91

        def get_forecast_temperature(self) -> float:
            return 286.91

    return Forecaster(MockOpenWeather())


@pytest.fixture()
def down_clear_forecaster():
    from forecaster import Forecaster

    class MockOpenWeather:
        def get_current_weather_and_temperature(self) -> (str, float):
            return "Clear", 288.91

        def get_forecast_temperature(self) -> float:
            return 286.91

    return Forecaster(MockOpenWeather())


def test_print_with_api(forecaster):
    rel = forecaster.calculate_temperature_tendency_and_weather()
    assert rel[0] in ["SAME", "UP", "DOWN"]
    assert rel[1] in ["Steady green", "Steady red", "Flashing red", "Flashing white"]


def test_up_with_clouds(same_clouds_forecaster):
    rel = same_clouds_forecaster.calculate_temperature_tendency_and_weather()
    assert rel[0] == "SAME"
    assert rel[1] == "Steady red"


def test_up_and_flashing_red(up_rain_forecaster):
    rel = up_rain_forecaster.calculate_temperature_tendency_and_weather()
    assert rel[0] == "UP"
    assert rel[1] == "Flashing red"


def test_down_and_clear(down_clear_forecaster):
    rel = down_clear_forecaster.calculate_temperature_tendency_and_weather()
    assert rel[0] == "DOWN"
    assert rel[1] == "Steady green"


def test_down_and_flashing_white(down_snow_forecaster):
    rel = down_snow_forecaster.calculate_temperature_tendency_and_weather()
    assert rel[0] == "DOWN"
    assert rel[1] == "Flashing white"
