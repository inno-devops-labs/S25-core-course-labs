"""Flask web application that displays the current time in Moscow."""
from datetime import datetime
import pytz
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """Render the home page with the current Moscow time."""
    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', current_time=moscow_time)


if __name__ == '__main__':
    app.run(debug=True)
