# Python Web Application: Moscow Time

## Overview

This is a simple Python web application built using the Flask framework, which displays the current time in Moscow. The
time is dynamically updated each time the page is refreshed.

The application uses the `pytz` library to handle time zones and `datetime` to fetch the current time in Moscow.

## Features

- Displays the current time in Moscow.
- The time is updated every time the page is refreshed.
- Developed using Flask, a lightweight web framework.
- Built following best practices for coding standards, testing, and project structure.

## Local installation

To set up and run the application locally, follow these steps:

### Prerequisites:

- Python 3.8 and upper
- A virtual environment (optional)

### Setup instructions:

1. Clone this repository:

   ```bash
   git clone https://github.com/MattWay224/S25-core-course-labs.git
   cd /<your-path>/S25-core-course-labs/app_python/
    ```

2. Create a virtual environment:
    ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment:
    - On Windows:
   ```bash
    .venv\Scripts\activate
   ```
    - On macOS/Linux
   ```bash
   source .venv/bin/activate
   ```

4. Install the required dependencies:
    ```bash
   pip install -r requirements.txt
   ```

5. Run the Flask application:
    ```bash
   python run.py
   ```

6. Open your web browser and visit http://127.0.0.1:5000/ to see the current time in Moscow.

### Unit tests:

To execute unit tests, run:

```sh
pytest app_python/test/test_python.py
```

Ensure dependencies are installed:

```sh
pip install -r app_python/requirements.txt
```

## Docker

### Steps to Build, Push, and Run

1. **Build the Docker Image**:
   ```bash
   docker build -t moscow-time-app:1.0 .
   ```
2. Run Locally:
   ```bash
   docker run -p 5000:5000 moscow-time-app:1.0
   ```

3. Push to Docker Hub (Put your dockerhub username instead of \<username>:

    - Tag the image:
   ```bash
   docker tag moscow-time-app:1.0 <username>/moscow-time-app:1.0
   ```
    - Push the image:
   ```bash
    docker push <username>/moscow-time-app:1.0
   ```

4. Pull and Run:

   ```bash
   docker pull <username>/moscow-time-app:1.0

   ```
   ```bash
   docker run -p 5000:5000 <username>/moscow-time-app:1.0
   ```



