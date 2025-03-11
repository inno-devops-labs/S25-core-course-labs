import pytest
from flask import template_rendered

from app_python.api.main import create_app


@pytest.fixture
def app():
    return create_app()


@pytest.fixture
def test_client(app):
    return app.test_client()


@pytest.fixture
def captured_templates(app):
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)
