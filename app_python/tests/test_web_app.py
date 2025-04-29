import pytest
from datetime import datetime
import pytz
import sys
import os
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_dir)


from web_app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_show_status_code(client):
    response = client.get('/')
    assert response.status_code == 200


def test_show_performance(client):
    import time
    start_time = time.time()
    response = client.get('/')
    end_time = time.time()

    assert end_time - start_time < 1  # response should be within 1 second


def test_show_time_is_current(client):
    response = client.get('/')
    moscow_tz = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(moscow_tz).strftime('%H:%M:%S')

    assert f'Current Moscow time: {current_time}'.encode() in response.data
