import unittest
from app import app
from datetime import datetime
import pytz
from bs4 import BeautifulSoup


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_status_code(self):
        """Test that the index page returns 200 status code"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_content(self):
        """Test that the index page contains time and date elements"""
        response = self.app.get('/')
        soup = BeautifulSoup(response.data, 'html.parser')

        self.assertIsNotNone(soup.find('div', class_='time'))
        self.assertIsNotNone(soup.find('div', class_='date'))

    def test_moscow_timezone(self):
        """Test that the time is correctly set to Moscow timezone"""
        moscow_tz = pytz.timezone('Europe/Moscow')
        current_time = datetime.now(moscow_tz)

        response = self.app.get('/')
        soup = BeautifulSoup(response.data, 'html.parser')

        displayed_time = soup.find('div', class_='time').text.strip()
        displayed_date = soup.find('div', class_='date').text.strip()

        self.assertRegex(displayed_time, r'^\d{2}:\d{2}:\d{2}$')

        displayed_hours = int(displayed_time.split(':')[0])
        displayed_minutes = int(displayed_time.split(':')[1])

        current_hours = current_time.hour
        current_minutes = current_time.minute

        self.assertEqual(displayed_hours, current_hours)
        self.assertEqual(displayed_minutes, current_minutes)

        expected_date = current_time.strftime('%B %d, %Y')
        self.assertEqual(displayed_date, expected_date)


if __name__ == '__main__':
    unittest.main()
