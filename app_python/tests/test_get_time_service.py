import unittest
from services.get_time_service import GetTimeService


class TestGetTimeService(unittest.TestCase):
    def test_get_time_by_valid_timezone(self):
        """Test retrieving time for a valid timezone."""
        timezone = "Europe/Moscow"
        result = GetTimeService.get_time_by_timezone(timezone)
        # Ensure the result matches the expected format
        self.assertRegex(result, r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$")

    def test_get_time_by_invalid_timezone(self):
        """Test handling of invalid timezone input."""
        with self.assertRaises(ValueError):
            GetTimeService.get_time_by_timezone("Invalid/Timezone")

    def test_get_time_by_edge_case_timezone(self):
        """Test retrieving time for an edge-case timezone."""
        timezone = "UTC"
        result = GetTimeService.get_time_by_timezone(timezone)
        # Ensure the result matches the expected format
        self.assertRegex(result, r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$")


if __name__ == "__main__":
    unittest.main()
