from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

VISITS_FILE = "/data/visits.txt"

def increment_visits():
    """Increment the visit counter and return the current count."""
    if not os.path.exists(VISITS_FILE):
        with open(VISITS_FILE, "w") as f:
            f.write("0")
    
    with open(VISITS_FILE, "r+") as f:
        count = int(f.read().strip() or 0)
        count += 1
        f.seek(0)
        f.write(str(count))
        f.truncate()
    
    return count

@app.route('/')
def home():
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
    return render_template("index.html", moscow_time=current_time)

@app.route('/visits')
def visits():
    """Endpoint to display the number of visits."""
    if not os.path.exists(VISITS_FILE):
        return "Visits: 0"
    
    with open(VISITS_FILE, "r") as f:
        count = f.read().strip()
    
    return f"Visits: {count}"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")