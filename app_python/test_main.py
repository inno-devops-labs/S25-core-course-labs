import os
from fastapi.testclient import TestClient
from datetime import datetime
import pytz
import re

from main import app, VISITS_FILE, read_visits, write_visits

client = TestClient(app)

MOSCOW_TZ = pytz.timezone("Europe/Moscow")


def test_get_moscow_time():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

    match = re.search(r"\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2}", response.text)
    assert match is not None, "Expected Moscow time format not found in response"

    extracted_time = datetime.strptime(match.group(), "%d.%m.%Y %H:%M:%S")
    extracted_time = MOSCOW_TZ.localize(extracted_time)

    now_moscow = datetime.now(MOSCOW_TZ)
    time_difference = abs((now_moscow - extracted_time).total_seconds())

    assert time_difference < 5, "Moscow time in response is not recent"

def test_visits_counter():
    if os.path.exists(VISITS_FILE):
        os.remove(VISITS_FILE)
    
    # Initial state
    initial_count = read_visits()
    assert initial_count == 0, "Visits count should be 0"
    
    # First request
    client.get("/")
    assert read_visits() == 1, "Visits count should be 1"
    
    # Second request
    client.get("/")
    assert read_visits() == 2, "Visits count should be 2"

def test_visits_endpoint():
    response = client.get("/visits")
    assert response.status_code == 200
    assert "application/json" in response.headers["content-type"]
    
    visits_data = response.json()
    assert "visits" in visits_data, "Response should contain 'visits' key"
    assert isinstance(visits_data["visits"], int), "Visits count should be an integer"