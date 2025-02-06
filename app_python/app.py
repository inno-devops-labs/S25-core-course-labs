from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route('/')
def show_time():
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz)
    return render_template(
        'index.html',
        time=current_time.strftime('%Y-%m-%d %H:%M:%S')
    )


if __name__ == '__main__':
    app.run()
