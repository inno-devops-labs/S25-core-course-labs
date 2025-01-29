from flask import Flask
from datetime import datetime, timezone, timedelta

app = Flask(__name__)

@app.route("/")
def time():
    return f"{datetime.now(timezone(timedelta(hours=3))).strftime("%H:%M:%S")}"

if __name__ == "__main__":
    app.run()
