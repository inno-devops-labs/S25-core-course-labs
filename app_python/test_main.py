"""Tests for Moscow time Python application"""

import time
from datetime import datetime

import pytz
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_time_is_equal():
    """
    Check that time on API is real Moscow time.
    """
    response = client.get("/")
    assert response.status_code == 200

    moscow_tz = pytz.timezone("Europe/Moscow")
    moscow_time = datetime.now(moscow_tz).strftime("%H:%M:%S")

    assert moscow_time in response.text


def test_time_have_changed():
    """
    Check that time on API is updating over time.
    """
    response1 = client.get("/")
    assert response1.status_code == 200

    time.sleep(1)

    response2 = client.get("/")
    assert response2.status_code == 200

    assert response1.text != response2.text
