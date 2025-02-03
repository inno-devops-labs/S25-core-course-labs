from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')

def get_moscow_time():
    # Get Moscow timezone and the current time
    msk_time_zone = pytz.timezone('Europe/Moscow')
    msk_current_time = datetime.now(msk_time_zone).strftime('%H:%M:%S')

    # Show the current time on the page
    return f"<h2>The current time in Moscow:</h2><h1>{msk_current_time}</h1>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
