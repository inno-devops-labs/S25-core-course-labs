import requests
import unittest


class TestIntegration(unittest.TestCase):
    def test_server_response(self):
        """Test if the server is running and returns a valid response."""
        response = requests.get("http://127.0.0.1:5000/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Current Time in Moscow", response.text)


if __name__ == "__main__":
    unittest.main()
