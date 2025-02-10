import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_moscow_time_page(mocker):
    mock_get_moscow_time = mocker.patch(
        "app.controllers.time_controller.get_moscow_time"
    )
    mock_get_moscow_time.return_value = "2024-02-03 15:00:00"

    response = client.get("/time")

    assert response.status_code == 200
    assert (
        "2024-02-03 15:00:00" in response.text
    )  # Check if the mocked time is rendered
