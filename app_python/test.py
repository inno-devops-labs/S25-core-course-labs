import unittest

from main import app


class TestFlaskMSKTimeApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_world(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn('This is MSK time for now:'.encode(), response.data)

    def test_404_page(self):
        response = self.app.get("/kjasdlkaslkdhl")
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"Page not found", response.data)


if __name__ == "__main__":
    unittest.main()
