from flask import Flask
from app_python.app import routes


def create_app():
    app = Flask(__name__)
    return app


app = create_app()
