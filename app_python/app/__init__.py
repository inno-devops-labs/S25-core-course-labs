from flask import Flask

from .config import Config


def initialize_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    with app.app_context():
        from . import routes

    return app
