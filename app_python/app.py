from flask import Flask
from datetime import datetime
import pytz
import os

VISITS_FILE = "visits"

app = Flask(__name__)

# Initialize visit count
if not os.path.exists(VISITS_FILE):
    with open(VISITS_FILE, "w") as f:
        f.write("0")

@app.route("/")
def home():
    # Read current count
    with open(VISITS_FILE, "r") as f:
        count = int(f.read())

    # Increment count
    count += 1
    with open(VISITS_FILE, "w") as f:
        f.write(str(count))

    # Get Moscow time
    moscow_time = datetime.now(pytz.timezone("Europe/Moscow")).strftime("%Y-%m-%d %H:%M:%S")

    return f"<h1>Current Time in Moscow</h1><p>{moscow_time}</p>"

@app.route("/visits")
def visits():
    with open(VISITS_FILE, "r") as f:
        count = f.read()
    return f"<h1>Visit Count</h1><p>{count}</p>"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=4000)
