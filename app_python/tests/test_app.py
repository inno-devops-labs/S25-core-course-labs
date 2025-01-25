from app_python.app import app
from datetime import datetime
import pytz
import unittest


class TimeAppTests(unittest.TestCase):
    """
    Collection of primary applications tests
    """

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_time_display(self):
        """
        Checks if home page is accessible and shows current time in Moscow
        """

        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

        moscow_tz = pytz.timezone("Europe/Moscow")
        expected_time = datetime.now(moscow_tz).strftime("%H:%M:%S")
        self.assertIn(expected_time, response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
