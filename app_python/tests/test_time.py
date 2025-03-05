import unittest
from unittest.mock import patch
from datetime import datetime
from app import app


class TestCurrentTimeRoute(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_current_time_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_current_time(self):
        # Mock the current time to a known value
        mock_time = datetime(2023, 10, 1, 12, 0, 0)
        expected_time = (mock_time).strftime('%H:%M')

        # Patch the datetime.now method to return the mock time
        with unittest.mock.patch('datetime.datetime') as mock_datetime:
            mock_datetime.now.return_value = mock_time
            response = self.app.get('/')
            self.assertIn(expected_time.encode(), response.data)


if __name__ == '__main__':
    unittest.main()
