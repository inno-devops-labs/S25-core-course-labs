from datetime import datetime

import pytest
import pytz
from freezegun import freeze_time

from app import app


@pytest.fixture
def test_client():
    """Create a test client for the app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index_route_status(test_client):
    """Test if the index route returns 200 status code."""
    response = test_client.get("/")
    assert response.status_code == 200


def test_index_route_content_type(test_client):
    """Test if the response content type is HTML."""
    response = test_client.get("/")
    assert response.content_type == "text/html; charset=utf-8"


@freeze_time("2024-02-15 12:00:00")
def test_moscow_time_display(test_client):
    """Test if Moscow time is correctly calculated and displayed."""
    response = test_client.get("/")
    moscow_tz = pytz.timezone("Europe/Moscow")
    expected_time = datetime.now(moscow_tz)
    assert str(expected_time.strftime("%H:%M")) in response.data.decode()


def test_template_rendering(test_client):
    """Test if the template is properly rendered with time data."""
    response = test_client.get("/")
    assert b"Current Local Time in Moscow, Russia" in response.data


def test_timezone_conversion():
    """Test timezone conversion logic."""
    moscow_tz = pytz.timezone("Europe/Moscow")
    utc_now = datetime.now(pytz.UTC)
    moscow_time = utc_now.astimezone(moscow_tz)
    assert moscow_time.tzinfo.zone == "Europe/Moscow"


def test_invalid_route(test_client):
    """Test handling of invalid routes."""
    response = test_client.get("/nonexistent")
    assert response.status_code == 404


@pytest.mark.parametrize(
    "test_time",
    [
        "2024-02-15 00:00:00",
        "2024-02-15 23:59:59",
        "2024-06-15 12:00:00",  # Summer time
        "2024-12-15 12:00:00",  # Winter time
    ],
)
@freeze_time()
def test_different_times(test_client, test_time):
    """Test time display at different times of day and year."""
    with freeze_time(test_time):
        response = test_client.get("/")
        moscow_tz = pytz.timezone("Europe/Moscow")
        expected_time = datetime.now(moscow_tz)
        assert str(expected_time.strftime("%H:%M")) in response.data.decode() 