import pytest
from pytz import timezone
from datetime import datetime

from app_python.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_moscow_time(client):
    moscow = timezone('Europe/Moscow')
    expected_time = datetime.now(moscow).strftime('%Y-%m-%d %H:%M:%S')

    response = client.get('/')

    assert response.status_code == 200
    assert expected_time[:16] in response.data.decode('utf-8')
