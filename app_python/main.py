from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def current_time():
    moscow_time = datetime.now(pytz.timezone('Europe/Moscow'))
    return f"Current time in Moscow: {moscow_time.strftime('%Y-%m-%d %H:%M:%S')}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
