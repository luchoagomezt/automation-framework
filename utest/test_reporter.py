import json

import pytest
from reporter import insert_test_in_list_by_ascending_order_of_test_name


@pytest.fixture()
def reporter():
    from reporter import Reporter
    json_string = '{"test_suites":[' \
                  '{"suite_name":"hvac_mode",' \
                  '"results": [' \
                  '{"test_name": "test_eco_2621","time": "8.556","status": "pass"}, ' \
                  '{"test_name": "test_eco_1725","time": "45.909","status": "pass"}, ' \
                  '{"test_name": "test_eco_2645","time": "9.383","status": "fail"}, ' \
                  '{"test_name": "test_eco_2623","time": "6.719","status": "pass"}, ' \
                  '{"test_name": "test_eco_2624","time": "","status": "blocked"}, ' \
                  '{"test_name": "test_eco_2625","time": "8.017","status": "pass"}, ' \
                  '{"test_name": "test_eco_2626","time": "8.774","status": "pass"}, ' \
                  '{"test_name": "test_eco_2641","time": "","status": "blocked"}, ' \
                  '{"test_name": "test_eco_2622","time": "4.967","status": "pass"},' \
                  '{"test_name": "test_eco_2782","time": "12.690","status": "fail"}, ' \
                  '{"test_name": "test_eco_2633","time": "70.902","status": "fail"}]}, ' \
                  '{"suite_name":"temp_setting",' \
                  '"results": [' \
                  '{"test_name": "test_eco_2915","time": "5.890","status": "fail"}, ' \
                  '{"test_name": "test_eco_2913","time": "10.000","status": "fail"}]}' \
                  ']}'

    return Reporter(json.loads(json_string))


def test_get_test_suite_name_from_summary(reporter):
    assert reporter.get_test_suite_summary(0)["suite_name"] == "hvac_mode"
    assert reporter.get_test_suite_summary(1)["suite_name"] == "temp_setting"


def test_get_pass_test_cases_from_summary(reporter):
    assert len(reporter.get_test_suite_summary(0)["pass"]) == 6
    assert len(reporter.get_test_suite_summary(1)["pass"]) == 0


def test_get_fail_test_cases_from_summary(reporter):
    assert len(reporter.get_test_suite_summary(0)["fail"]) == 3
    assert len(reporter.get_test_suite_summary(1)["fail"]) == 2


def test_get_blocked_test_cases_from_summary(reporter):
    assert len(reporter.get_test_suite_summary(0)["blocked"]) == 2
    assert len(reporter.get_test_suite_summary(1)["blocked"]) == 0


def test_get_long_execution_test_cases_from_summary(reporter):
    assert reporter.get_test_suite_summary(0)["long_execution"] == 3
    assert reporter.get_test_suite_summary(1)["long_execution"] == 0


def test_insert_test_in_list_by_ascending_order_of_test_name():
    list_of_tests = []
    test = {"test_name": "test_eco_2621"}
    insert_test_in_list_by_ascending_order_of_test_name(list_of_tests, test)
    assert list_of_tests == [{"test_name": "test_eco_2621"}]

    test = {"test_name": "test_eco_1725"}
    insert_test_in_list_by_ascending_order_of_test_name(list_of_tests, test)
    assert list_of_tests == [{"test_name": "test_eco_1725"}, {"test_name": "test_eco_2621"}]

    test = {"test_name": "test_eco_1730"}
    insert_test_in_list_by_ascending_order_of_test_name(list_of_tests, test)
    assert list_of_tests == [{"test_name": "test_eco_1725"}, {"test_name": "test_eco_1730"},
                             {"test_name": "test_eco_2621"}]

    test = {"test_name": "test_eco_2622"}
    insert_test_in_list_by_ascending_order_of_test_name(list_of_tests, test)
    assert list_of_tests == [{"test_name": "test_eco_1725"}, {"test_name": "test_eco_1730"},
                             {"test_name": "test_eco_2621"}, {"test_name": "test_eco_2622"}]


def test_print(reporter):
    print(reporter)
