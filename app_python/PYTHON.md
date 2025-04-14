# Web Application to Display Current Time in Moscow

This document explains why the **Flask** framework was chosen for the development of the web application that displays Moscow's current time. It also provides a detailed explanation of how the `app.py` (Python code) and `index.html` (HTML template) files work.

---

## Why Flask Was Chosen

Flask is a lightweight and flexible Python web framework suitable for small to medium-sized applications. Here are the reasons for choosing Flask:

1. **Minimalistic and Easy to Use**:
   - Flask is simple to set up and requires minimal boilerplate code, making it ideal for quick development of small-scale applications.

2. **Flexibility**:
   - Flask does not enforce specific tools or libraries, allowing developers to customize the application as needed.

3. **Integrated Templating System**:
   - Flask uses the Jinja2 templating engine, making it easy to render HTML templates dynamically by passing data from Python code.

4. **Active Community and Documentation**:
   - Flask has a large, active community and excellent documentation, which ensures that developers can easily find solutions to any issues.

5. **Sufficient for the Task**:
   - Since the application is simple (fetching and displaying the current time), Flask's lightweight nature is a perfect fit without unnecessary overhead.

---

```python
from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route("/")
def show_time():
    # Get the current time in Moscow
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
    
    return render_template("index.html", time=current_time)

if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
```


```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Current Time in Moscow</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 0;
            padding: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #f4f4f9;
        }
        .container {
            background: #fff;
            padding: 20px 40px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        h1 {
            font-size: 2rem;
            color: #333;
        }
        p {
            font-size: 1.5rem;
            color: #555;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Current Time in Moscow</h1>
        <p>{{ time }}</p>
    </div>
</body>
</html>
```

