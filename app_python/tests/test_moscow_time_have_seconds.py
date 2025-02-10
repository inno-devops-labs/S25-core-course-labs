from main import get_moscow_time


def test_moscow_time_have_seconds():

    # Arrange
    time_data = get_moscow_time()

    # Assert
    assert "seconds" in time_data
