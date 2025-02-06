import unittest
from unittest import mock
from main import app
from bs4 import BeautifulSoup

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_get_time_success(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'time', response.data)

    def test_internal_server_error(self):
        with mock.patch('main.datetime') as mock_datetime:
            mock_datetime.now.side_effect = Exception("Some error")
            response = self.client.get('/')
            self.assertEqual(response.status_code, 500)
            self.assertIn(b"Internal server error", response.data)

    def test_template_rendering(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        soup = BeautifulSoup(response.data, 'html.parser')
        time_element = soup.find(id='current-time')  # <p id="current-time">{{ time }}</p>
        self.assertIsNotNone(time_element, "Element with id='current-time' does not exist")

        import re
        time_pattern = re.compile(r'^\d{2}:\d{2}:\d{2}$')
        self.assertTrue(time_pattern.match(time_element.text.strip()), f"Incorrect time format: {time_element.text}")

if __name__ == '__main__':
    unittest.main()
