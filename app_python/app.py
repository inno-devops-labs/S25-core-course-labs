from datetime import datetime, timezone, timedelta
from os.path import exists
from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(
    __name__,
    template_folder="resources/templates",
    static_folder="resources/static"
)

metrics = PrometheusMetrics(app)

# Moscow time zone is UTC+3
TIMEZONE = 3
DATE_FORMAT = "%a %b %d %H:%M:%S %Y"

# Log file name
filename = "/data/visits"
if not exists(filename):
    with open(filename, "w") as f:
        f.write("0")


# Serve status to Prometheus
@app.route('/status/<int:status>')
@metrics.do_not_track()
@metrics.summary('requests_by_status', 'Request latencies by status',
                 labels={'status': lambda r: r.status_code})
@metrics.histogram('requests_by_status_and_path', 'Request latencies by status and path',
                   labels={'status': lambda r: r.status_code, 'path': lambda: request.path})
def echo_status(status):
    return 'Status: %s' % status, status

# The main page serves time in Moscow
@app.route("/")
def serve_time():
    # Get time in the required timezone and format it
    time_moscow = datetime.now(timezone(timedelta(hours=TIMEZONE)))
    time_moscow = time_moscow.strftime(DATE_FORMAT)
    
    # Increment visit counter
    f = open(filename, "r+")
    count = int(f.read())
    f.seek(0)
    f.write(f"{count+1}")
    f.truncate()
    f.close()

    # Render the template and send it to user
    return render_template("template.html", time_msk=time_moscow)
    
# Display visits to main page endpoint
@app.route("/visits")
def visit_count():
    return open(filename, "r").read()
