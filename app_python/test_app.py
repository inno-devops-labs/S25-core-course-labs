import unittest
from app import app
import pytz
from datetime import datetime
import re

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        # Initialize test client for Flask application
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        """Test checks if home page is accessible"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_time_format(self):
        """Test verifies correct time format"""
        response = self.app.get('/')
        html = response.data.decode()
        # Look for time in HH:MM:SS format
        time_pattern = r'\d{2}:\d{2}:\d{2}'
        self.assertTrue(re.search(time_pattern, html))

    def test_date_format(self):
        """Test verifies correct date format"""
        response = self.app.get('/')
        html = response.data.decode()
        # Look for date in DD.MM.YYYY format
        date_pattern = r'\d{2}\.\d{2}\.\d{4}'
        self.assertTrue(re.search(date_pattern, html))

    def test_moscow_timezone(self):
        """Test verifies Moscow timezone is used"""
        moscow_tz = pytz.timezone('Europe/Moscow')
        current_moscow = datetime.now(moscow_tz)
        response = self.app.get('/')
        html = response.data.decode()
        # Check if hour matches (with tolerance for hour changes)
        hour = current_moscow.strftime('%H')
        self.assertTrue(hour in html or
                       str((int(hour) + 1) % 24).zfill(2) in html or
                       str((int(hour) - 1) % 24).zfill(2) in html)
        
if __name__ == '__main__':
    unittest.main()