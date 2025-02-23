import re
from fastapi.testclient import TestClient
from app_python.main import app

client = TestClient(app)


def test_read_time_status_code():
    """
    Ensure that a GET request to the root endpoint
    ("/") returns an HTTP 200 status code.
    """
    response = client.get("/")
    assert response.status_code == 200, \
        f"Expected status code 200, got {response.status_code}"


def test_read_time_format():
    """
    Ensure that the rendered HTML contains a datetime string
    in the correct format (YYYY-MM-DD HH:MM:SS).
    """
    response = client.get("/")
    content = response.text
    date_pattern = r"\d{4}-\d{2}-\d{2}"
    time_pattern = r"\d{2}:\d{2}:\d{2}"
    date_match = re.search(date_pattern, content)
    time_match = re.search(time_pattern, content)
    assert date_match is not None and time_match is not None, \
        "Rendered template does not contain a valid date or time."
