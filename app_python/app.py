import os
from flask import Flask
from datetime import datetime
import pytz
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.StreamHandler()])

def create_app():
    app = Flask(__name__)
    visits_file = os.getenv('VISITS_FILE', '/data/visits.txt')
    data_dir = os.path.dirname(visits_file)

    try:
        os.makedirs(data_dir, exist_ok=True)
        if not os.path.exists(visits_file):
            with open(visits_file, 'w') as f:
                f.write('0')
    except PermissionError as e:
        logging.error(f"CRITICAL PERMISSION ERROR: {e}")
        raise RuntimeError(f"Check permissions for: {visits_file}") from e

    def get_visits():
        try:
            with open(visits_file, 'r') as f:
                return int(f.read().strip())
        except Exception as e:
            logging.error(f"Read error: {e}")
            return 0

    def increment_visits():
        count = get_visits() + 1
        try:
            with open(visits_file, 'w') as f:
                f.write(str(count))
            return count
        except Exception as e:
            logging.error(f"Write error: {e}")
            raise

    @app.route('/')
    def show_moscow_time():
        increment_visits()
        time = datetime.now(pytz.timezone('Europe/Moscow')).strftime('%Y-%m-%d %H:%M:%S')
        return f"<h1>Moscow time: {time}</h1>"

    @app.route('/visits')
    def show_visits():
        return f"<h1>Total visits: {get_visits()}</h1>"

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)