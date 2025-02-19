# tests/test_app.py
from fastapi.testclient import TestClient
from app_python.app import app
import re

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "Current Time in Moscow" in response.text
    assert re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", response.text) is not None