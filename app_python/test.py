"""
This file contains the unit tests for the app_service.py file.
"""
import unittest
from unittest.mock import MagicMock

from app_python.app_service import get_time, get_tz_time


class TestAppService(unittest.TestCase):
    """
    Test cases for the app_service.py file.
    """

    def test_get_tz_time(self):
        """
        Tests the get_tz_time function.
        It checks for different timezones and compares the results.
        """
        # Istanbul and Moscow time will be same if get_tz_time is working correctly
        self.assertEqual(get_tz_time("Europe/Istanbul"), get_tz_time("Europe/Moscow"))
        # Tokyo and Moscow time will be different for the same reason
        self.assertNotEqual(get_tz_time("Asia/Tokyo"), get_tz_time("Europe/Moscow"))

    def test_get_time(self):
        """
        Tests the get_time function.
        It checks if the current Moscow time is in the current time string.
        """
        dummy_req = MagicMock()
        response = get_time(dummy_req, "Europe/Moscow")
        # response_body = response.body.decode() if hasattr(response, "body")
        #  and response.body else ""
        self.assertIn(get_tz_time("Europe/Moscow"), response.body.decode())


if __name__ == "__main__":
    unittest.main()
