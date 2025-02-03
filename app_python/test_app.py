from fastapi.testclient import TestClient
from app import app, get_moscow_time
from unittest.mock import patch


client = TestClient(app)


def test_get_moscow_time():
    """
    Test get_moscow_time() function to ensure it returns a valid time format.
    """
    time_str = get_moscow_time()
    assert isinstance(time_str, str)
    assert len(time_str.split(":")) == 3  # Ensures format is HH:MM:SS


@patch("app.get_moscow_time", return_value="12:34:56")
def test_read_root(mock_get_moscow_time):
    """
    Test the FastAPI root endpoint to check if the correct response is returned.
    """
    response = client.get("/")
    assert response.status_code == 200
    json_data = response.json()
    assert "message" in json_data
    assert json_data["message"] == "The current time in Moscow is 12:34:56"


def test_invalid_route():
    """
    Ensure accessing a non-existent route returns a 404 error.
    """
    response = client.get("/nonexistent")
    assert response.status_code == 404
