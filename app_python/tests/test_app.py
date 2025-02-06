import unittest
from app import app
from unittest.mock import patch
from datetime import datetime

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        """Set up the Flask test client."""
        self.client = app.test_client()
        self.client.testing = True

    @patch("app.datetime")
    def test_moscow_time_response(self, mock_datetime):
        """Test if the API returns Moscow time in the correct format."""
        fake_time = datetime(2025, 2, 3, 12, 30, 0)  # Fixed test time
        mock_datetime.now.return_value = fake_time
        mock_datetime.strftime.return_value = fake_time.strftime('%Y-%m-%d %H:%M:%S')

        response = self.client.get("/")
        response_data = response.data.decode()
        self.assertEqual(response.status_code, 200)
        self.assertIn("Current Time in Moscow", response_data)
        self.assertRegex(response_data, r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}")

    def test_invalid_route(self):
        """Test that an invalid route returns a 404 error."""
        response = self.client.get("/invalid")
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
