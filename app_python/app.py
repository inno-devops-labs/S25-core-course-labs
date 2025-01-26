from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

# Route for the root URL where moscow_time function will be executed
@app.route('/')
def moscow_time():
    # Setting up a timezone
    moscow_tz = pytz.timezone('Europe/Moscow')
    # Formatting the date and time
    moscow_time = datetime.now(moscow_tz).strftime('%d-%m-%Y    %H:%M:%S')
    # Returning the date and time to the web page
    return f"Current time in Moscow: {moscow_time}"

if __name__ == '__main__':
    app.run(debug=True)
