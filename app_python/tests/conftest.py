from app.app import app
import pytest


@pytest.fixture()
def flask_app():
    """
    Pytest app fixture.
    """
    f_app = app
    f_app.config.update({"TESTING": True})
    yield f_app


@pytest.fixture()
def client(flask_app):
    """
    Pytest client fixture.
    """
    return flask_app.test_client()


@pytest.fixture()
def runner(flask_app):
    """
    Pytest runner fixture.
    """
    return flask_app.test_cli_runner()
