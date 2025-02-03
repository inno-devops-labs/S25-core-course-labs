from flask import Flask, render_template_string
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route("/")
def home():
    moscow_time = datetime.now(pytz.timezone("Europe/Moscow")).strftime("%Y-%m-%d %H:%M:%S")
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Moscow Time</title>
    </head>
    <body>
        <h1>Current Time in Moscow</h1>
        <p>{{ time }}</p>
    </body>
    </html>
    """, time=moscow_time)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

