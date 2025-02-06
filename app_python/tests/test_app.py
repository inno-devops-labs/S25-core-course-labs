import unittest
from app import app


class TestAppRoutes(unittest.TestCase):
    def setUp(self):
        """Set up the Flask test client."""
        self.app = app.test_client()

    def test_get_time_route(self):
        """Test the '/' route to ensure it returns the correct response."""
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Current Time in Moscow", response.data)

    def test_get_time_with_invalid_timezone(self):
        """Test error handling when an invalid timezone is configured."""
        # Temporarily override the TIMEZONE_NAME in the config
        from config import config
        try:
            app.config["TIMEZONE_NAME"] = "Invalid/Timezone"
            response = self.app.get("/")
            self.assertEqual(response.status_code, 400)
            self.assertIn(b"Error: Invalid timezone", response.data)
        finally:
            # Restore the original timezone
            app.config.from_mapping(config)


if __name__ == "__main__":
    unittest.main()
