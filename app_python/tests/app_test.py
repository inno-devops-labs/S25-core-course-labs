from contextlib import contextmanager

from flask import template_rendered

from app_python.app import app


@contextmanager
def captured_templates(app):
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)


def test_index():
    with captured_templates(app) as templates:
        rv = app.test_client().get('/')
        assert rv.status_code == 200
        template, context = templates[0]
        assert template.name == 'index.html'
        assert 'time' in context
