from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_moscow_time():
    response = client.get("/")
    assert response.status_code == 200
    assert "Moscow Time" in response.json()

    import re
    time_pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"
    assert re.match(time_pattern, response.json()["Moscow Time"])
