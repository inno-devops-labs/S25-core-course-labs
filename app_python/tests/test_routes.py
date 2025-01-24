import unittest

from app import initialize_app


class TestRoutes(unittest.TestCase):

    def setUp(self):
        self.app = initialize_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_index_route(self):
        """
        Test that correct HTTP response is returned by the server and time in UTC+3 (MSK)
        :return:
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200, "EXPECTED: 200 HTTP")
        self.assertIn(b'Moscow', response.data, "EXPECTED: Moscow in timezone")


if __name__ == '__main__':
    unittest.main()
