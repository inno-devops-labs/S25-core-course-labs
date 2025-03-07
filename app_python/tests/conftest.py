import pytest
from flask import template_rendered
from app_python.src.app import create_app


@pytest.fixture
def app():
    return create_app()


@pytest.fixture
def server(app):
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def captured_templates(app):
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    yield recorded
    template_rendered.disconnect(record, app)
