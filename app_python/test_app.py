import re
import unittest
from app import app


class TestMoscowTime(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_text(self):
        response = self.client.get('/')
        self.assertIn('The current time in Moscow:', response.data.decode())

    def test_time(self):
        response = self.client.get('/')
        match = re.search(r"\d{2}:\d{2}:\d{2}", response.data.decode())
        self.assertIsNotNone(match, "No valid HH:MM:SS time found")

    def test_tags(self):
        response = self.client.get('/')
        html_text = response.data.decode()
        self.assertIn('<h2>', html_text)
        self.assertIn('</h2>', html_text)
        self.assertIn('<h1>', html_text)
        self.assertIn('</h1>', html_text)


if __name__ == '__main__':
    unittest.main()
