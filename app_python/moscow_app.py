"""
- flask is a general python webapp framework
- Module datetime gives us time of any Timezone
"""
from datetime import datetime, timedelta, timezone
from flask import Flask, render_template

app = Flask(__name__)
MOSCOW = timezone(timedelta(hours=3), "Moscow")

@app.route("/")
def index():
    """A primary method generating main and only webpage"""
    msc = datetime.now(MOSCOW)
    current = datetime.today()

    msc = msc.strftime("%H:%M:%S %Z")
    current = current.strftime("%H:%M:%S %Z")

    return render_template("index.html", msc=msc, current=current)


if __name__ == "__main__":
    app.run()
