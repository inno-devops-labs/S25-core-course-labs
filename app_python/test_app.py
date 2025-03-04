import unittest
from app import app

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_show_time(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Current Time in Moscow', response.data)

    def test_show_time_format(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        # Check if the response contains the correct date format
        self.assertRegex(response.data.decode('utf-8'), r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')

    def test_invalid_route(self):
        response = self.app.get('/invalid')
        self.assertEqual(response.status_code, 404)

    def test_content_type(self):
        response = self.app.get('/')
        self.assertEqual(response.content_type, 'text/html; charset=utf-8')

if __name__ == '__main__':
    unittest.main()