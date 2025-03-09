from flask import Flask
from datetime import datetime
import pytz
from prometheus_flask_exporter import PrometheusMetrics
import os

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/')
def show_time():
    msc_t = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(msc_t).strftime('%Y-%m-%d %H:%M:%S')
    return f"<h1>Current time in Moscow: {moscow_time}</h1>"

print("Registering /visits route")
@app.route('/visits')
def visits():
    file_path = "visits"
    count = 0
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            try:
                count = int(f.read().strip())
            except ValueError:
                count = 0
    count += 1
    with open(file_path, "w") as f:
        f.write(str(count))
    return f"Number of visits: {count}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
