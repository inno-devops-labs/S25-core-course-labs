from flask import Flask, render_template_string
from datetime import datetime
import pytz
import os

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Moscow Time</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f2f5;
        }
        .container {
            text-align: center;
            padding: 2rem;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        .time {
            font-size: 3rem;
            color: #1a73e8;
            margin: 1rem 0;
        }
        .date {
            font-size: 1.5rem;
            color: #5f6368;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="time">{{ time }}</div>
        <div class="date">{{ date }}</div>
    </div>
</body>
</html>
'''


@app.route('/')
def index():
    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz)

    time_str = moscow_time.strftime('%H:%M:%S')
    date_str = moscow_time.strftime('%B %d, %Y')

    return render_template_string(HTML_TEMPLATE, time=time_str, date=date_str)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=os.environ.get('FLASK_DEBUG', False))
