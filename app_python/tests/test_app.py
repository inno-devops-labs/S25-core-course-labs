# tests/test_app.py
import re
from fastapi.testclient import TestClient
# Adjust the import if your app file has a different name
from app_python.app import app

client = TestClient(app)


def test_show_time_response_structure():
    """
    Test that the '/' endpoint returns a JSON response with a 'message' key
    and that the message begins with the expected prefix.
    """
    response = client.get("/")
    assert response.status_code == 200, "Status code should be 200 OK"

    data = response.json()
    assert "message" in data, "Response JSON should contain a 'message' key"

    expected_prefix = "The current time in Moscow is:"
    assert data["message"].startswith(expected_prefix), (
        f"Message should start with '{expected_prefix}'"
    )


def test_show_time_format():
    """
    Test that the message returned from the '/' endpoint
    contains a datetime in the format 'YYYY-MM-DD HH:MM:SS'
    after the expected text.
    """
    response = client.get("/")
    data = response.json()

    # Define a regex pattern on a single line:
    # "The current time in Moscow is: " followed by
    # a datetime string formatted as YYYY-MM-DD HH:MM:SS
    pattern = r"The current time in Moscow is: \d{4}-\d{2}-\d{2} " \
              r"\d{2}:\d{2}:\d{2}"
    error_msg = (
        "The message does not match the expected format: "
        "'The current time in Moscow is: YYYY-MM-DD HH:MM:SS'"
    )
    assert re.fullmatch(pattern, data["message"]), error_msg
