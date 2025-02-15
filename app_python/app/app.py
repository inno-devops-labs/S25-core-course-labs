from datetime import datetime
from os import environ

import pytz
from flask import Flask, render_template

HOST = environ.get("HOST", "0.0.0.0")
PORT = int(environ.get("PORT", "8080"))


def create_app():
    app = Flask(__name__)

    @app.route("/", methods=["GET"])
    def index():
        """
        Returns html page with current Moscow time.
        """
        moscow_timezone = pytz.timezone("Europe/Moscow")
        time = datetime.now(moscow_timezone)
        return render_template("index.html", time=time)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=False)
