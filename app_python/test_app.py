import pytest
from app import app
from unittest.mock import patch
from datetime import datetime
import pytz
import re


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_status_code(client):
    response = client.get('/')
    assert response.status_code == 200


@patch('app.datetime')
def test_home_time_update(mock_datetime, client):
    # Mock current time
    fixed_time = datetime(2023, 1, 1, 12, 0, 0)
    moscow_tz = pytz.timezone('Europe/Moscow')
    mock_datetime.now.return_value = moscow_tz.localize(fixed_time)

    response = client.get('/')
    assert b'2023-01-01 12:00:00' in response.data


def test_home_content(client):
    response = client.get('/')
    html = response.data.decode('utf-8')
    assert "Current Time in Moscow" in html
    assert "<p>" in html


def test_time_format(client):
    response = client.get('/')
    html = response.data.decode('utf-8')
    match = re.search(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})', html)
    assert match, "Time string with expected format not found in response."
