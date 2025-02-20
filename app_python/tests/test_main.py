import unittest
from app_python.main import current_time
from datetime import datetime
import pytz


class TestCurrentTime(unittest.TestCase):
    def test_moscow_time_format(self):
        moscow_time = datetime.now(pytz.timezone('Europe/Moscow'))
        result = current_time()  # Simulate calling the route
        time_str = moscow_time.strftime('%Y-%m-%d %H:%M:%S')
        expected = f"Current time in Moscow: {time_str}"
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
