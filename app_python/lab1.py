import os

from flask import Flask, render_template
from routes import get_time

app = Flask(__name__)

VISITS_FILE = "/app/data/visits"

@app.route('/')
def time():
    # Увеличиваем счётчик посещений
    count = 0
    if os.path.exists(VISITS_FILE):
        with open(VISITS_FILE, 'r') as f:
            count = int(f.read())
    count += 1
    with open(VISITS_FILE, 'w') as f:
        f.write(str(count))

    current_time = get_time()
    return render_template("index.html", time=current_time)

@app.route('/visits')
def visits():
    if os.path.exists(VISITS_FILE):
        with open(VISITS_FILE, 'r') as f:
            return f"Visits: {f.read()}"
    else:
        return "No visits recorded yet."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
