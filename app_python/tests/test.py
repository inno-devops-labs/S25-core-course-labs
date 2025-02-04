import unittest
import pytz
import time

from app_python.app import app, get_current_time, TIMEZONE, set_new_timezone
from datetime import datetime


STATUS_OK = 200
STATUS_FAILED = 400
INVALID_TIMEZONE = "Unexists/notcity"


class Testing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    def test_valid_get_cur_t(self):
        # testing function that returns cur time with valid TZ
        timezone = TIMEZONE
        res = get_current_time(timezone)

        self.assertIsNotNone(res)
        print("Testing timezone: ", res)

        valid_timezone = pytz.timezone("Europe/Moscow")
        valid = datetime.now(valid_timezone).strftime("%H:%M")

        self.assertIn(valid, res.strftime("%H:%M"))

    def test_invalid_get_cur_t(self):
        # the same but for invalid case
        timezone = INVALID_TIMEZONE
        res = get_current_time(timezone)
        self.assertIsNone(res)

    def test_home_page(self):
        # check accessibility of the home page (default case)
        res = self.client.get('/')
        self.assertEqual(res.status_code, STATUS_OK)

    def test_time_changing(self):
        # time should be updated after each reloading
        res1 = self.client.get('/')
        time.sleep(1.1)
        res2 = self.client.get('/')

        self.assertEqual(res1.status_code, STATUS_OK)
        self.assertEqual(res2.status_code, STATUS_OK)

        self.assertNotEqual(res1.text, res2.text)

    def test_invalid_home_page(self):
        # the same but with invalid timezone
        set_new_timezone(INVALID_TIMEZONE)
        print("New set timezone for an invalid case:", INVALID_TIMEZONE)

        response = self.client.get('/')
        self.assertEqual(response.status_code, STATUS_FAILED)
        self.assertIn('timezone', response.text)

        set_new_timezone(TIMEZONE)


if __name__ == '__main__':
    unittest.main()
