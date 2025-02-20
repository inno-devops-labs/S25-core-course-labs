from flask import Flask
from datetime import datetime
import pytz
import logging
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest, Counter, start_http_server

app = Flask(__name__)

REQUEST_COUNT = Counter('app_python_requests_total', 'Total requests to the application')

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def current_time():
    moscow_time = datetime.now(pytz.timezone('Europe/Moscow'))
    time_str = moscow_time.strftime('%Y-%m-%d %H:%M:%S')
    
    # Log the current time request
    logger.info(f"Current time requested: {time_str}")
    # Increment the request counter
    REQUEST_COUNT.inc()
    
    return f"Current time in Moscow: {time_str}"

@app.route('/metrics')
def metrics():
    # Return the current metrics as a response
     return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    # Log when the server starts
    logger.info("Starting Flask server...")
    # Expose metrics at port 8000
    start_http_server(8000)
    app.run(host="0.0.0.0", port=5000)
