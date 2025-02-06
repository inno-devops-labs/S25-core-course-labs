import socket
from datetime import datetime, timedelta, timezone

import pytest
import requests
from multiprocessing import Process
from app import main

MOSCOW_TZ = timezone(timedelta(hours=3))


def get_free_port() -> int:
    """Finds a free port by binding to port 0, letting the OS choose an available one."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))  # Bind to an available port
        return s.getsockname()[1]  # Return the assigned port


@pytest.fixture(scope="module")
def server_port():
    random_port = get_free_port()

    server_process = Process(target=main, args=(random_port,))
    try:
        server_process.start()
        yield random_port
    finally:
        server_process.terminate()
        server_process.join()
        server_process.close()


def test_server_response(server_port):
    response = requests.get(f"http://localhost:{server_port}")
    assert response.status_code == 200, "Server is not responding"
    assert "moscow_time" in response.json(), "Response does not contain moscow_time"
    moscow_time = datetime.strptime(response.json()["moscow_time"], "%Y-%m-%d %H:%M:%S")
    moscow_time = moscow_time.replace(tzinfo=MOSCOW_TZ)
    expected_moscow_trme = datetime.now(MOSCOW_TZ)
    assert moscow_time - expected_moscow_trme < timedelta(minutes=1), (
        "Incorrect Moscow time"
    )
