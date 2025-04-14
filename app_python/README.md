# Moscow Time Web Application

## Overview
This Python web application displays the current time in Moscow using Flask and `pytz`.

## Requirements
- Flask
- pytz

## Installation
1. Clone the repository:
git clone `https://github.com/Habibullo-777/S25-core-course-labs.git` cd app_python

2. Create a virtual environment and activate it:
python -m venv venv source venv/bin/activate # Mac/Linux venv\Scripts\activate # Windows.

3. Install dependencies:
pip install `-r requirements.txt` .

4. Run the application:
python app.py

5. Open `http://127.0.0.1:8000/` in your browser.


## Git Workflow
- Ensure `.gitignore` is maintained properly.
- Create 2 PRs (pull requests) for collaboration.<br><br>

# Flask Dockerized Application 

## Project Overview
This project demonstrates how to containerize a Flask application using Docker while following best practices.

## Docker Instructions

### 1. Build the Docker Image
Run the following command to build the image:
```bash
docker build -t moscow-time .
```

### 2. Pull the Image from Docker Hub
If the image is pushed to Docker Hub, pull it using:

```bash
docker pull equesmors/moscow-time:latest
```

### 3. Run the Docker Container
Run the container and map the necessary ports:

```sh
docker run -p 8000:8000 moscow-time
```
Now, access the application in your browser: http://localhost:8000


### 4. Check Running Containers
To verify running containers:

```sh
docker ps
```

### 5. View Logs
To view logs from a running container:

```sh
docker logs CONTAINER_ID
```

## Best Practices Followed
- Runs as non-root user.
- Uses .dockerignore to keep image size small.
- Minimal base image (python:3.10-alpine).
- Uses multi-stage builds.
- Optimized layer caching.
