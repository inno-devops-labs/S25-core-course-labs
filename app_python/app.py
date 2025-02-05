from flask import Flask, render_template, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

# for testing workflow
# for testing workflow
# for testing workflow

def get_moscow_time():
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz)
    return current_time.strftime('%Y-%m-%d %H:%M:%S %Z')

@app.route('/')
def root():
    return render_template('index.html', time=get_moscow_time())

@app.route('/get_time')
def time_endpoint():
    return jsonify({'time': get_moscow_time()})

if __name__ == '__main__':
    app.run(debug=True)