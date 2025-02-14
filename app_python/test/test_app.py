import pytest
from app import app, get_moscow_time
import pytz
from datetime import datetime
from datetime import timezone
import time

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Current Time in Moscow' in rv.data
    
def test_time_endpoint(client):
    rv = client.get('/get_time')
    assert rv.status_code == 200
    assert 'time' in rv.get_json()

def test_timezone():
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz)
    assert current_time.tzinfo.zone == 'Europe/Moscow'

def test_time_synchronization():
    """Test time synchronization between multiple requests."""
    with app.test_client() as client:

        first_response = client.get('/get_time').get_json()
        time.sleep(1) 
        second_response = client.get('/get_time').get_json()
        

        first_time = datetime.strptime(
            first_response['time'].split(' ')[1],
            '%H:%M:%S'
        )
        second_time = datetime.strptime(
            second_response['time'].split(' ')[1],
            '%H:%M:%S'
        )
        

        time_diff = (second_time - first_time).total_seconds()
        
        assert 0.5 <= time_diff <= 1.5, f"Time difference {time_diff} not within expected range"
