from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route('/')
# Get current time in Moscow
def current_time_moscow():
    # Set timezone
    moscow_tz = pytz.timezone('Europe/Moscow')
    # Get current time in Moscow
    moscow_time = datetime.now(moscow_tz)
    # Format time
    formatted_time = moscow_time.strftime('%Y-%m-%d %H:%M:%S')
    # Return time
    return f'Current time in Moscow: {formatted_time}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
