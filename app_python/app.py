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


class StatsService(ABC):
    @abstractmethod
    def get_visits(self) -> int:
        pass
    
    @abstractmethod
    def increment_visits(self):
        pass


def create_app(time_service: TimeService, template_service: TemplateService, stats_service: StatsService) -> Flask:
    app = Flask(__name__)

    @app.route('/')
    def index():
        stats_service.increment_visits()
        return template_service.fill_current_time_template(time_service.current_time())

    @app.route('/visits')
    def visits():
        return str(stats_service.get_visits())

    return app
