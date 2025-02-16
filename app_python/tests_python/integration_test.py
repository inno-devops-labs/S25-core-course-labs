import unittest
from app_python.app import app


class TestIntegration(unittest.TestCase):
    """Integration tests using Flask test client."""

    def setUp(self):
        """Set up the test client before each test."""
        self.client = app.test_client()

    def test_server_response(self):
        """Test if the server is running and returns a valid response."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Current Time in Moscow", response.get_data(as_text=True))


if __name__ == "__main__":
    unittest.main()
