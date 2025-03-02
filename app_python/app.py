from abc import ABC, abstractmethod
from flask import Flask
from datetime import datetime


class TimeService(ABC):
    @abstractmethod
    def current_time(self) -> datetime:
        pass


class TemplateService(ABC):
    @abstractmethod
    def fill_current_time_template(self, current_time: datetime) -> str:
        pass


def create_app(time_service: TimeService, template_service: TemplateService) -> Flask:
    app = Flask(__name__)

    @app.route('/')
    def index():
        return template_service.fill_current_time_template(time_service.current_time())

    return app
