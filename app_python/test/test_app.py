import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "..")))

import re
import pytz
from datetime import datetime
from app_python.app import app  # Import the Flask application
import pytest

@pytest.fixture
def client():
    """Create a test client for Flask."""
    app.config["TESTING"] = True  # Enable testing mode
    with app.test_client() as client:
        yield client


def test_time_format(client):
    """Check if the HTML response contains time in the format HH:MM:SS."""
    response = client.get("/")
    time_match = re.search(
        r"\d{2}:\d{2}:\d{2}",
        response.get_data(
            as_text=True))
    assert time_match is not None, "Time format is incorrect"


def test_time_in_response(client):
    """Check if the HTML response contains the current time in the format HH:MM:SS."""
    response = client.get("/")
    assert response.mimetype == "text/html", "Response should be an HTML page"

    # Get the current Moscow time
    moscow_tz = pytz.timezone("Europe/Moscow")
    expected_time = datetime.now(moscow_tz).strftime("%H:%M:%S")

    # Check if the time is present in the HTML response
    assert expected_time in response.get_data(
        as_text=True), "Time in response does not match the current Moscow time"