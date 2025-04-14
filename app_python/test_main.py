from fastapi.testclient import TestClient
from main import app
from datetime import datetime
import pytz

client = TestClient(app)

def test_get_moscow_date():
    moscow_tz = pytz.timezone("Europe/Moscow")
    expected_date = datetime.now(moscow_tz).strftime("%d.%m.%Y %H:%M:%S")

    response = client.get("/")
    
    assert response.status_code == 200

    assert expected_date in response.text

    assert "<title>Moscow Time</title>" in response.text
    assert "<h1>Current Time in Moscow</h1>" in response.text
