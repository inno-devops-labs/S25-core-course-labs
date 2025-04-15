import unittest

from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page_status_code(self):
        """Test if the home page returns HTTP 200"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_time_format(self):
        """Test if the response contains a valid time format HH:MM:SS"""
        response = self.app.get('/')
        pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'
        self.assertRegex(response.data.decode('utf-8'), pattern)

    def test_response_contains_moscow_time(self):
        """Ensure 'Current Time in Moscow' appears in the response"""
        response = self.app.get('/')
        self.assertIn("Current Time in Moscow", response.data.decode('utf-8'))

    def test_invalid_route(self):
        """Test if accessing a non-existent route returns a 404 error"""
        response = self.app.get('/invalid')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
