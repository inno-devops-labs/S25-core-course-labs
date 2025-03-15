import pytest
from pytz import timezone
from datetime import datetime
from unittest.mock import patch
from app_python.run import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_dynamic_time(client):
    moscow = timezone('Europe/Moscow')
    expected_time = datetime.now(moscow).strftime('%Y-%m-%d %H:%M:%S')

    response = client.get('/')

    assert response.status_code == 200
    assert expected_time[:16] in response.data.decode('utf-8')


def test_static_time(monkeypatch, client):
    moscow = timezone('Europe/Moscow')
    fixed_time = datetime(2024, 2, 4, 12, 0, 0, tzinfo=moscow)

    with (patch("run.datetime") as mock_datetime):
        mock_datetime.now.return_value = fixed_time
        mock_datetime.strftime = datetime.strftime

        response = client.get('/')

        assert response.status_code == 200
        time_str = fixed_time.strftime('%Y-%m-%d %H:%M:%S')
        response_data = response.data.decode('utf-8')
        assert time_str in response_data
