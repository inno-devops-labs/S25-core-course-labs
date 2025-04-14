import datetime
import unittest

import pytz

from app_python.app import app


class AppTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_moscow_time_calc(self):
        expected_msc_time = (datetime.datetime
                             .now(pytz.timezone("Europe/Moscow")))
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

        displayed_time = (response
                          .data
                          .decode('utf-8')
                          .split("Moscow Time: ")[1]
                          .split("</h1>")[0]
                          .strip()
                          )
        self.assertEqual(displayed_time,
                         expected_msc_time.strftime("%Y-%m-%d %H:%M:%S"))

    def test_home_page_rendering(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Moscow Time:', response.data)


if __name__ == '__main__':
    unittest.main()
