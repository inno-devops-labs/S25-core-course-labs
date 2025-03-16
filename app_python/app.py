from flask import Flask, render_template
from datetime import datetime
import pytz
import os

app = Flask(__name__)

# Path to the visits file
VISITS_FILE = "/data/visits.txt"

# Function to ensure the /data directory exists
def ensure_data_directory_exists():
    data_dir = os.path.dirname(VISITS_FILE)
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

# Ensure the /data directory exists
ensure_data_directory_exists()

# Initialize the counter
if not os.path.exists(VISITS_FILE):
    with open(VISITS_FILE, "w") as f:
        f.write("0")

@app.route("/")
def home():
    # Read the current count
    with open(VISITS_FILE, "r") as f:
        count = int(f.read())

    # Increment the count
    count += 1

    # Save the updated count
    with open(VISITS_FILE, "w") as f:
        f.write(str(count))

    # Get the current time in Moscow timezone
    moscow_tz = pytz.timezone("Europe/Moscow")
    moscow_time = datetime.now(moscow_tz)
    current_time = moscow_time.strftime("%Y-%m-%d %H:%M:%S")

    # Render the template with the current time and visit count
    return render_template("index.html", current_time=current_time, visit_count=count)

@app.route("/visits")
def visits():
    # Read the current count
    with open(VISITS_FILE, "r") as f:
        count = int(f.read())

    # Return the total number of visits
    return f"Total visits: {count}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)