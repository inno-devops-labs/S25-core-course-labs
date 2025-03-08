from fastapi.testclient import TestClient
from datetime import datetime
import pytz
import os
import tempfile
from unittest import mock
from main import app
from routers.time import VISITS_FILE

client = TestClient(app)

def test_root_endpoint():
    """
    Main page valid html returning test 
    """
    with tempfile.NamedTemporaryFile() as temp_file:
        with mock.patch('routers.time.VISITS_FILE', temp_file.name):
            response = client.get("/")
            assert response.status_code == 200
            assert "Moscow Time" in response.text
            assert 'class="time-container"' in response.text
            assert 'Total visits:' in response.text

def test_time_endpoint():
    """
    Time endpoint test
    """
    response = client.get("/time")
    assert response.status_code == 200
    
    assert "time" in response.json()
    
    time_str = response.json()["time"]
    try:
        datetime.strptime(time_str, '%H:%M:%S')
    except ValueError:
        assert False, "Invalid format"

def test_time_accuracy():
    """
    MSK time accuracy test
    """
    response = client.get("/time")
    api_time = response.json()["time"]
    
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_moscow_time = datetime.now(moscow_tz).strftime('%H:%M:%S')
    
    # Check that difference does not exceed 2 seconds
    api_time_obj = datetime.strptime(api_time, '%H:%M:%S')
    current_time_obj = datetime.strptime(current_moscow_time, '%H:%M:%S')
    time_diff = abs((api_time_obj.hour * 3600 + api_time_obj.minute * 60 + api_time_obj.second) - 
                    (current_time_obj.hour * 3600 + current_time_obj.minute * 60 + current_time_obj.second))
    assert time_diff <= 2, "Difference > 2 seconds"

def test_html_structure():
    """
    HTML structure test
    """
    with tempfile.NamedTemporaryFile() as temp_file:
        with mock.patch('routers.time.VISITS_FILE', temp_file.name):
            response = client.get("/")
            html_content = response.text
            
            assert "<title>Moscow Time</title>" in html_content
            assert 'id="moscow-time"' in html_content
            assert "setInterval(updateTime, 1000)" in html_content
            assert 'id="visit-count"' in html_content

def test_visits_endpoint():
    """
    Visits endpoint test
    """
    with tempfile.NamedTemporaryFile() as temp_file:
        with mock.patch('routers.time.VISITS_FILE', temp_file.name):
            # Write a test value to the mock file
            with open(temp_file.name, 'w') as f:
                f.write('42')
            
            response = client.get("/visits")
            assert response.status_code == 200
            assert "visits" in response.json()
            assert response.json()["visits"] == 42

def test_visit_counter_increment():
    """
    Visit counter increment test
    """
    with tempfile.NamedTemporaryFile() as temp_file:
        with mock.patch('routers.time.VISITS_FILE', temp_file.name):
            # Write a starting value
            with open(temp_file.name, 'w') as f:
                f.write('10')
            
            # First visit
            response1 = client.get("/")
            assert response1.status_code == 200
            
            # Check that the counter was incremented
            response2 = client.get("/visits")
            assert response2.json()["visits"] == 11
            
            # Another visit
            response3 = client.get("/")
            assert response3.status_code == 200
            
            # Check that the counter was incremented again
            response4 = client.get("/visits")
            assert response4.json()["visits"] == 12