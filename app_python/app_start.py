from app import TimeService, TemplateService, StatsService, create_app
from datetime import datetime
from zoneinfo import ZoneInfo, available_timezones
from argparse import ArgumentParser
from sys import stderr
from os import path
from prometheus_flask_exporter import PrometheusMetrics

class ZonedTimeService(TimeService):
    def __init__(self, zone: str):
        self.zone = ZoneInfo(zone)

    def current_time(self) -> datetime:
        return datetime.now(self.zone)


class HtmlTemplateService(TemplateService):
    def fill_current_time_template(self, current_time: datetime) -> str:
        return f'<h1>Current time: <a id="current-time">{current_time}</a></h1>'


class FileStatsService(StatsService):
    def __init__(self, file_name: str):
        self.file_name = file_name

    def get_visits(self) -> int:
        if not path.isfile(self.file_name):
            return 0

        with open(self.file_name, 'r') as f:
            return int(f.readline().strip())

    def increment_visits(self):
        v = self.get_visits()
        with open(self.file_name, 'w') as f:
            f.write(str(v + 1))


if __name__ == '__main__':
    parser = ArgumentParser(
        prog='time-application',
        description='Shows time at the specified timezone'
    )

    parser.add_argument(
        '-t', '--timezone',
        help='The timezone to use', type=str,
        default='Europe/Moscow'
    )

    parser.add_argument(
        '--host',
        help='The host to bind', type=str,
        default='0.0.0.0'
    )

    parser.add_argument(
        '-p', '--port',
        help='The port to bind', type=int,
        default=8080
    )

    args = parser.parse_args()

    timezones = available_timezones()
    if args.timezone not in timezones:
        print(f"time-application: error: argument -t/--timezone: invalid choice: '{args.timezone}'", file=stderr)
        print(f'available: {timezones}', file=stderr)
    else:
        app = create_app(ZonedTimeService(args.timezone), HtmlTemplateService(), FileStatsService('visits'))
        metrics = PrometheusMetrics(app)

        metrics.info('time_app_py', 'Python Time Display Application', version='1.0.0')
        app.run(host=args.host, port=args.port)
