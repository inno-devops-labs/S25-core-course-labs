from flask import Flask, render_template
from datetime import datetime
import pytz

# Create a Flask web app
app = Flask(__name__)


# Define a route for the default URL
@app.route('/')
def home():
    # Get the current time in Moscow
    time_zone = pytz.timezone('Europe/Moscow')
    # Format the time as HH:MM
    time = datetime.now(time_zone).strftime('%H:%M')
    # Render the home.html template with the time
    return render_template('home.html', time=time)
