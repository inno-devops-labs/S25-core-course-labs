from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route('/')
def show_moscow_time():
    # Set timezone to Europe/Moscow
    moscow_timezone = pytz.timezone('Europe/Moscow')
    current_time_moscow = datetime.now(moscow_timezone).strftime('%Y-%m-%d %H:%M:%S')

    # Render the template with the current time
    return render_template('index.html', current_time=current_time_moscow)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
