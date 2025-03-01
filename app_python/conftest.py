from pytest import fixture
from fastapi.testclient import TestClient

from main import app


@fixture
def client():
    return TestClient(app)