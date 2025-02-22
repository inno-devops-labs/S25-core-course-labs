import unittest
from web_app import app
from datetime import datetime
import pytz


class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        """Set up a test client for Flask app."""
        self.app = app.test_client()
        self.app.testing = True

    def test_homepage_response(self):
        """Test if the homepage returns a 200 status code."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_moscow_time_format(self):
        """Test if the Moscow time returned is in correct format."""
        response = self.app.get('/')
        self.assertIn("Time in Moscow", response.data.decode())

        moscow_tz = pytz.timezone('Europe/Moscow')
        current_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
        # Check date match
        self.assertIn(current_time[:10], response.data.decode())


if __name__ == "__main__":
    unittest.main()
