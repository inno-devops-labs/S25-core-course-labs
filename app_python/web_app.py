from datetime import datetime
import pytz
from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

@app.route('/')
def moscow_time():
    """
    Function to display the current time in Moscow.
    """
    moscow_tz = pytz.timezone('Europe/Moscow')
    # Get the current time in Moscow and format it as 'YYYY-MM-DD HH:MM:SS'
    current_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
    # Return the time as an HTML response
    return f"<h1>Time in Moscow</h1><p>{current_time}</p>"
    
# Run the Flask app if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)
