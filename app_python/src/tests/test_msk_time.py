from fastapi.testclient import TestClient
from ..main import app
import datetime
import pytz

client = TestClient(app)

def test_get_msk_time():
    response = client.get("/")
    assert response.status_code == 200

    current_date = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
    
    assert current_date.strftime("%H:%M") in response.text
