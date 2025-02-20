from fastapi.testclient import TestClient
from datetime import datetime
import pytz
import re

from main import app

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