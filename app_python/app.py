from flask import Flask, render_template
from utils.time_util import get_current_time_in_moscow

app = Flask(__name__)


@app.route("/")
def home():
    current_time = get_current_time_in_moscow()
    return render_template("index.html", current_time=current_time)


if __name__ == "__main__":
    app.run(debug=True)
