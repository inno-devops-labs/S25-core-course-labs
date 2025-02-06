import pytest
from app import app, get_time_from_api
from unittest.mock import patch
import requests


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_root(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"<!DOCTYPE html>" in response.data


def test_get_time(client):
    response = client.get('/time')
    assert response.status_code == 200
    json_data = response.get_json()
    assert "time" in json_data
    assert "status" in json_data
    assert json_data["status"] in ["success", "error"]


@patch('app.requests.get')
def test_get_time_from_api(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"dateTime": "2025-02-06T14:30:00"}

    time = get_time_from_api()
    assert time == "14:30:00"


@patch("app.requests.get")
def test_get_time_from_api_fail(mock_get):
    mock_get.side_effect = requests.RequestException("API is down")
    time = get_time_from_api()
    assert time is None
