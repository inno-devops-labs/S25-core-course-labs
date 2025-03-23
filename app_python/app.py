from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def index():
    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz)
    time_str = moscow_time.strftime('%H:%M:%S')
    date_str = moscow_time.strftime('%d.%m.%Y')
    
    return render_template('index.html', time=time_str, date=date_str)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)