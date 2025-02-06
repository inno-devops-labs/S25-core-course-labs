import unittest
from datetime import datetime
import pytz
from app import app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        """Set up test client before each test."""
        self.app = app.test_client()
        self.app.testing = True

    def test_index_route(self):
        """Test the main route returns 200 and contains time."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'time-display', response.data)
        self.assertRegex(response.data.decode(), r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')

    def test_moscow_time_format(self):
        """Test Moscow time formatting."""
        moscow_tz = pytz.timezone('Europe/Moscow')
        current_time = datetime.now(moscow_tz)
        formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
        self.assertRegex(formatted_time, r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')

if __name__ == '__main__':
    unittest.main() 