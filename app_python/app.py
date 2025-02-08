from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def index():
    """Serve the index page with the current Moscow time."""
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', current_time=current_time)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

