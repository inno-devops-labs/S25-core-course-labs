from freezegun import freeze_time
import pytest

from app_python import app


@pytest.fixture()
def client():
    return app.app.test_client()


@freeze_time("2025-02-05 22:33:44", tz_offset=-3)
def test_show_moscow_time(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "2025-02-05 22:33:44" in response.get_data(as_text=True)
