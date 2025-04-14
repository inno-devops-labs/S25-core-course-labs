import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    def test_time_format(self):
        response = self.app.get('/')
        pattern = rb'\d{2}:\d{2}:\d{2}'
        self.assertRegex(response.data, pattern)

if __name__ == '__main__':
    unittest.main()
