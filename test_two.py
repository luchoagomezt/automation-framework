from forecaster import Forecaster
from forecaster import OpenWeather
import argparse


def execute(canadian_city:str = None):
    OpenWeather(canadian_city)
    forecaster = Forecaster(OpenWeather(canadian_city))
    print(forecaster)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--canadian_city', '-city', help='Canadian city, hamilton',
                        required=True, type=str)
    args = parser.parse_args()
    execute(**vars(args))
