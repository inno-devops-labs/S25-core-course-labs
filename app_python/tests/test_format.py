import sys
import os
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
)
from app import app
import pytest
import re


@pytest.fixture
def client():
    """fixture to create a test client for the Flask app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_time_format(client, mocker):
    """test that the time format follows YYYY-MM-DD HH:MM:SS"""
    mock_response = {
        "dateTime": "2025-02-05T14:30:00.000"
    }
    mock_get = mocker.patch("requests.get")
    mock_get.return_value.json.return_value = mock_response
    mock_get.return_value.raise_for_status.return_value = None
    response = client.get('/')
    assert response.status_code == 200
    time_text = response.get_data(as_text=True)
    assert re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", time_text)


def test_time_format_invalid(client, mocker):
    """test handling when API returns a malformed time format"""
    mock_response = {
        "dateTime": "invalid_time_format"
    }
    mock_get = mocker.patch("requests.get")
    mock_get.return_value.json.return_value = mock_response
    mock_get.return_value.raise_for_status.return_value = None
    response = client.get('/')
    assert response.status_code == 500
    assert ('an error occurred, please try again later'
            in response.get_data(as_text=True))
