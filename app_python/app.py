from flask import Flask, render_template
from datetime import datetime
import pytz

# Initialize the Flask application
app = Flask(__name__)


def get_moscow_time():
    """
        Get the current time in Moscow.
    """
    return datetime.now(pytz.timezone('Europe/Moscow'))


def format_time(time):
    """
        Format into a string in the format 'YYYY-MM-DD HH:MM:SS'.
    """
    return time.strftime('%Y-%m-%d %H:%M:%S')


@app.route('/')
def show_time():
    """
        Route handler for the root URL.
    """
    moscow_time = get_moscow_time()
    formatted_moscow_time = format_time(moscow_time)
    return render_template('index.html',
                           formatted_moscow_time=formatted_moscow_time)


# Run the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
