import unittest
from app import app
from datetime import datetime
import pytz


class TestApp(unittest.TestCase):

    def setUp(self):
        """Set up test client before running tests."""
        self.app = app.test_client()
        self.app.testing = True

    def test_current_time_format(self):
        """Test if the current time is returned in the correct format."""
        tz_moscow = pytz.timezone("Europe/Moscow")
        expected_format = "%Y-%m-%d %H:%M:%S"
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(datetime.now(tz_moscow).strftime(expected_format)[:16], response.get_data(as_text=True))

    def test_homepage_content(self):
        """Check if the homepage contains the correct heading."""
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("<h1>Current Time in Moscow</h1>", response.get_data(as_text=True))


if __name__ == "__main__":
    unittest.main()
