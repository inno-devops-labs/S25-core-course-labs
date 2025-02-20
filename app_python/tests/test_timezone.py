import pytest
from app_python.main import get_location_time
from datetime import datetime


class TestGetLocationTime:
    """
    Test suite for the get_location_time function.
    """

    def test_valid_timezone(self):
        """
        Successful test.
        """
        region = "Europe/Moscow"
        result = get_location_time(region)
        assert isinstance(result, datetime), (
            "The result should be a datetime object."
        )

    def test_invalid_timezone(self):
        """
        Should raise error with invalid timezone.
        """
        region = "Invalid/Timezone"
        with pytest.raises(ValueError) as exc_info:
            get_location_time(region)
        expected_error_message = f"Invalid timezone: {region}"
        assert str(exc_info.value) == expected_error_message, (
            f"The error message should be '{expected_error_message}', "
            f"but got '{str(exc_info.value)}'."
        )

    def test_edge_case_timezone(self):
        """
        Successful test with an edge-case timezone.
        """
        region = "Etc/GMT+12"
        result = get_location_time(region)
        assert isinstance(result, datetime), (
            "The result should be a datetime object."
        )

    def test_timezone_with_special_characters(self):
        """
        Success with not typical region name.
        """
        region = "America/New_York"
        result = get_location_time(region)
        assert isinstance(result, datetime), (
            "The result should be a datetime object."
        )
