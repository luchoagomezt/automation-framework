from typing import List


def insert_test_in_list_by_ascending_order_of_test_name(list_of_tests: List, test_to_insert: str):
    index = 0
    while index < len(list_of_tests):
        if test_to_insert["test_name"] < list_of_tests[index]["test_name"]:
            break
        index = index + 1

    list_of_tests.insert(index, test_to_insert)


class Reporter:
    def __init__(self, result_json_obj: str):
        self.result_json_obj = result_json_obj
        self.number_of_test_suites = len(self.result_json_obj["test_suites"])
        self.test_suite_summary = []
        self.__compile_summary_for_all_test_suites()

    def __str__(self):
        to_string = "\n---Test Suite Results--- "
        for summary in self.test_suite_summary:
            to_string = to_string + f'\nsuite name: {summary["suite_name"]}'

            to_string = to_string + f'\n\tpass: {len(summary["pass"])}'
            to_string = to_string + '\n\tdetails:' if len(summary["pass"]) > 0 else to_string
            for test in summary["pass"]:
                to_string = to_string + f'\n\t\t{test}'

            to_string = to_string + f'\n\tfail: {len(summary["fail"])}'
            to_string = to_string + '\n\tdetails:' if len(summary["fail"]) > 0 else to_string
            for test in summary["fail"]:
                to_string = to_string + f'\n\t\t{test}'

            to_string = to_string + f'\n\tblocked: {len(summary["blocked"])}'

            to_string = to_string + f'\n\ttotal number of test case that took more than 10s: {summary["long_execution"]}'

        return to_string

    def __compile_summary_for_all_test_suites(self):
        for i in range(self.number_of_test_suites):
            summary = {"suite_name": self.result_json_obj["test_suites"][i]["suite_name"], "pass": [], "fail": [],
                       "blocked": [], "long_execution": 0}

            for test in self.result_json_obj["test_suites"][i]["results"]:
                if test["time"] != "" and float(test["time"]) > 10.0:
                    summary["long_execution"] = summary["long_execution"] + 1

                if test["status"]  == "pass":
                    insert_test_in_list_by_ascending_order_of_test_name(summary["pass"], test)
                    continue

                if test["status"] == "fail":
                    insert_test_in_list_by_ascending_order_of_test_name(summary["fail"], test)
                    continue

                if test["status"] == "blocked":
                    insert_test_in_list_by_ascending_order_of_test_name(summary["blocked"], test)

            self.test_suite_summary.append(summary)

    def get_test_suite_summary(self, index: int):
        assert index < self.number_of_test_suites
        return self.test_suite_summary[index]
