import pytest
from unittest.mock import patch
from datetime import datetime
import pytz
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@patch('app.datetime')  # Mock datetime in the app module
def test_time_updates(mock_datetime, client):
    # Mock the time for the first request
    mock_datetime.now.return_value = datetime(2023, 10, 1, 12, 0, 0, tzinfo=pytz.timezone('Europe/Moscow'))
    response1 = client.get('/')
    time1 = response1.data.decode()

    # Mock the time for the second request
    mock_datetime.now.return_value = datetime(2023, 10, 1, 12, 0, 1, tzinfo=pytz.timezone('Europe/Moscow'))
    response2 = client.get('/')
    time2 = response2.data.decode()

    # Verify the time has changed
    assert time1 != time2









