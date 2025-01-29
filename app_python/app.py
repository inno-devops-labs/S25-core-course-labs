from flask import Flask, render_template
from datetime import datetime, timezone, timedelta

app = Flask(__name__)


@app.route('/')
def index():
    moscow_time = datetime.utcnow().replace(tzinfo=timezone.utc) + timedelta(hours=3)
    return render_template('index.html', time=moscow_time.strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == '__main__':
    app.run(debug=True)
