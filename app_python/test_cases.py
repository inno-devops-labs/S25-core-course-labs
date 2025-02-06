import unittest
import app
import re


class UnitTests(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_valid_time(self):
        page = self.app.get('/')
        self.assertEqual(page.status_code, 200)

        # Extract the time from response data
        match = re.search(rb'(\d{2}:\d{2}:\d{2})', page.data)
        self.assertIsNotNone(match, "Time format not found in response")

    def test_page(self):
        page = self.app.get('/')
        self.assertEqual(page.status_code, 200)
        self.assertIn(b'Current time in Moscow, Russia:', page.data)


if __name__ == '__main__':
    unittest.main()
