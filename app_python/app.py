from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def start():
    return render_template('index.html')

if __name__ == 'main':
    app.run(debug=True)