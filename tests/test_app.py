import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app_python')))

import unittest
from app import app

class BasicTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_not_found(self):
        response = self.app.get('/non-existent-endpoint')
        self.assertEqual(response.status_code, 404)
        
if __name__ == "__main__":
    unittest.main()