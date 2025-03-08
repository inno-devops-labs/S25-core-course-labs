from prometheus_client import start_http_server, Summary
from flask import Flask, render_template
from datetime import datetime
import pytz

# Start up the server to expose the metrics
start_http_server(8000)

# Create a metric to track time spent and requests made
REQUEST_TIME = Summary('request_processing_seconds',
                       'Time spent processing request')


# Read the number of visits from a file and increment it
def count_visits():
    # Read the number of visits from the file
    with open('visits', 'r') as read_visits:
        counter = read_visits.read()
    # Increment the number of visits and write it back to the file
    with open('visits', 'w') as write_visits:
        write_visits.write(str(int(counter) + 1))
    # Return the number of visits
    return int(counter) + 1


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
    count_visits()

    return render_template('home.html', time=time)


# Define a route for the visits page
@app.route('/visits')
def visits():
    # Get the number of visits from the file
    visits = count_visits()
    # Render the visits.html template with the number of visits
    return render_template('visits.html', visits=visits)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
