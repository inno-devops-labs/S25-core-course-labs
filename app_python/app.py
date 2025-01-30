from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def getCurrentTime():
    moscowTimeZone = pytz.timezone("Europe/Moscow")
    currentTime = datetime.now(moscowTimeZone).strftime("%H:%M:%S")
    return render_template("index.html", time=currentTime)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

