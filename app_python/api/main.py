from datetime import datetime
from flask import Flask, render_template
import pytz


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        try:
            moscow_tz = pytz.timezone('Europe/Moscow')
            moscow_time = datetime.now(moscow_tz).strftime('%H:%M:%S')
            return render_template("index.html", time=moscow_time)
        except Exception as e:
            return e, 500

    return app


if __name__ == "__main__":
    main_app = create_app()
    main_app.run(debug=True, host='0.0.0.0', port=5000)
