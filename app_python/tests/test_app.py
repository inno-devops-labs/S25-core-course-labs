import unittest
import tempfile
import os
from app import app


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        os.environ["DATA_DIR"] = self.temp_dir.name
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_index(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"The current time in Moscow is:", response.data)

    def test_get_time(self):
        response = self.app.get("/time")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"time", response.data)


if __name__ == "__main__":
    unittest.main()
