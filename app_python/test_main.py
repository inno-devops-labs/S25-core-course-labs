import unittest
from main import app


class TestTimeApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_contains_time(self):
        response = self.app.get('/')
        self.assertIn('Current time in Moscow', response.get_data(as_text=True))


if __name__ == '__main__':
    unittest.main()
