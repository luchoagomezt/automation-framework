import json
from Automation.reporter import Reporter
import argparse


def execute(path_to_results_file):
    result_json_obj = json.load(path_to_results_file)
    reporter = Reporter(result_json_obj)
    print(reporter)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--results_file', '-rf', help='path/name to test results json file', type=str)