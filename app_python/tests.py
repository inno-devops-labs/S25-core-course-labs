import unittest
from app import app, get_moscow_time
import json
from datetime import datetime
import pytz

class FlaskAppTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<!DOCTYPE html>', response.data)  # Ensuring HTML is returned
        print("test_home_page: PASSED")

    def test_get_time_endpoint(self):
        response = self.app.get('/time')
        self.assertEqual(response.status_code, 200)
        
        # Parse JSON response
        data = json.loads(response.data)
        self.assertIn('time', data)
        
        # Validate time format
        try:
            datetime.strptime(data['time'], "%Y-%m-%d %H:%M:%S")
            print("test_get_time_endpoint: PASSED")
        except ValueError:
            print("test_get_time_endpoint: FAILED - Invalid time format returned")
            self.fail("Invalid time format returned from /time endpoint")
    
    def test_get_moscow_time(self):
        tz = pytz.timezone("Europe/Moscow")
        expected_time = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        actual_time = get_moscow_time()
        
        # Ensure the format is correct
        try:
            parsed_time = datetime.strptime(actual_time, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            print("test_get_moscow_time: FAILED - Improperly formatted string")
            self.fail("get_moscow_time returned an improperly formatted string")
        
        # Check if the returned time is reasonably close to the expected time
        time_difference = abs((parsed_time - datetime.strptime(expected_time, "%Y-%m-%d %H:%M:%S")).total_seconds())
        self.assertLessEqual(time_difference, 5, "Time difference is too large")
        print("test_get_moscow_time: PASSED")

if __name__ == '__main__':
    unittest.main()
