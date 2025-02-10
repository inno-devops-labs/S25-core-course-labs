from main import get_moscow_time


def test_moscow_time_have_minutes():
    # Arrange
    time_data = get_moscow_time()

    # Assert
    assert "minutes" in time_data
