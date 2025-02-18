import unittest

from app import initialize_app


class TestAppRoutes(unittest.TestCase):

    def setUp(self):
        self.app = initialize_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_1_index_route_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200, "EXPECTED: 200")
        self.assertIn(b'Moscow', response.data, "EXPECTED: UTC+3 (MSC)")

    def test_2_incorrect_route_404(self):
        response = self.client.get('/accidentaly-incorrect-route')
        self.assertEqual(response.status_code, 404, "EXPECTED: 404")
        self.assertIn(b'404 Not Found', response.data, "EXPECTED: Correct response received")


if __name__ == '__main__':
    unittest.main()
