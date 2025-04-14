from prometheus_client import start_http_server, Summary
from flask import Flask, render_template
from datetime import datetime
import pytz

# Start up the server to expose the metrics
start_http_server(8000)

# Create a metric to track time spent and requests made
REQUEST_TIME = Summary('request_processing_seconds',
                       'Time spent processing request')

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
