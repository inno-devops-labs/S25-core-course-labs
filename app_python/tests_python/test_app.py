import unittest
from app_python.app import show_time


class TestApp(unittest.TestCase):
    """Unit tests for show_time function."""

    def test_show_time_returns_string(self):
        """
        Test that show_time function returns
        a string containing the date format.
        """
        response = show_time()
        self.assertIn("Current Time in Moscow", response)


if __name__ == "__main__":
    unittest.main()
