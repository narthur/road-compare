import unittest
from tests.test_case import TestCase
from road_compare.main import Main
import datetime


class TestMain(TestCase):
    _base_timestamp = int(datetime.datetime.strptime('2019-1-1', '%Y-%m-%d').timestamp())

    _main: Main

    def setUp(self) -> None:
        super().setUp()

        self._main = self._factory.make(Main)

    def _assert_goals_passed(self, should_pass=True):
        expected = 'PASSED' if should_pass else 'FAILED'

        self._mock_python.print.assert_any_call('', expected)

    def _load_request_json_responses(self, before, after):
        self._mock_requests.get_json.side_effect = [before, after]

    def test_uses_mock_requests(self):
        self._main.run('first', 'second')

        self._mock_requests.get_json.assert_any_call('first')

    def test_prints_result(self):
        self._main.run('first', 'second')

        self._assert_goals_passed()

    def test_calculates_success(self):
        self._load_request_json_responses(
            {
                'fullroad': [
                    [self._base_timestamp, 1, 1]
                ]
            },
            {
                'fullroad': [
                    [self._base_timestamp, 2, 2]
                ]
            }
        )

        self._main.run('', '')

        self._assert_goals_passed()

    def test_calculates_failure(self):
        self._load_request_json_responses(
            {
                'fullroad': [
                    [self._base_timestamp, 2, 2]
                ]
            },
            {
                'fullroad': [
                    [self._base_timestamp, 1, 1]
                ]
            }
        )

        self._main.run('', '')

        self._assert_goals_passed(False)


if __name__ == '__main__':
    unittest.main()
