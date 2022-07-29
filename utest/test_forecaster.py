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
def up_clear_forecaster():
    from forecaster import Forecaster

    class MockOpenWeather:
        def get_current_weather_and_temperature(self) -> (str, float):
            return "Clear", 288.91

        def get_forecast_temperature(self) -> float:
            return 290.91

    return Forecaster(MockOpenWeather())


def test_print_with_api(forecaster):
    print(forecaster)


def test_print_with_mock_clouds(same_clouds_forecaster):
    print(same_clouds_forecaster)


def test_temperature_tendency_and_weather_with_rain(up_rain_forecaster):
    rel = up_rain_forecaster.calculate_temperature_tendency_and_weather()
    assert rel[0] == "UP"
    assert rel[1] == "Flashing red"


def test_print_with_mock_rain(up_clear_forecaster):
    rel = up_clear_forecaster.calculate_temperature_tendency_and_weather()
    assert rel[0] == "UP"
    assert rel[1] == "Steady green"
