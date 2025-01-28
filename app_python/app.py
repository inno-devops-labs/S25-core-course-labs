from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def show_time():
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

if __name__ == '__main__':
    app.run(debug=True)
