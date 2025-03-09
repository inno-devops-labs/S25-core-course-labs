import unittest
from app_python.app import some_function


class TestApp(unittest.TestCase):
    def test_some_function_case1(self):
        self.assertEqual(some_function(2), 4)

    def test_some_function_case2(self):
        self.assertEqual(some_function(3), 9)

    def test_some_function_case3(self):
        self.assertEqual(some_function(4), 16)

    def test_some_function_case4(self):
        self.assertEqual(some_function(5), 25)

    def test_some_function_case5(self):
        self.assertEqual(some_function(6), 36)


if __name__ == "__main__":
    unittest.main()
