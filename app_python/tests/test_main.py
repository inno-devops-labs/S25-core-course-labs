import pytest
import re
from fastapi.testclient import TestClient
from app_python.main import app

client = TestClient(app)


def test_get_moscow_time():
    """Test if the root endpoint returns a valid HTML response with time."""
    response = client.get("/")
    assert response.status_code == 200
    assert "<title>Moscow time</title>" in response.text
    assert "<p>Time in Moscow</p>" in response.text


def test_moscow_time_format():
    """Test if the returned time follows HH:MM:SS format."""
    response = client.get("/")
    assert response.status_code == 200

    matches = re.findall(r"<p>(\d{2}:\d{2}:\d{2})</p>", response.text)

    assert matches, "Could not find a valid time format in the response"
    returned_time = matches[0]

    assert len(returned_time) == 8, "Returned time format is incorrect"
    assert returned_time.count(":") == 2, "Time should contain exactly two colons"


def test_unsupported_methods():
    """Test that unsupported HTTP methods return 405 Method Not Allowed."""
    response_post = client.post("/")
    response_put = client.put("/")
    response_delete = client.delete("/")

    assert response_post.status_code == 405
    assert response_put.status_code == 405
    assert response_delete.status_code == 405


def test_internal_server_error(monkeypatch):
    """Simulate an internal server error and check if it returns status code 500."""
    def mock_exception(*args, **kwargs):
        raise Exception("Simulated Internal Server Error")

    monkeypatch.setattr("app_python.main.create_response", mock_exception)

    response = client.get("/")
    assert response.status_code == 500
    assert "<p>Error</p>" in response.text


if __name__ == "__main__":
    pytest.main()
