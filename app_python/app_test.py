from typing import List
import unittest
from zoneinfo import ZoneInfo

from bs4 import BeautifulSoup
from webtest import TestApp
from datetime import datetime

from app import TimeService, TemplateService, StatsService, create_app
from app_start import ZonedTimeService, HtmlTemplateService, FileStatsService


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


class MockStatsService(StatsService):
    def __init__(self):
        self.visits = 0

    def get_visits(self) -> int:
        return self.visits
    
    def increment_visits(self):
        self.visits += 1


class TestController(unittest.TestCase):
    def setUp(self):
        self.time_values = [i * 1000000 for i in range(1, 4)]
        self.app = TestApp(create_app(MockTimeService(self.time_values), MockTemplateService(), MockStatsService()))

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


class TestAppConfiguration(unittest.TestCase):
    def setUp(self):
        zone = 'Europe/Moscow'
        self.zone = ZoneInfo(zone)
        self.app = TestApp(create_app(ZonedTimeService(zone), HtmlTemplateService(), FileStatsService()))

    def test_app(self):
        start = datetime.now(self.zone)
        response = self.app.get('/')
        end = datetime.now(self.zone)

        bs = BeautifulSoup(response.text, 'html.parser')

        time_str = bs.find('a', {'id': 'current-time'})
        time = datetime.fromisoformat(time_str.text)

        assert start <= time, f'Expected {start} <= {time}'
        assert time <= end, f'Expected {time} <= {end}'


if __name__ == '__main__':
    unittest.main()
