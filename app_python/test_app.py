from datetime import datetime
import unittest

from pytz import timezone
from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_time_page(self):
        response = self.app.get('/')
        moscow_time = datetime.now(timezone('Europe/Moscow')).strftime('%Y-%m-%d %H:%M:%S')
        self.assertEqual(response.status_code, 200)
        self.assertIn(f'Current time in Moscow: {moscow_time}', response.data.decode())


if __name__ == '__main__':
    unittest.main()
