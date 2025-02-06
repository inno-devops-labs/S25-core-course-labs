from main import get_moscow_time
import time


def test_the_hours_in_Moscow():
    # Arrange
    time_data = get_moscow_time()

    # Act
    currentDateAndTime = time.gmtime()

    # Assert
    assert ((currentDateAndTime.tm_hour+3) % 24) == time_data["hours"]
