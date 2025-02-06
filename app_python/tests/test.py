import unittest
import requests
import datetime
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class Endpoints():

    def make_request(url):
        try:
            response = client.get(url, timeout=3)
            response.raise_for_status()
            return response.status_code
        except requests.exceptions.Timeout as err:
            print(err)
            raise
        except requests.exceptions.HTTPError as err:
            print(err)
            raise

    def get_timezone_info(url):
        try:
            response = client.get(url, timeout=3)
            response.raise_for_status()
            datetime_object = datetime.datetime.strptime(
                response.json()['time'], '%Y-%m-%d %H:%M:%S.%f%z')
            return datetime_object.tzname()
        except requests.exceptions.Timeout as err:
            print(err)
            raise
        except requests.exceptions.HTTPError as err:
            print(err)
            raise


class TestTime(unittest.TestCase):

    URL = '/time/'

    def test_success(self):
        self.assertEqual(200, Endpoints.make_request(self.URL))

    def test_timezone(self):
        self.assertEqual('UTC+03:00', Endpoints.get_timezone_info(self.URL))


if __name__ == '__main__':
    unittest.main()
