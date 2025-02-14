import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import unittest
from fastapi.testclient import TestClient
from app_python.app import app 
from datetime import datetime
import pytz
from bs4 import BeautifulSoup
from unittest.mock import patch

class Test_Web_App(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    def test_server_start(self):
        '''Server performance testing '''        
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_time_check(self):
        '''Testing of correct time indication on the website '''
        resp = self.client.get('/')

        soup = BeautifulSoup(resp.text, "html.parser")
        time_element = soup.find(id="msc-time")
        time_str_from_response = time_element.get_text().strip()

        timezone = pytz.timezone('Europe/Moscow')
        time_in_test = datetime.now(timezone).timestamp()
        time_in_site = timezone.localize(datetime.strptime(time_str_from_response, '%d-%m-%Y %H:%M:%S')).timestamp()


        self.assertAlmostEqual(time_in_test, time_in_site, delta = 5)

if __name__ == '__main__':
    unittest.main()

