import sys
import os
import pytest

# Add the parent directory to sys.path so the test file can find the app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app  # Now this should work

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Test if the home route returns a valid response."""
    response = client.get("/")
    assert response.status_code == 200
    assert isinstance(response.data.decode(), str)  # Ensure response is a string

import re

def test_time_format(client):
    """Test if the response contains a valid time format (HH:MM:SS)."""
    response = client.get("/")
    time_pattern = r"\b\d{2}:\d{2}:\d{2}\b"  # Regex for HH:MM:SS
    assert re.search(time_pattern, response.data.decode()) is not None

def test_invalid_method(client):
    """Test that a POST request to '/' returns 405 (Method Not Allowed)."""
    response = client.post("/")
    assert response.status_code == 405
