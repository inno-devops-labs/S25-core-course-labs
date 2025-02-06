from main import get_moscow_time


def test_the_hours_limits():

    # Arrange
    time_data = get_moscow_time()

    # Assert
    assert 0 <= time_data["hours"] < 24
