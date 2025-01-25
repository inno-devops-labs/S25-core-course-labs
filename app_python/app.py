"""
This is a simple python web application that shows current time in Moscow.
Author: Aleksandr Ryabov (a.ryabov@innoplis.university)
"""

from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

# Set nice date and time format
time_format = '%H:%M:%S %d.%m.%Y'

@app.route('/')
def show_moscow_time():
    """
        Returns an html page with current time in Moscow
    """
    # Get the timezone and current time
    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz).strftime(time_format)

    # Pass the time to the HTML template
    return render_template('moscow_time.html', moscow_time=moscow_time)

if __name__ == '__main__':
    app.run(debug=True)
