import pytest
from app import app

@pytest.fixture
def client():
    # Create a test client using the Flask application configured for testing
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_show_time(client):
    """
    This test verifies that the '/' route returns an HTTP 200 response and
    includes the expected HTML structure.
    """
    response = client.get('/')
    assert response.status_code == 200
    # Check if the returned data includes the title "Current Time in Moscow"
    assert b"Current Time in Moscow:" in response.data
