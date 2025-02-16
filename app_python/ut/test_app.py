import unittest
from app_python.main import app
from bs4 import BeautifulSoup


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_get_time_success(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'time', response.data)

    def test_template_rendering(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        soup = BeautifulSoup(response.data, 'html.parser')
        # <p id="current-time">{{ time }}</p>
        time_element = soup.find(id='current-time')
        self.assertIsNotNone(
            time_element,
            "Element with id='current-time' does not exist")

        import re
        time_pattern = re.compile(r'^\d{2}:\d{2}:\d{2}$')
        self.assertTrue(
            time_pattern.match(
                time_element.text.strip()),
            f"Incorrect time format: {
                time_element.text}")


if __name__ == '__main__':
    unittest.main()
