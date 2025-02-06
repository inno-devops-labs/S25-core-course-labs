import unittest

from app_python.app import app  # Ensure correct import path


class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_homepage_status_code(self):
        """Test if homepage returns status code 200"""
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage_content(self):
        """Test if homepage contains 'Current Time in Moscow'"""
        response = self.app.get("/")
        self.assertIn(b"Current Time in Moscow", response.data)

    def test_homepage_mime_type(self):
        """Test if homepage returns text/html"""
        response = self.app.get("/")
        self.assertEqual(response.content_type, "text/html; charset=utf-8")

    def test_invalid_route(self):
        """Test if a non-existent page returns 404"""
        response = self.app.get("/invalid-page")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
