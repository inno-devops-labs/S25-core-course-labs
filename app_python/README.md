# Moscow Time Web App

Displays current Moscow time (MSK) using Python/Flask.
![Demo](./assets/screenshot.png)

## Quick Start
```bash
git clone https://github.com/VilaPat7/S25-core-course-labs.git
git checkout lab1
cd app_python

# Install dependencies
pip install -r requirements.txt

# Run app
python3 app.py
```
Open http://localhost:5000 in browser. Refresh page to update time.

## Features
- Real-time MSK timezone
- Simple Flask implementation
- Auto HTML escaping
- Version-pinned dependencies

## Run with Docker

This application is Dockerized for easy deployment. Follow the steps below to run it using Docker.

### Prerequisites

Docker must be installed on your system. 

### How to Build the Docker Image
```bash
sudo docker build -t vika123vika/app-python:latest .
```

### How to Pull the Docker Image from Docker Hub
```bash
sudo docker pull vika123vika/app-python:latest
```

### How to Run the Docker Container
```bash
sudo docker run -p 5000:5000 vika123vika/app-python:latest
```

### Go to localhost:
Open http://localhost:5000 in browser.
