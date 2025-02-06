from main import get_moscow_time
import time


def test_the_minutes_in_moscow():
    # Arrange
    time_data = get_moscow_time()

    # Act
    currentDateAndTime = time.gmtime()

    # Assert
    assert currentDateAndTime.tm_min == time_data["minutes"]
