from datetime import datetime

import pytz
from flask import Flask

app = Flask(__name__)


def get_moscow_time():
    try:
        moscow_time = (datetime
                       .now(pytz.timezone('Europe/Moscow'))
                       .strftime('%Y-%m-%d %H:%M:%S')
                       )
        return moscow_time
    except Exception as e:
        print(f"Error fetching Moscow time: {e}")
        return "Error fetching Moscow time"


@app.route('/')
def home():
    moscow_time = get_moscow_time()
    return f"<h1>Current time in Moscow: {moscow_time}</h1>"


@app.errorhandler(404)
def not_found(error):
    return ("<h1>404 - Page Not Found</h1><p>The requested  "
            "URL was not found on the server.</p>"), 404


if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True, host='0.0.0.0', port=5000)
