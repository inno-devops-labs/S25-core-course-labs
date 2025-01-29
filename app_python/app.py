from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def home():
    moscow_time = datetime.now(pytz.timezone('Europe/Moscow')).strftime('%Y-%m-%d %H:%M:%S')
    return f"Current time in Moscow: {moscow_time}"

if __name__ == '__main__':
    app.run(debug=True)

