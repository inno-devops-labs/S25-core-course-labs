import unittest
from app_python.app import app
import re


class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_homepage(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Current time in Moscow:", response.data)

    def test_time_format(self):
        response = self.client.get("/")
        response_text = response.data.decode("utf-8")
        pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"

        match = re.search(pattern, response_text)
        self.assertIsNotNone(match, "Invalid output format")


if __name__ == "__main__":
    unittest.main()
