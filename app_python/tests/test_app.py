from fastapi.testclient import TestClient
import re
from datetime import datetime
from time import sleep

from src.app import app


client = TestClient(app)


def test_read_time():
    response = client.get("/")
    assert response.status_code == 200

    data = response.json()
    assert "Moscow Time" in data

    current_time = data["Moscow Time"]

    time_pattern = r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$"
    assert re.match(time_pattern, current_time), "Time format is not correct"

    print("Extracted time:", current_time)


def test_time_increases_on_refresh():
    response1 = client.get("/")
    data1 = response1.json()
    assert "Moscow Time" in data1
    time1 = data1["Moscow Time"]
    datetime1 = datetime.strptime(time1, "%Y-%m-%d %H:%M:%S")

    sleep(1)

    response2 = client.get("/")
    data2 = response2.json()
    assert "Moscow Time" in data2
    time2 = data2["Moscow Time"]
    datetime2 = datetime.strptime(time2, "%Y-%m-%d %H:%M:%S")

    assert datetime2 > datetime1, "The time did not increase upon page refresh"

    print("First time:", time1)
    print("Second time:", time2)
