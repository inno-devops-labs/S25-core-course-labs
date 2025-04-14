from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route("/")
def show_time():
    # Get the current time in Moscow
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
    
    return render_template("index.html", time=current_time)

if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True, host="0.0.0.0")