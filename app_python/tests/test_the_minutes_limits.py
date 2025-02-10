from main import get_moscow_time


def test_the_minutes_limits():
    # Arrange
    time_data = get_moscow_time()

    # Assert
    assert 0 <= time_data["minutes"] < 60
