import pytest
from app import app
from unittest.mock import patch
from datetime import datetime
import pytz


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
