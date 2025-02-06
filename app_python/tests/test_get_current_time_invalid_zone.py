from util import get_current_time


def test_get_current_time_invalid_zone():
    assert get_current_time("invalid_zone") == "Invalid zone."
