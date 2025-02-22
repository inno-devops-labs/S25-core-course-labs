from flask import Flask, render_template
from datetime import datetime
import pytz
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

metrics = PrometheusMetrics(app)

@app.route('/')
def home():
    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', time=moscow_time)

if __name__ == '__main__':
    print(app.url_map)
    app.run(host="0.0.0.0", port=5000)
