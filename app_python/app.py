from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route("/")
def get_moscow_time():
    """Returns the time in Europe/Moscow timezone"""
    
    tz_moscow = pytz.timezone("Europe/Moscow")
    moscow_time = datetime.now(tz_moscow).strftime("%H:%M:%S")
    html_content = f"""
    <html>
        <body>
            <h3>Time in Moscow - {moscow_time}</h3>
        </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    app.run()