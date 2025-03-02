from flask import Flask, render_template
from routes import get_time

app = Flask(__name__)


@app.route('/')
def time():
    current_time = get_time()
    return render_template("index.html", time=current_time)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
