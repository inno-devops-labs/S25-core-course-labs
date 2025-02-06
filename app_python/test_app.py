import pytest
from app import app
from datetime import datetime
import pytz
from freezegun import freeze_time

@pytest.fixture
def client():
    """Create a test client for the app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route_status(client):
    """Test if the index route returns 200 status code."""
    response = client.get('/')
    assert response.status_code == 200

def test_index_route_content_type(client):
    """Test if the response content type is HTML."""
    response = client.get('/')
    assert response.content_type == 'text/html; charset=utf-8'

@freeze_time("2024-02-15 12:00:00")
def test_moscow_time_display(client):
    """Test if Moscow time is correctly calculated and displayed."""
    response = client.get('/')
    moscow_tz = pytz.timezone('Europe/Moscow')
    expected_time = datetime.now(moscow_tz)
    assert str(expected_time.strftime('%H:%M')) in response.data.decode()

def test_template_rendering(client):
    """Test if the template is properly rendered with time data."""
    response = client.get('/')
    assert b'Current time in Moscow' in response.data

def test_timezone_conversion():
    """Test timezone conversion logic."""
    moscow_tz = pytz.timezone('Europe/Moscow')
    utc_now = datetime.now(pytz.UTC)
    moscow_time = utc_now.astimezone(moscow_tz)
    assert moscow_time.tzinfo.zone == 'Europe/Moscow'

def test_invalid_route(client):
    """Test handling of invalid routes."""
    response = client.get('/nonexistent')
    assert response.status_code == 404

@pytest.mark.parametrize('test_time', [
    "2024-02-15 00:00:00",
    "2024-02-15 23:59:59",
    "2024-06-15 12:00:00",  # Summer time
    "2024-12-15 12:00:00",  # Winter time
])
@freeze_time()
def test_different_times(client, test_time):
    """Test time display at different times of day and year."""
    with freeze_time(test_time):
        response = client.get('/')
        moscow_tz = pytz.timezone('Europe/Moscow')
        expected_time = datetime.now(moscow_tz)
        assert str(expected_time.strftime('%H:%M')) in response.data.decode() 