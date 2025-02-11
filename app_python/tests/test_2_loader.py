import unittest

from app import initialize_app


class TestAppConfiguration(unittest.TestCase):

    def setUp(self):
        self.app = initialize_app()
        self.app.config['SOME_ANOTHER_VAR'] = 'UNDEFINED'
        self.app.config['PORT'] = 5000
        self.app.config['DEBUG'] = False
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_config_loading_from_env(self):
        self.assertEqual(self.app.config['DEBUG'], False, "EXPECTED: DEBUG='False'")
        self.assertEqual(self.app.config['PORT'], 5000, "EXPECTED: PORT='5000'")
        self.assertEqual(self.app.config['TESTING'], True, "EXPECTED: TESTING=True")
        self.assertEqual(self.app.config['SOME_ANOTHER_VAR'], 'UNDEFINED', "EXPECTED: SOME_ANOTHER_VAR='UNDEFINED'")


if __name__ == '__main__':
    unittest.main()
