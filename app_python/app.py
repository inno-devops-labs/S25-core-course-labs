from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route("/")
def moscow_time():
    moscow_tz = pytz.timezone('Europe/Moscow')
    now = datetime.now(moscow_tz)
    current_time = now.strftime("%Y-%m-%d %H:%M:%S %Z%z")
    return f"The current time in Moscow is: {current_time}"

if __name__ == "__main__":
    app.run(debug=True)
