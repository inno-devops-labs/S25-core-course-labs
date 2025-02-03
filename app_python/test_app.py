import unittest

from app import app, get_moscow_time


class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_moscow_time(self):
        time_str = get_moscow_time()
        self.assertRegex(time_str, r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Current time in Moscow:', response.data)

    def test_404_page(self):
        response = self.app.get('/nonexistent')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'404 - Page Not Found', response.data)


if __name__ == '__main__':
    unittest.main()
