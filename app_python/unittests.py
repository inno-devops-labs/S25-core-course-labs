import unittest, pytz, os
from app import app, current_time, get_timezone
from datetime import datetime



CONFIG_FILE = "config.txt"



class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        """Client settings"""

        self.app = app.test_client()
        self.app.testing = True


    def test_current_time_endpoint(self):
        """Correctness test for endpoint '/'"""

        response = self.app.get("/")
        
        self.assertEqual(response.status_code, 200)
        response_text = response.data.decode("utf-8")
        self.assertIn("Current time in", response_text)
        self.assertIn("is", response_text)


    def test_get_timezone_valid(self):
        """Valid time zone reading test"""

        if os.path.exists("test_get_timezone_valid_config.txt"):
            os.remove("test_get_timezone_valid_config.txt")

        with open("test_get_timezone_valid_config.txt", "w+") as file:
            file.write("Europe/London\n")

        timezone = get_timezone("test_get_timezone_valid_config.txt")
        os.remove("test_get_timezone_valid_config.txt")
        self.assertEqual(timezone, pytz.timezone("Europe/London"))


    def test_get_timezone_invalid(self):
        """Invalid time zone reading test"""
        
        if os.path.exists("test_get_timezone_invalid_config.txt"):
            os.remove("test_get_timezone_invalid_config.txt")

        with open("test_get_timezone_invalid_config.txt", "w+") as file:
            file.write("Invalid/Timezone\n")

        timezone = get_timezone("test_get_timezone_invalid_config.txt")
        os.remove("test_get_timezone_invalid_config.txt")
        self.assertEqual(timezone, pytz.timezone("Europe/Moscow")) 


    def test_get_timezone_empty(self):
        """Empty configure file testing"""

        if os.path.exists("test_get_timezone_empty_config.txt"):
            os.remove("test_get_timezone_empty_config.txt")

        with open("test_get_timezone_empty_config.txt", "w+") as file:
            file.write("\n")

        timezone = get_timezone("test_get_timezone_empty_config.txt")
        os.remove("test_get_timezone_empty_config.txt")
        self.assertEqual(timezone, pytz.timezone("Europe/Moscow"))


    def test_get_timezone_file_not_found(self):
        """No configuration file testing"""

        timezone = get_timezone("")
        self.assertEqual(timezone, pytz.timezone("Europe/Moscow"))


    def test_timezone_format(self):
        """Format testing in response"""

        response = self.app.get("/")
        response_text = response.data.decode("utf-8")
        
        import re
        time_pattern = r"\d{2}:\d{2}:\d{2}"
        self.assertTrue(re.search(time_pattern, response_text))


    def test_full_response(self):
        """Full answer testing"""
        
        try:
            with open(CONFIG_FILE, "r") as config_file:
                time_zone = pytz.timezone(config_file.read().strip())
        except Exception:
            time_zone = pytz.timezone("Europe/Moscow")

        self.assertEqual(current_time(), f"Current time in {time_zone} is {datetime.now(time_zone).strftime('%H:%M:%S')}")
            


if __name__ == "__main__":
    unittest.main()
