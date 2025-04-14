from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def home():
    """
    Returns the current time in Moscow
    """
    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', current_time=moscow_time)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)