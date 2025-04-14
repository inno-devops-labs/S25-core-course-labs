from datetime import datetime, timezone, timedelta
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def time_request():
    moscow_tz = timezone(timedelta(hours=3))  # Moscow timezone is UTC +3
    moscow_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')

    return render_template('time_request.html', time=moscow_time)


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)
