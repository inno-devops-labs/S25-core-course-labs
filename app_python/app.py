import logging
from flask import Flask
from datetime import datetime
import pytz

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

app = Flask(__name__)


@app.route("/")
def show_time():
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz).strftime("%Y-%m-%d %H:%M:%S")

    logging.info(f"Served current time: {current_time}")

    return f"""
    <html>
        <head>
            <title>Current Time in Moscow</title>
            <style>
                body {{ font-family: Arial, sans-serif;
 text-align: center; padding: 50px; }}
                h1 {{ color: #333; }}
                p {{ font-size: 20px; }}
            </style>
        </head>
        <body>
            <h1>Current Time in Moscow</h1>
            <p>{current_time}</p>
        </body>
    </html>
    """


if __name__ == "__main__":
    logging.info("Starting Flask application...")
    app.run(debug=True, host="0.0.0.0")
