# Moscow Time Web Application

A simple Flask-based web application that displays the current time in Moscow.

[![Moscow Time Web Application CI](https://github.com/HayderSarhan/S25-core-course-labs/actions/workflows/CI.yml/badge.svg)](https://github.com/HayderSarhan/S25-core-course-labs/actions/workflows/CI.yml)

---

## Overview

This application uses the Flask framework to create a web server. When accessed, it displays the current time in Moscow in the format `HH:MM` and it shows the number of times it got accessed. The time is fetched using the `pytz` library to handle time zones.

---

## Features

- Displays the current time in Moscow.
- Lightweight and easy to deploy.
- Uses Flask for the web server and `pytz` for time zone handling.
- Show the number of time it got accessed by visiting `/visits`

---

## How to run

- **Clone the repository:**

    ```bash
    git https://github.com/ThePinkPanther77/S25-core-course-labs.git
    cd S25-core-course-labs/app_python
    ```

- **Install the dependencies:**

    ```bash
    pip install -r ./requirements.txt
    ```

- **Run the application:**

    ```bash
    flask --app main.py run
    ```

- **Access the application:** Check the app by opening the browser and navigating to `http://127.0.0.1:5000`

## Docker

This section explains how to build, pull, and run the containerized Flask application.

### 1. How to build the docker image?

1. Navigate to the directory where the `Dockerfile` is located.
2. Build the image:

    ```bash
    docker build -t [image_name] .
    ```

This command will execute the instructions in the `Dockerfile` to create the image, installing dependencies and setting up the Flask application.

### 2. How to pull the docker image?

If you want to pull the pre-built image from [Docker Hub](https://hub.docker.com/r/hayderuni/moscow-time-flask), run the following command:

```bash
docker pull hayderuni/moscow-time-flask
```

### 3. How to run the docker container?

After building or pulling the docker image you can run it using the following command:

```bash
docker run -p 5000:5000 [image_name]
```

**Note:** If the image was pulled from Docker Hub, the name of the image should be: `hayderuni/moscow-time-flask`

After running the the app should be running on `localhost:5000`

## Unit tests

This section is about unit tests included in the project to to verify its functionality.

### How to run the tests

Simply run the following command in the app directory

```bash
pytest test_main.py
```

### Test overview

- **`test_home`:** This test sends a GET request to the home page (/) of the application and verifies:
  - The response status code is `200`.
    - The response contains the correct HTML headings.
    - The response includes the current time in a correct format.

## CI workflow

This sections is about the pipeline and how it works:

- **Setting up the python environment:** The workflow sets up `python 3.10` and installs the necessary dependencies from the `requirements.txt` file.
- **Linting:** The workflow uses `Flake8` to check the code style and report any issues.
- **Testing:** The tests in the workflow are executed using `pytest` to ensure that everything is working as expected.
- **Docker build and push:**
  - The Docker image is built with the latest code from the app_python directory.
    - The image is then pushed to Docker Hub

### Key Components in the Workflow

- **Test Job:** This job ensures the application’s code is linted, the dependencies are installed, and the tests are run.
- **Docker Job:** This job builds and pushes the Docker image to Docker Hub, ensuring that the latest code is always available in the container.
