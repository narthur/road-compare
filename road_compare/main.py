from pyminder.goal import Goal
from natlibpy.factory import Factory
import datetime
import json
from road_compare.requests import Requests
from road_compare.python import Python


class Main:
    _factory: Factory
    _python: Python
    _requests: Requests

    def __init__(self, factory: Factory, python: Python, requests_: Requests):
        self._factory = factory
        self._python = python
        self._requests = requests_

    def run(self, before_address, after_address):
        before_goal: Goal = self._build_goal(before_address)
        after_goal: Goal = self._build_goal(after_address)

        results = self._calculate_results(before_goal, after_goal)

        self._print_ranges(results)
        self._print_result(results)

    @staticmethod
    def _calculate_results(before_goal, after_goal):
        start = int(datetime.datetime.strptime('2019-1-1', '%Y-%m-%d').timestamp())
        end = int(datetime.datetime.strptime('2019-12-31', '%Y-%m-%d').timestamp())
        day = 24 * 60 * 60
        times = list(range(start, end + 1, day))

        return [(t, after_goal.get_road_val(t) >= before_goal.get_road_val(t)) for t in times]

    def _build_goal(self, data_location) -> Goal:
        data = self._get_goal_data(data_location)

        return self._factory.make(Goal, data=data)

    def _get_goal_data(self, location):
        try:
            with open(location) as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            return self._requests.get_json(location)

    def _print_ranges(self, results):
        for range_ in self._build_ranges(results):
            self._print_range(range_)

    def _build_ranges(self, results: list, range_=None, ranges=None):
        results = results if range_ else results.copy()
        ranges = ranges if ranges else []

        if not results:
            if range_:
                ranges.append(range_)

            return ranges

        result = results.pop(0)
        range_ = range_ if range_ else [result[0], result[0], result[1]]

        if result[1] == range_[2]:
            range_[1] = result[0]
        else:
            ranges.append(range_)
            range_ = [result[0], result[0], result[1]]

        return self._build_ranges(results, range_, ranges)

    @staticmethod
    def _print_range(range_):
        start_string = datetime.datetime.fromtimestamp(range_[0]).strftime('%Y-%m-%d')
        end_string = datetime.datetime.fromtimestamp(range_[1]).strftime('%Y-%m-%d')
        range_string = start_string if start_string == end_string else f'{start_string} – {end_string}'

        print(f'{range_string}: {range_[2]}')

    def _print_result(self, day_results):
        bools = [r[1] for r in day_results]
        passed = False not in bools

        print()

        self._python.print('', 'PASSED' if passed else 'FAILED')
