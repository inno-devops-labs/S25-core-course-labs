from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

from .config import Config


def initialize_app():
    """
    Initialize application with the given routes and context
    :return: Flask app
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    PrometheusMetrics(app)

    with app.app_context():
        from . import routes

    return app
