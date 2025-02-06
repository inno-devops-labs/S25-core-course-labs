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

## How the Code Works

### `app.py` (Python Code)

This is the core Python script that powers the application. Below is the explanation of each part of the script:

```python
from flask import Flask, render_template
from datetime import datetime
import pytz
```

1. **Imports**:
   - `Flask`: The main framework to handle routing and HTTP requests.
   - `render_template`: Used for rendering the HTML template (index.html) with dynamic data.
   - `datetime`: Used to get the current date and time.
   - `pytz`: A library for timezone handling to ensure the displayed time is accurate for Moscow.

```python
app = Flask(__name__)
```

2. **Application Initialization**:
   - A Flask application instance is created using `Flask(__name__)`.

```python
@app.route("/")
def show_time():
    # Get the current time in Moscow
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
    
    return render_template("index.html", time=current_time)
```

3. **Route Definition**:
   - The `@app.route("/")` decorator defines the route for the home page (`/`).
   - The `show_time` function:
     - Retrieves the current date and time for the Moscow timezone using `pytz`.
     - Formats the time as a human-readable string (`'%Y-%m-%d %H:%M:%S'`).
     - Passes the formatted time to the `index.html` template using `render_template`.

```python
if __name__ == "__main__":
    app.run(debug=True)
```

4. **Run the Application**:
   - The script starts the Flask development server when executed directly.
   - `debug=True` enables auto-reloading during development and provides detailed error messages.

---

### `index.html` (HTML Template)

This is the HTML file used to display the current time. Below is the explanation of its structure:

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

1. **Header Section**:
   - The `<meta>` tags ensure the page is encoded properly (`UTF-8`) and is responsive on mobile devices (`viewport` tag).
   - A `<style>` block is included to define styling directly within the HTML file.

2. **Body Styling**:
   - The body uses a **flexbox layout** to center content both vertically and horizontally.
   - A light background color (`#f4f4f9`) is used for visual appeal.

3. **Content Styling**:
   - A `.container` div wraps the main content, with padding, a rounded border, and a subtle shadow for better visual hierarchy.
   - Fonts and colors are chosen to ensure readability and aesthetics.

4. **Dynamic Content**:
   - The `{{ time }}` placeholder is part of Flask's Jinja2 templating system. It is dynamically replaced with the value of the `time` variable passed from the `show_time` function in `app.py`.

---

## How the Application Works

1. When you visit the `/` route in your browser, Flask calls the `show_time` function.
2. The `show_time` function:
   - Retrieves the current time in the Moscow timezone using `pytz`.
   - Formats the time into a readable format (`YYYY-MM-DD HH:MM:SS`).
   - Passes the formatted time to the `index.html` template.
3. The `index.html` template receives the `time` variable and displays it in the `<p>` tag.
4. When the page is refreshed, the `show_time` function is called again, ensuring the displayed time updates.

---
## Unit Tests
```
import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "..")))

import re
import pytz
from datetime import datetime
from app_python.app import app  # Import the Flask application
import pytest

@pytest.fixture
def client():
    """Create a test client for Flask."""
    app.config["TESTING"] = True  # Enable testing mode
    with app.test_client() as client:
        yield client


def test_time_format(client):
    """Check if the HTML response contains time in the format HH:MM:SS."""
    response = client.get("/")
    time_match = re.search(
        r"\d{2}:\d{2}:\d{2}",
        response.get_data(
            as_text=True))
    assert time_match is not None, "Time format is incorrect"


def test_time_in_response(client):
    """Check if the HTML response contains the current time in the format HH:MM:SS."""
    response = client.get("/")
    assert response.mimetype == "text/html", "Response should be an HTML page"

    # Get the current Moscow time
    moscow_tz = pytz.timezone("Europe/Moscow")
    expected_time = datetime.now(moscow_tz).strftime("%H:%M:%S")

    # Check if the time is present in the HTML response
    assert expected_time in response.get_data(
        as_text=True), "Time in response does not match the current Moscow time"

```
# CI Workflow Description and Best Practices

## Workflow Overview
This GitHub Actions CI pipeline automates testing and Docker image deployment for a Flask application. It consists of 2 jobs:
1. **`build-test`**: Runs unit tests and linting.
2. **`docker`**: Builds and deploys a Docker image (only if `build-test` succeeds).

---

## Key Features & Best Practices

### 1. **Trigger Control**
   ```yaml
   on:
     push:
       branches: [lab3]
     pull_request:
       branches: [lab3]
```
## CI workflow
```
name: CI Pipeline

on:
  push:
    branches: [lab3]
  pull_request:
    branches: [lab3]

jobs:
  build-test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          cd app_python
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install flake8

      - name: Run tests (pytest)
        run: pytest

  docker:
    needs: build-test
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Login to Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}

      - name: Build and push Docker image
        run: |
          docker build -t tikhonkhod/flask-moscow-time:1.0 -f app_python/Dockerfile .
          docker push tikhonkhod/flask-moscow-time:1.0
```
## Summary

This application uses Flask for its simplicity and flexibility, making it ideal for small-scale projects. The application separates logic (Python code) from the presentation (HTML template) for better maintainability. The use of `pytz` ensures accurate timezone handling, and the HTML includes responsive design principles to ensure it works well on all devices.
