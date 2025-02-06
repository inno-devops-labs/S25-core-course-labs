import sys
import os
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
)
import pytest
from app import app


@pytest.fixture
def client():
    """fixture to create a test client for the Flask app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_success(client):
    """test if the home page loads successfully"""
    response = client.get('/')
    assert response.status_code == 200
