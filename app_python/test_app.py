from datetime import datetime
import unittest

from pytz import timezone
from app import app

class TestApp(unittest.TestCase):
    #Set up test client
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_time_page(self):
        #Send GET request to server
        response = self.app.get('/')
        
        #Get current time in Moscow
        moscow_time = datetime.now(timezone('Europe/Moscow')).strftime('%Y-%m-%d %H:%M:%S')
        
        #Check if server returns OK status code
        self.assertEqual(response.status_code, 200)
        #Check if server returns correct time
        self.assertIn(f'Current time in Moscow: {moscow_time}', response.data.decode())
        
        
if __name__ == '__main__':
    unittest.main()
