import unittest, subprocess, time, requests, os

SERVER="http://127.0.0.1:8080/"

class TestServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server_process = subprocess.Popen(["./server"])
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.server_process.terminate()
        cls.server_process.wait()

    def test_response_status_code(self):
        response = requests.get(SERVER)
        self.assertEqual(response.status_code, 200)

    def test_response_format(self):
        response = requests.get(SERVER)
        self.assertTrue(response.text.startswith("Random number is: "))
        
        number_str = response.text[len("Random number is: "):]
        self.assertTrue(number_str.isdigit())

if __name__ == "__main__":
    os.system("g++ app.cpp -o server")

    try:
        unittest.main()
    finally:
        if os.path.exists("server"):
            os.remove("server")
