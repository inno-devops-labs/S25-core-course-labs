import unittest
from app import app, get_moscow_time
from datetime import datetime
import pytz


class FlaskTestCase(unittest.TestCase):
    """Tests for the Flask application"""

    def setUp(self):
        """Set up test client"""
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        """Test if the home page loads successfully"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Current Time in Moscow', response.data)

    def test_moscow_time_format(self):
        """Test if the Moscow time format is correct"""
        moscow_time = get_moscow_time()
        # Check if the time format is 'YYYY-MM-DD HH:MM:SS'
        try:
            datetime.strptime(moscow_time, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            self.fail("Incorrect time format")

    def test_moscow_time_timezone(self):
        """Test if Moscow time is correctly fetched in the Moscow timezone"""
        moscow_tz = pytz.timezone('Europe/Moscow')
        current_time = datetime.now(moscow_tz)
        moscow_time = get_moscow_time()
        # Test if the time returned matches Moscow time
        self.assertTrue(
            current_time.strftime('%Y-%m-%d %H:%M:%S') == moscow_time[:19]
            )


if __name__ == '__main__':
    unittest.main()
