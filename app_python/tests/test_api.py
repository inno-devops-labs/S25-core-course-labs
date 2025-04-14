import sys
import os
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
)
from app import app
import pytest
import requests


@pytest.fixture
def client():
    """fixture to create a test client for the Flask app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_api_failure(client, mocker):
    """test handling of an API failure"""
    mocker.patch(
        "requests.get",
        side_effect=requests.RequestException("API error")
    )
    response = client.get('/')
    assert response.status_code == 500  # Expect 500 now
    assert ('an error occurred, please try again later'
            in response.get_data(as_text=True))


def test_home_invalid_json(client, mocker):
    """test handling of invalid JSON response from the API"""
    mock_get = mocker.patch("requests.get")
    mock_get.return_value.json.side_effect = ValueError("invalid JSON")
    mock_get.return_value.raise_for_status.return_value = None
    response = client.get('/')
    assert response.status_code == 500
    assert ('an error occurred, please try again later'
            in response.get_data(as_text=True))
