"""
This is a simple python web application that shows current time in Moscow.
Author: Aleksandr Ryabov (a.ryabov@innoplis.university)
"""

import pytz
from os import environ
from datetime import datetime
from flask import Flask, render_template


HOST = environ.get("HOST", "0.0.0.0")
PORT = int(environ.get("PORT", "8000"))


def create_flask_app() -> Flask:
    """
        Creates an application and configures routes
    """ 
    app = Flask(__name__)

    # Set nice date and time format
    time_format = '%H:%M:%S %d.%m.%Y'

    @app.route('/')
    def show_moscow_time():
        """
            Returns an html page with current time in Moscow
        """
        # Get the timezone and current time
        moscow_tz = pytz.timezone('Europe/Moscow')
        moscow_time = datetime.now(moscow_tz).strftime(time_format)

        # Pass the time to the HTML template
        return render_template('moscow_time.html', moscow_time=moscow_time)
    
    return app


wsgi_app = create_flask_app()


if __name__ == '__main__':
    wsgi_app.run(host=HOST, port=PORT, debug=False)
