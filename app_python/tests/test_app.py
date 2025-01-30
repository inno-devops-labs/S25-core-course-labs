import unittest
from unittest.mock import patch
from datetime import datetime
from fastapi.testclient import TestClient

from app.main import app

class TestMoscowTimeAPI(unittest.TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app)
        
    def test_root_route(self) -> None:
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Current Moscow Time", response.text)
        self.assertIn('id="time-display"', response.text)
        self.assertIn('id="copy-btn"', response.text)

    @patch("app.main.datetime")
    def test_api_endpoint(self, mock_datetime) -> None:
        fixed_time = datetime(2024, 1, 15, 12, 0)
        mock_datetime.now.return_value = fixed_time

        response = self.client.get("/api/moscow_time")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "time": "2024-01-15 12:00:00",
            "timestamp": fixed_time.timestamp()
        })

    @patch("app.main.datetime")
    def test_api_endpoint_with_pytz_mock(self, mock_datetime) -> None:
        from pytz import timezone as tz
        moscow_tz = tz('Europe/Moscow')
        mock_time = moscow_tz.localize(datetime(2024, 1, 15, 15, 0))
        mock_datetime.now.return_value = mock_time

        response = self.client.get("/api/moscow_time")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["time"], "2024-01-15 15:00:00")

if __name__ == '__main__':
    unittest.main()
