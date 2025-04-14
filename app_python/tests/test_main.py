from fastapi.testclient import TestClient
from app.main import app
import re

client = TestClient(app)


def test_get_moscow_time():
    """Test if the Moscow time endpoint returns a valid response"""
    response = client.get("/")

    assert response.status_code == 200

    assert "<title>Moscow Time</title>" in response.text

    time_match = re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", response.text)
    assert time_match is not None, "Timestamp format is incorrect"
