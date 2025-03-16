import pytest
from fastapi.testclient import TestClient
from datetime import datetime
import pytz
import sys
from pathlib import Path

# Add the parent directory to Python path
sys.path.append(str(Path(__file__).parent.parent))

from main import app, get_formatted_times
from config import settings

client = TestClient(app)

def test_get_formatted_times():
    """Test the get_formatted_times function"""
    times = get_formatted_times()
    
    assert isinstance(times, dict)
    assert "moscow_time" in times
    assert "current_time" in times
    
    # Verify time format
    moscow_time = times["moscow_time"]
    assert len(moscow_time.split(":")) == 3  # HH:MM:SS format
    
    current_time = times["current_time"]
    # Check for either full name or abbreviation
    assert any(tz in current_time for tz in ["Moscow", "MSK"])  # Timezone should be present

def test_root_endpoint():
    """Test the root endpoint returns HTML"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    
    # Check if time is present in response
    content = response.text.lower()
    assert "moscow time" in content
    assert "current time" in content

def test_get_time_endpoint():
    """Test the /get_time API endpoint"""
    response = client.get("/get_time")
    assert response.status_code == 200
    
    data = response.json()
    assert isinstance(data, dict)
    assert "moscow_time" in data
    assert "current_time" in data

def test_timezone_validity():
    """Test that the configured timezone is valid"""
    try:
        pytz.timezone(settings.TIMEZONE)
    except pytz.exceptions.UnknownTimeZoneError:
        pytest.fail(f"Invalid timezone: {settings.TIMEZONE}")

@pytest.mark.asyncio
async def test_async_endpoints():
    """Test async endpoints behavior"""
    # Use regular TestClient for async tests as it supports async context
    response = client.get("/get_time")
    assert response.status_code == 200
    data = response.json()
    assert all(key in data for key in ["moscow_time", "current_time"]) 