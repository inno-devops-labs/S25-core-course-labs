import unittest
from app_python.app import app


class TestMoscowTime(unittest.TestCase):
    """
    Unit test for the Moscow Time API endpoint.
    """

    def setUp(self):
        """
        Set up the test client.
        """
        self.client = app.test_client()

    def test_moscow_time_endpoint(self):
        """
        Test if the Moscow Time endpoint returns a valid response.
        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Current Moscow Time", response.data.decode())


if __name__ == "__main__":
    unittest.main()
