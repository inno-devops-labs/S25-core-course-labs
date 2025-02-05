from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route("/")
def show_time():
    moscow_time = datetime.now(pytz.timezone('Europe/Moscow'))
    return f"<h1>Current Time in Moscow: {moscow_time.strftime('%Y-%m-%d %H:%M:%S')}</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
