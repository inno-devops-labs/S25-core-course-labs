from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

def get_msk_time():
    return datetime.now(pytz.timezone('Europe/Moscow'))

@app.route('/')
def show_time():
    msk_time = get_msk_time()
    return f"<h1>Current Time in Moscow: {msk_time.strftime('%H:%M:%S')}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)