from typing import List
import unittest
from zoneinfo import ZoneInfo

from webtest import TestApp
from datetime import datetime, timezone

from app import TimeService, TemplateService, create_app
from app_start import ZonedTimeService


class MockTimeService(TimeService):
    def __init__(self, values: List[int]):
        self.values = list(map(lambda x: datetime.fromtimestamp(x), values))
        self.index = len(values) - 1

        if len(values) <= 0:
            raise Exception('Illegal values are provided: required at least one value')

    def current_time(self) -> datetime:
        self.index += 1
        if self.index >= len(self.values):
            self.index = 0

        return self.values[self.index]


class MockTemplateService(TemplateService):
    def fill_current_time_template(self, current_time: datetime) -> str:
        return f'{int(current_time.timestamp())}'


class TestController(unittest.TestCase):
    def setUp(self):
        self.time_values = [i * 1000000 for i in range(1, 4)]
        self.app = TestApp(create_app(MockTimeService(self.time_values), MockTemplateService()))

    def test_index(self):
        for value in self.time_values + self.time_values:
            text = self.app.get('/').text
            assert str(value) == text, f'Expected {value}, got {text}'


class TestZonedTimeService(unittest.TestCase):
    def setUp(self):
        zone = 'Europe/Moscow'
        self.zone = ZoneInfo(zone)
        self.service = ZonedTimeService(zone)

    def test_current_time(self):
        start = datetime.now(self.zone)
        time = self.service.current_time()
        end = datetime.now(self.zone)

        assert start <= time, f'Expected {start} <= {time}'
        assert time <= end, f'Expected {time} <= {end}'
        assert time.tzinfo == self.zone


if __name__ == '__main__':
    unittest.main()
