from flask import Flask, jsonify
import os
import socket
import datetime

app = Flask(__name__)

# Use a different path for tests
if os.environ.get('TESTING') == 'true':
    VISITS_FILE = "visits.txt"  # Use a local file for testing
else:
    VISITS_FILE = "/data/visits"  # Use the mounted volume in production

def get_visits():
    try:
        if not os.path.exists(VISITS_FILE):
            # Create directory only if using the /data path
            if VISITS_FILE.startswith('/'):
                os.makedirs(os.path.dirname(VISITS_FILE), exist_ok=True)
            with open(VISITS_FILE, "w") as f:
                f.write("0")
            return 0
        
        with open(VISITS_FILE, "r") as f:
            return int(f.read().strip())
    except (IOError, PermissionError):
        # Return a default value if there's an error accessing the file
        return 0

def increment_visits():
    try:
        visits = get_visits() + 1
        with open(VISITS_FILE, "w") as f:
            f.write(str(visits))
        return visits
    except (IOError, PermissionError):
        # Return a default value if there's an error writing to the file
        return 1

@app.route('/')
def hello():
    visits = increment_visits()
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}<br/>" \
           "<b>Current Time:</b> {time}<br/>"
    return html.format(name=os.getenv("NAME", "world"), 
                      hostname=socket.gethostname(),
                      visits=visits,
                      time=current_time)

@app.route('/visits')
def visits():
    return jsonify(
        visits=get_visits()
    )

@app.route('/health')
def health():
    return jsonify(
        status="UP"
    )

@app.route('/version')
def version():
    return jsonify(
        version="1.0.0"
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)