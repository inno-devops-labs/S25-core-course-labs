from datetime import datetime
from flask import Flask, render_template
import os
import pytz

VISITS_FILE = "visits.txt"

app = Flask(__name__)

def plus_plus():
    if not os.path.exists(VISITS_FILE):
        with open(VISITS_FILE, 'w') as f:
            f.write("0")
    with open(VISITS_FILE, 'r') as f:
        plus = f.read().strip()
        sum = int(plus) if plus.isdigit() else 0
    new_sum = sum + 1
    with open(VISITS_FILE, 'w') as f:
        f.write(str(new_sum))
    return new_sum

@app.route("/")
def get_time():
    try:
        plus_plus()
        moscow_time = datetime.now(
            pytz.timezone('Europe/Moscow')).strftime('%H:%M:%S')
        return render_template("index.html", time=moscow_time)
    except Exception as e:
        app.logger.error(f"An error occurred: {e}")
        return "Internal server error", 500

@app.route("/visits")
def visits():
    try:
        if not os.path.exists(VISITS_FILE):
            sum = 0
        else:
            with open(VISITS_FILE, 'r') as f:
                plus = f.read().strip()
                sum = int(plus) if plus.isdigit() else 0
        return f"Total visits: {sum}"
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9200)
