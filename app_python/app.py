from flask import Flask, jsonify
import os
from datetime import datetime
import pytz
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

VISITS_FILE = 'data/visits'


@app.route('/metrics')


def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}


def get_visits():
    if not os.path.exists(VISITS_FILE):
        return 0
    with open(VISITS_FILE, 'r') as f:
        try:
            return int(f.read().strip())
        except ValueError:
            return 0


def update_visits():
    visits = get_visits() + 1
    with open(VISITS_FILE, 'w') as f:
        f.write(str(visits))
    return visits


@app.route('/')


def index():

    visits = update_visits()

    # Setting Moscow timezone
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
    return f"""
    <html>
        <head>
            <style>

                @import url('https://fonts.googleapis.com/css2?family=Baron+Neue&display=swap');


                body {{
                    background-color: #C7D2A9;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    position: relative;
                    font-family: 'Baron Neue', sans-serif;
                    color: white;
                }}
                h1 {{
                    text-align: center;
                    font-family: 'Baron Neue', sans-serif;
                    color: white;
                }}

                /* CSS decoration: animated flowers */
                .flower {{
                    width: 20px;
                    height: 20px;
                    background: #EFC6B7;
                    border-radius: 50%;
                    position: absolute;
                }}

                .flower::before, .flower::after, .flower .petal1, .flower .petal2, .flower .petal3 {{
                    content: '';
                    width: 20px;
                    height: 20px;
                    background: white;
                    border-radius: 50%;
                    position: absolute;
                }}
                .flower::before {{
                    top: -10px;
                    left: 0;
                }}
                .flower::after {{
                    top: 0;
                    left: -10px;
                }}
                .flower .petal1 {{
                    top: -10px;
                    left: -10px;
                }}
                .flower .petal2 {{
                    top: 10px;
                    left: 0;
                }}
                .flower .petal3 {{
                    top: 0;
                    left: 10px;
                }}
            </style>
        </head>
        <body>
            <h1>Hello! You are visitor number {visits}.<br>
            <h1>Current Time in Moscow: {current_time}</h1>

            <!-- CSS Flowers for decoration -->
            <div class="flower" style="top: 10%; left: 20%;">
                <div class="petal1"></div>
                <div class="petal2"></div>
                <div class="petal3"></div>
            </div>
            <div class="flower" style="top: 30%; left: 50%;">
                <div class="petal1"></div>
                <div class="petal2"></div>
                <div class="petal3"></div>
            </div>
            <div class="flower" style="top: 40%; left: 80%;">
                <div class="petal1"></div>
                <div class="petal2"></div>
                <div class="petal3"></div>
            </div>
            <div class="flower" style="top: 70%; left: 30%;">
                <div class="petal1"></div>
                <div class="petal2"></div>
                <div class="petal3"></div>
            </div>
            <div class="flower" style="top: 90%; left: 80%;">
                <div class="petal1"></div>
                <div class="petal2"></div>
                <div class="petal3"></div>
            </div>
            <div class="flower" style="top: 10%; left: 20%;"></div>
            <div class="flower" style="top: 30%; left: 50%;"></div>
            <div class="flower" style="top: 40%; left: 80%;"></div>
            <div class="flower" style="top: 70%; left: 30%;"></div>
            <div class="flower" style="top: 90%; left: 80%;"></div>
        </body>
    </html>
    """


@app.route('/visits')
def visits_endpoint():
    visits = get_visits()
    return jsonify({"visits": visits})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
