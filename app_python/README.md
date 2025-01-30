# Python Web Application: Moscow Time

## Overview
This is a simple Python web application that displays the current time in Moscow. The application is built using FastAPI with Python 3.12+ based on standard Python type hints.

## Features
- Displays the current time in Moscow.
- Automatically updates the time upon page refresh.
- Interactive API documentation provided by FastAPI.

## Installation
To run this application locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Fridorovich/S25-core-course-labs/tree/lab1/app_python.git
    cd app_python
2. **Set up a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
4. **Run the application**:
    ```bash
    uvicorn main:app --reload
5. **Access the application**:
    Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Docker
This application is containerized using Docker. Below are instructions for building, running and deploying the Docker image.

### Building the Docker Image

1. Navigate to the `app_python` directory:
    ```bash
    cd app_python
    ```

2. Build the Docker image:
    ```bash
    docker build -t your_dockerhub_username/python-app:latest .
    ```
   Replace `your_dockerhub_username` with your Docker Hub username.

### Running the Docker Container

1. Run the Docker container:
    ```bash
    docker run -d -p 80:80 your_dockerhub_username/python-app:latest
    ```

2. Access the application:
    Open your browser and go to [http://localhost:80/](http://localhost:80/).

### Pushing the Docker Image to Docker Hub

1. Log in to Docker Hub:
    ```bash
    docker login
    ```

2. Push the Docker image:
    ```bash
    docker push your_dockerhub_username/python-app:latest
    ```

### Pulling and Running the Docker Image from Docker Hub

1. Pull the Docker image:
    ```bash
    docker pull your_dockerhub_username/python-app:latest
    ```

2. Run the Docker container:
    ```bash
    docker run -d -p 80:80 your_dockerhub_username/python-app:latest
    ```