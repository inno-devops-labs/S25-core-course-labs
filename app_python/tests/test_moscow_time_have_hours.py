from main import get_moscow_time


def test_moscow_time_have_hours():
    # Arrange
    time_data = get_moscow_time()

    # Assert
    assert "hours" in time_data
