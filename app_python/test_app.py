import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    """Tests for the Flask application"""

    def setUp(self):
        """Set up test client"""
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        """Test if the home page loads successfully"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Current Time in Moscow', response.data)

if __name__ == '__main__':
    unittest.main()

