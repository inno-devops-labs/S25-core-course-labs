from fastapi.testclient import TestClient
from app import app

import pytz
from datetime import datetime


# Create a test client for the FastAPI app
client = TestClient(app)


# Helper function to get Moscow time (for comparison in tests)
def get_moscow_time():
    moscow_tz = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(moscow_tz).strftime("%Y-%m-%d %H:%M:%S")
    return current_time


# Test case to check if the root endpoint returns the correct Moscow time
def test_moscow_time():
    response = client.get("/")  # Simulate a GET request to the root endpoint
    assert response.status_code == 200  # Ensure the response status code is 200 (OK)

    # Extract the returned time from the response
    data = response.json()
    returned_time = data.get("Current time in Moscow")

    # Get the current Moscow time for comparison
    expected_time = get_moscow_time()

    # Allow for a small time difference due to execution delay
    returned_date, returned_time_part = returned_time.split(" ")
    expected_date, expected_time_part = expected_time.split(" ")

    # Compare the date part first
    assert returned_date == expected_date

    # Compare the time part with a tolerance of a few seconds
    returned_h, returned_m, returned_s = map(int, returned_time_part.split(":"))
    expected_h, expected_m, expected_s = map(int, expected_time_part.split(":"))

    assert returned_h == expected_h
    assert returned_m == expected_m
    assert abs(returned_s - expected_s) <= 5  # Allow ±5 seconds for delay
