import datetime
import logging
from flask import Flask, jsonify
from flask_cors import CORS
import pytz
from dotenv import load_dotenv
import os
import sys
from prometheus_flask_exporter import PrometheusMetrics

project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_dir)
from backend.database.db import db, Zones

# Load environment variables from .env file
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Set up CORS
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://myuser:mypassword@localhost:5432/times"#os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db.init_app(app)

# Initialize Prometheus metrics


# Route to get all time zones
@app.route('/times', methods=['GET'])
def get_time():
    try:
        data = Zones.query.all()
        times = []
        if not data:
            logger.error("No cities found in the database.")
            return jsonify({"err": "Cities not found"}), 404
        for d in data:
            times.append({
                'id': d.id,
                'name': d.name,
                'timezone': d.timezone,
            })
        return jsonify(times), 200  # Return JSON
    except Exception as e:
        logger.error(f"Error fetching time zones: {e}")
        return jsonify({"err": "Internal server error"}), 500

# Route to get the current time for a given city
@app.route('/times/<string:name>', methods=['GET'])
def get_current_time(name):
    try:
        data = Zones.query.filter_by(name=name).first()
        if not data:
            logger.error(f"Timezone not found for city: {name}")
            return jsonify({"err": "Timezone not found"}), 404
        tz = pytz.timezone(data.timezone)
        time_now = datetime.datetime.now(tz).strftime('%H:%M:%S')
        logger.info(f"Current time for {name}: {time_now}")
        return jsonify({
            'name': name,
            'time': time_now,
        }), 200
    except Exception as e:
        logger.error(f"Error fetching current time for city {name}: {e}")
        return jsonify({"err": "Internal server error"}), 500

# Create tables and run the application
if __name__ == '__main__':
    metrics = PrometheusMetrics(app,export_defaults=True)
    metrics.info('app_info', 'Application info', version='1.0.0')
    try:
        app.run(host='0.0.0.0', port=8080, debug=False)
        logger.info("App is running successfully")
    except Exception as e:
        logger.error(f"Error starting the application: {e}")
