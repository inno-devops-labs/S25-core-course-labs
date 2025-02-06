import sys
import pytest

sys.path.append('..\\app_python')

import app as app_python_app
"""
Primarily taken from https://flask.palletsprojects.com/en/stable/tutorial/tests/ and
then changed to be applicable to this project, as it is simpler than their example.
"""
@pytest.fixture
def app():
    app = app_python_app.app
    yield app

@pytest.fixture
def client(app):
    return app.test_client()
