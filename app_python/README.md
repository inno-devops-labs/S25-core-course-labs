# Moscow Time Web Application

A simple Flask-based web application that displays the current time in Moscow.

---

## Overview

This application uses the Flask framework to create a web server. When accessed, it displays the current time in Moscow in the format `HH:MM`. The time is fetched using the `pytz` library to handle time zones.

---

## Features

- Displays the current time in Moscow.
- Lightweight and easy to deploy.
- Uses Flask for the web server and `pytz` for time zone handling.

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