import json
from json import JSONDecodeError

from reporter import Reporter
import argparse


def execute(results_file):
    try:
        fp = open(results_file)
        result_json_obj = json.load(fp)
    except FileNotFoundError as err:
        print(f'FileNotFoundError: {err}')
        return
    except JSONDecodeError as err:
        print(f'JSONDecodeError: {err}')
        return

    reporter = Reporter(result_json_obj)
    print(reporter)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--results_file', '-rf', required=True,
                        help='path/name to the test results json file', type=str)
    args = parser.parse_args()
    execute(**vars(args))
