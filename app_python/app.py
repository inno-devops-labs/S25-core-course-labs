from flask import Flask, render_template, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

# Function to get the current Moscow time
def get_moscow_time():
    tz = pytz.timezone("Europe/Moscow")
    return datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/time')
def get_time():
    return jsonify(time=get_moscow_time())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# requirements.txt
# Flask
# pytz
