from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def show_moscow_time():
    # Timezone for Moscow (MSK)
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
    return f"<h1>Welcome to my Python Web App!</h1><h1>Current Time in Moscow: {current_time} MSK</h1>"

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000, debug=True)
