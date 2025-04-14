from app_python.app import app
from datetime import datetime
from time import sleep
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
        Checks if home page (/) is accessible and
        shows current time in Moscow in format hh:mm:ss dd.mm.yyyy
        """

        self.check_web_page()

    def test_continuous_time_display(self):
        """
        Checks whether the homepage is accessible for 5 seconds and
        whether the current time in Moscow is displayed
        correctly every second in format hh:mm:ss dd.mm.yyyy.
        """

        for i in range(0, 5):
            self.check_web_page()
            sleep(1)

    def check_web_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

        moscow_tz = pytz.timezone("Europe/Moscow")
        expected_time = datetime.now(moscow_tz).strftime("%H:%M:%S %d.%m.%Y")

        self.assertEqual(
            f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Moscow Time</title>
</head>
<body>
    <h1>Current Time in Moscow:</h1>
    <h3>{expected_time}</h3>
    <p>Refresh page to update the time</p>
</body>
</html>'''.strip(),
            response.data.decode('utf-8').strip()
        )


if __name__ == '__main__':
    unittest.main()
