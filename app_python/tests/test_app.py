import unittest
from unittest.mock import patch
import datetime as dt
import pytz

from app import app, get_moscow_time, Config

class TestMoscowTimeFunctions(unittest.TestCase):
    def setUp(self):
        # Enable testing mode and create a test client for our Flask app.
        app.testing = True
        self.client = app.test_client()

    def test_get_moscow_time_valid(self):
        """
        Test that get_moscow_time returns the correctly formatted date and time
        when the timezone configuration is valid.
        """
        # Arrange: Create a fixed UTC datetime.
        fixed_utc = dt.datetime(2025, 2, 4, 12, 0, 0, tzinfo=pytz.utc)

        # Create a subclass of datetime that overrides now
        class FixedDatetime(dt.datetime):
            @classmethod
            def now(cls, tz=None):
                return fixed_utc

        # Patch the datetime class in the app module with our FixedDatetime
        with patch("app.datetime", FixedDatetime):
            # Act: Call the function.
            date_str, time_str = get_moscow_time()

            # Compute the expected Moscow time.
            moscow_tz = pytz.timezone(Config.TIMEZONE)
            expected_moscow = fixed_utc.astimezone(moscow_tz)
            expected_full = expected_moscow.strftime(Config.DATE_FORMAT)
            expected_date, expected_time = expected_full.split(" ", 1)

            # Assert: Verify the returned strings match the expected values.
            self.assertEqual(date_str, expected_date)
            self.assertEqual(time_str, expected_time)

    def test_get_moscow_time_invalid_timezone(self):
        """
        Test that get_moscow_time raises UnknownTimeZoneError if the timezone
        configuration is invalid.
        """
        # Temporarily change the timezone configuration.
        original_timezone = Config.TIMEZONE
        Config.TIMEZONE = "Invalid/Timezone"
        try:
            with self.assertRaises(pytz.exceptions.UnknownTimeZoneError):
                get_moscow_time()
        finally:
            # Restore the original configuration.
            Config.TIMEZONE = original_timezone

    @patch("app.render_template")
    @patch("app.get_moscow_time")
    def test_display_time_success(self, mock_get_moscow_time, mock_render_template):
        """
        Test that the main route ("/") returns a 200 response and calls the
        correct template when get_moscow_time succeeds.
        """
        # Arrange:
        # Simulate a valid return value from get_moscow_time.
        mock_get_moscow_time.return_value = ("2025-02-04", "15:00:00")
        # Simulate render_template simply returning a rendered string.
        mock_render_template.return_value = "Rendered index"

        # Act: Perform a GET request to the "/" route.
        response = self.client.get("/")

        # Assert:
        # Verify that render_template was called with the correct arguments.
        mock_render_template.assert_called_with(
            "index.html",
            time="15:00:00",
            date="2025-02-04",
            refresh=Config.REFRESH_INTERVAL
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Rendered index")


if __name__ == "__main__":
    unittest.main()

