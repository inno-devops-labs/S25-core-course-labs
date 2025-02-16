"""
Unit tests for testing web application
"""

import unittest
from datetime import datetime, timezone, timedelta

from ..app.app import web_app


class TestApp(unittest.TestCase):
    """
    Class that represents unit tests for web application
    """

    def setUp(self):
        """
        Set up of web application
        """
        test_app = web_app
        self.app = test_app.test_client()

    def test_time_endpoint(self):
        """
        Check for the correctness of status code
        """
        response = self.app.get("/")

        self.assertEqual(response.status_code, 200)

    def test_content(self):
        """
        Checks web page content
        """
        response = self.app.get("/")

        self.assertIn("Current Time in Moscow:", response.text)

    def test_time(self):
        """
        Test time for correctness
        """
        response = self.app.get("/")

        utc_now = datetime.now(timezone.utc)
        moscow_tz = timezone(timedelta(hours=3))
        moscow_time = utc_now.astimezone(moscow_tz)

        time_to_check = str(moscow_time).split(".", maxsplit=1)[0]
        self.assertIn(time_to_check, response.text)


if __name__ == "__main__":
    unittest.main()
