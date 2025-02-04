import unittest
from datetime import datetime
import pytz
from app_python.main import app


class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_index_route(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Current Time in Moscow", response.data)

    def test_moscow_time_correctness(self):
        moscow_time_zone = pytz.timezone("Europe/Moscow")
        expected_time = (datetime.now(moscow_time_zone)
                         .strftime("%Y-%m-%d %H:%M:%S"))
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

        actual_time = (response.data
                       .decode('utf-8')
                       .split("<p>")[1]
                       .split("</p>")[0]
                       .strip())
        self.assertEqual(actual_time, expected_time)
