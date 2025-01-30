# Python Web App

## Overview

This web application displays the current time in Moscow using the Flask framework. The time is shown both digitally and on an analog clock.

## Features

- **Time Display**: Shows the current time in Moscow.
- **Flask Framework**: Used for handling web requests and rendering templates.
- **Modular Design**: Code is separated into Python, CSS, and JavaScript files.

## Installation

1. Clone the repository:

    ```bash
    git clone git clone https://github.com/Friedox/S25-core-course-labs.git
    ```

2. Navigate to the project directory:

    ```bash
    cd app_python
    ```

3. Set up a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

    ```bash
    venv\Scripts\activate
    ```

    - On macOS/Linux:

    ```bash
    source venv/bin/activate
    ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Run the application:

    ```bash
    python app.py
    ```

7. Open the browser and go to `http://127.0.0.1:5000/` to check the app

## Docker

### Build the Docker Image

To build the Docker image for this application, run the following command:

   ```bash
   docker build -f Dockerfile.python -t app-python .
   ```

### Run the Docker Image

   ```bash
   docker run --name app-python-container -p 5000:5000 app-python
   ```

### Pull the Docker Image

   ```bash
   docker pull your-docker-username/app-python:latest
   ```
