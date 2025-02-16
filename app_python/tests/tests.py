import unittest
from app import app
from datetime import datetime, timedelta
import pytz


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_status_code(self):
        result = self.app.get("/")
        self.assertEqual(result.status_code, 200)

    def test_accuracy(self):
        result = self.app.get("/")
        self.assertEqual(result.status_code, 200)

        # Extract the time from the response
        webapp_time_str = (
            result.data.decode("utf-8")
            .split("Time in Moscow - ")[1]
            .split("<")[0]
            .strip()
        )
        webapp_time = datetime.strptime(webapp_time_str, "%H:%M:%S")

        # Get the current time in Moscow
        tz_moscow = pytz.timezone("Europe/Moscow")
        current_time = datetime.now(tz_moscow)

        # Allow for a 10-second inaccuracy
        inaccuracy = timedelta(seconds=10)

        # Check if the webapp time is within the allowed inaccuracy
        self.assertTrue(
            (current_time - inaccuracy).time()
            <= webapp_time.time()
            <= (current_time + inaccuracy).time()
        )


if __name__ == "__main__":
    unittest.main()
