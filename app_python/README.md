# Flask Time Application

This is a simple web application created using Flask that displays the current time in Moscow. The project consists of two main files: `app.py` (the main application file) and `index.html` (template for displaying the time).

---

## Main files

### 1. `app.py`
This is the main application file written in Python using Flask. It performs the following tasks:
- Creates an instance of the Flask application.
- Defines a route (`/`) that handles requests to the main page.
- Gets the current time in Moscow using the `pytz` library.
- Transfers the time to an HTML template for display.

#### Code:
```python
from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route("/")
def get_time():
    # Specify the time zone of Moscow
    moscow_tz = pytz.timezone('Europe/Moscow')

    # Get the current time in Moscow
    moscow_time = datetime.now(moscow_tz)

    # Format the time
    time = moscow_time.strftime("%H:%M:%S")
    return render_template('index.html', current_time=time)

if __name__ == "__main__":
    app.run()
```
Explanation:

Flask: The main class for creating a web application.

render_template: Function for rendering HTML templates.

pytz: Library for working with time zones.

datetime.now(moscow_tz): Gets the current time in the specified time zone.

render_template('index.html', current_time=time): Transfers the time to the index.html template.

2. templates/index.html
This is an HTML template that displays the current time in Moscow. It uses data passed from Flask to dynamically display the time.

#### Код:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Application for lab1</title>
</head>
<body>
    <h1 class="display-4">Application for lab1</h1>
    <h2 class="mb-3">Hello!</h2>
    <p class="lead">The current time in Moscow is: <strong>{{ current_time }}</strong>.</p>
</body>
</html>
```

Explanation:
<meta charset=“UTF-8”>: Specifies the encoding of the page.

<meta name=“viewport” content=“width=device-width, initial-scale=1.0”>: Makes the page adaptive for mobile devices.

{{ current_time }}: A variable passed from Flask that displays the current time in Moscow.

## Requirements

Flask==3.1.0

pytz==2024.2

### Установка и запуск

1. Клонируйте репозиторий или загрузите файлы проекта.
2. Создайте виртуальное окружение (рекомендуется) и активируйте его.
3. Установите зависимости:
```bash
pip install -r requirements.txt
 ```
4. Запустите приложение:
```bash
python app.py
```
Откройте браузер и перейдите по адресу http://127.0.0.1:5000/ чтобы увидеть текущее время в Москве.

### Установка с помощью Docker

```bash
# pull образа
docker pull gleb2005/flask-moscow-time:1.0
# запуск образа
docker run -p 5000:5000  gleb2005/flask-moscow-time:1.0
# сборка образа
docker build -t gleb2005/flask-moscow-time:1.0 .
```

## Unit Tests

#### Code:
```python
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import pytest
from app_python.app import app  # Import the Flask application
from datetime import datetime
import pytz
import re

@pytest.fixture
def client():
    """Create a test client for Flask."""
    app.config["TESTING"] = True  # Enable testing mode
    with app.test_client() as client:
        yield client


def test_time_format(client):
    """Check if the HTML response contains time in the format HH:MM:SS."""
    response = client.get("/")
    time_match = re.search(r"\d{2}:\d{2}:\d{2}", response.get_data(as_text=True))
    assert time_match is not None, "Time format is incorrect"


def test_time_in_response(client):
    """Check if the HTML response contains the current time in the format HH:MM:SS."""
    response = client.get("/")
    assert response.mimetype == "text/html", "Response should be an HTML page"

    # Get the current Moscow time
    moscow_tz = pytz.timezone("Europe/Moscow")
    expected_time = datetime.now(moscow_tz).strftime("%H:%M:%S")

    # Check if the time is present in the HTML response
    assert expected_time in response.get_data(as_text=True), "Time in response does not match the current Moscow time"
```
### Running the Tests
To execute the unit tests, run the following command from the project root:
```sh
pytest
```
## GitHub Actions CI/CD for Flask Application

This workflow automatically runs tests and builds a Docker image on every `push` and `pull request` to the `master` branch.

###  Workflow Steps

#### 1️ **Build and Test (build-test)**
- **Checkout repository** (`actions/checkout@v4`)
- **Set up Python 3.11** (`actions/setup-python@v5`)
- **Install dependencies** (`pip install -r requirements.txt`)
- **Run tests (`pytest`)** to verify application functionality

#### 2️ **Docker Build and Push (docker)**
- **Checkout repository** (`actions/checkout@v4`)
- **Login to Docker Hub** using GitHub Secrets (`DOCKER_USERNAME` and `DOCKER_PASSWORD`)
- **Build and push Docker image** to `gleb2005/flask-moscow-time:1.0`

###  How It Works?
1. **On every push or pull request to `lab3`**, the CI workflow is triggered.
2. If linting and tests pass, the **Docker image is built**.
3. The final Docker image is **pushed to Docker Hub** 🚀.

###  GitHub Secrets Setup
To enable Docker Hub authentication, add the following GitHub Secrets:
- **DOCKER_USERNAME** → Your Docker Hub username
- **DOCKER_PASSWORD** → Your Docker Hub password

###  `.github/workflows/ci.yml` File
This workflow is stored in `.github/workflows/ci.yml`.  
Commit and push this file to your repository to enable automatic CI/CD.

### Badge 
[![CI Pipeline](https://github.com/Glebias/S25-core-course-labs/actions/workflows/ci.yml/badge.svg)](https://github.com/Glebias/S25-core-course-labs/actions/workflows/ci.yml)

