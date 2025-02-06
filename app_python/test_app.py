import pytest
from app import app
from datetime import datetime
import pytz


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Current Time in Moscow' in response.data


def test_time_format(client):
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
    response = client.get('/')
    assert current_time.encode() in response.data
