import unittest
from unittest.mock import patch
import json
import os
import sys


project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_dir)


from backend.main import app

class FlaskAppTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        app.config['TESTING'] = True
        cls.app = app.test_client()

    def test_get_time(self):
        response = self.app.get('/times')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 4)

    def test_get_current_time(self):
        response = self.app.get('/times/Moscow')
        self.assertEqual(response.status_code, 200)

    def test_get_current_time_not_found(self):
        response = self.app.get('/times/Kazan')
        self.assertEqual(response.status_code, 404)

    if __name__ == '__main__':
        unittest.main()
