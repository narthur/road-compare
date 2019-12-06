import unittest
from unittest.mock import MagicMock
from natlibpy.factory import Factory
from road_compare.python import Python
from road_compare.requests import Requests


class TestCase(unittest.TestCase):
    _factory = None

    _mock_python = None
    _mock_requests = None

    def setUp(self) -> None:
        super().setUp()

        self._factory = Factory()

        self._mock_python = self.__mock(Python)
        self._mock_requests = self.__mock(Requests)

    def __mock(self, class_):
        mock = MagicMock(spec_set=class_)

        self._factory.inject(mock)

        return mock
