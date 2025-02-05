import pytz

from flask import Flask, render_template

from datetime import datetime


# Initialize Flask application
def init_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        # Get the current time in Moscow timezone
        moscow_tz = pytz.timezone('Europe/Moscow')
        current_time = datetime.now(moscow_tz).strftime("%Y-%m-%d %H:%M:%S")

        # Render template with the current time
        return render_template('index.html', current_time=current_time)

    return app


if __name__ == '__main__':
    app = init_app()
    app.run(host="0.0.0.0", port=5000)
