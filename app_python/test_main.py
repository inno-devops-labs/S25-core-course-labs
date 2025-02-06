import pytest
import re
# Import the Flask application
from main import app


# Fixture to set up the test client
@pytest.fixture
def setUp():
    app.testing = True
    # Create a test client using the Flask application
    return app.test_client()


# Test the home page
def test_home(setUp):
    # Send a GET request to the home page
    response = setUp.get('/')
    # Check if the response status code is 200
    assert response.status_code == 200
    # Check if the response data contains the heading
    assert b'<h1>Moscow Time</h1>' in response.data
    # Check if the response data contains the time pattern
    assert re.search(r"\d{2}:\d{2}", response.data.decode('utf-8'))
