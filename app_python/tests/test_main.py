import sys
import os
import pytest
import re
from datetime import datetime
import pytz
from main import app


BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')
)
sys.path.insert(0, BASE_DIR)


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index_status_and_content_type(client):
    """Test that the index route returns 200 status and correct content type"""
    response = client.get('/')
    assert response.status_code == 200
    assert response.content_type == 'text/html; charset=utf-8'


def test_response_contents(client):
    """Test that the response contains all elements with formatting"""
    response = client.get('/')
    response_text = response.data.decode('utf-8')

    # Check for static content
    assert 'Welcome to my Python Web App!' in response_text
    assert 'Current Time in Moscow:' in response_text

    # Verify time format and timezone abbreviation
    time_match = re.search(
        r'Current Time in Moscow: (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) MSK',
        response_text
    )
    assert time_match is not None, (
        "Time format is incorrect or MSK timezone not displayed"
    )

    # Validate datetime format
    try:
        datetime.strptime(time_match.group(1), '%Y-%m-%d %H:%M:%S')
    except ValueError:
        pytest.fail("Time string is not a valid datetime")


def test_time_accuracy(client):
    """Test that the displayed time is accurate within a 2-second threshold"""
    response = client.get('/')
    response_text = response.data.decode('utf-8')

    # Extract time from response
    time_match = re.search(
        r'Current Time in Moscow: (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) MSK',
        response_text
    )
    assert time_match is not None
    response_time_str = time_match.group(1)

    # Parse times with Moscow timezone
    moscow_tz = pytz.timezone('Europe/Moscow')
    response_time = moscow_tz.localize(
        datetime.strptime(response_time_str, '%Y-%m-%d %H:%M:%S')
    )
    test_time = datetime.now(moscow_tz)

    # Calculate time difference
    time_diff = abs((test_time - response_time).total_seconds())
    assert time_diff < 2, (
        f"Time discrepancy too large: {time_diff} seconds"
    )
