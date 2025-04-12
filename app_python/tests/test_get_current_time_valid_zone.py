from util import get_current_time


def test_get_current_time_valid_zone():
    assert get_current_time("moscow") != "Invalid zone."
