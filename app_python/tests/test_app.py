import unittest
from app import app
from datetime import datetime
import pytz


class TestMoscowTimeApp(unittest.TestCase):
    # Create a test client for the Flask app
    def setUp(self):
        self.app = app.test_client()

    # Check whether base endpoint is available
    def test_moscow_time_endpoint_status_code(self):
        """Test that the / endpoint returns a 200 status code."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    # Check whether application returns a string with Moscow time
    def test_moscow_time_response_content(self):
        """Test that the response contains the expected
        'Current time in Moscow' string."""
        response = self.app.get('/')
        self.assertIn(b'Current time in Moscow', response.data)

    # Check whether application returns a Moscow time in supposed format
    def test_moscow_time_format(self):
        """Test that the response includes the time in the correct
        format (DD-MM-YYYY HH:MM:SS)."""
        response = self.app.get('/')
        response_text = response.data.decode('utf-8')

        # Extract the time part from the response
        time_str = response_text.split(': ')[1]

        # Define the expected date-time format
        expected_format = '%d-%m-%Y %H:%M:%S'

        # Attempt to parse the time string using the expected format
        try:
            datetime.strptime(time_str, expected_format)
        except ValueError:
            self.fail(f"Time string '{time_str}' does not match the expected" +
                      f"format '{expected_format}'")

    # Check whether application returns a correct Moscow time
    def test_moscow_time_accuracy(self):
        """Test that the time displayed matches the current Moscow time."""
        response = self.app.get('/')
        response_text = response.data.decode('utf-8')

        # Extract the time part from the response
        time_str = response_text.split(': ')[1]

        # Parse the time string into the naive datetime object
        moscow_time_in_response_naive = datetime.strptime(
            time_str, '%d-%m-%Y %H:%M:%S')

        # Attach the Moscow timezone to the naive datetime object
        moscow_tz = pytz.timezone('Europe/Moscow')
        moscow_time_in_response = moscow_tz.localize(
            moscow_time_in_response_naive)

        # Get the current Moscow time
        current_moscow_time = datetime.now(moscow_tz)

        # Allow a small inaccuracy due to computation and comparison overhead
        allowed_margin = 5

        # Compare the times
        time_difference = abs((current_moscow_time -
                               moscow_time_in_response).total_seconds())
        self.assertLessEqual(time_difference, allowed_margin,
                             f"Displayed time '{moscow_time_in_response}'" +
                             "does not match current Moscow time" +
                             f"'{current_moscow_time}'")


if __name__ == '__main__':
    unittest.main()
