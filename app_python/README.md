# Python web application - Moscow Timezone

![CI Workflow](https://github.com/DoryShibkova/S25-core-course-labs/actions/workflows/ci.yml/badge.svg)

## Overview
This project is a simple Python web application that displays the current time in Moscow. The application uses the **Flask** framework for creating the web server and **pytz** for timezone management. Tracks **visitor count persistence** using a `visits` file and provides an endpoint `/visits` to display the visit count.

## Features
- Displays the current time in Moscow.
- Tracks and **persists visit count** across restarts.
- New `/visits` endpoint shows the number of accesses.
- Automatically updates the time upon refreshing the webpage.

## Technology Stack
- **Python:** Programming language used to develop the application.
- **Flask:** Lightweight web framework for handling HTTP requests.
- **pytz:** Library for accurate timezone management.

## Installation steps

Steps to configure the app locally:
1. **Clone the repository:**
   ```bash
       git clone https://github.com/DoryShibkova/S25-core-course-labs
   ```
2. **Navigate to the project directory:**
   ```bash
       cd app_python
   ```
3. **Create a virtual environment (optional but recommended):**
   ```bash
       python -m venv venv
       source venv/bin/activate  # For Linux/Mac
       venv\Scripts\activate   # For Windows
   ```
4. **Install the required dependencies:**
   ```bash
       pip install -r requirements.txt
   ```
5. **Run the application:**
   ```bash
       python app.py
   ```
6. **Open browser and go to:** http://127.0.0.1:5000/


## Docker

### Login to Docker Hub
Before building or pulling the Docker image, login into Docker Hub:
```bash
docker login
```
You will be prompted to enter your Docker Hub username and password.

### How to Build the Docker Image
To build the Docker image for this application, navigate to the project directory and run:
```bash
docker build -t app .
```

### How to Push the Docker Image to Docker Hub
After building the Docker image, push it to Docker Hub:
```bash
docker tag app <dockerhub-username>/app:latest
docker push <dockerhub-username>/app
```

### How to Pull the Docker Image from Docker Hub
If the image has been pushed to Docker Hub, to pull it use:
```bash
docker pull <dockerhub-username>/app
```

### How to Run the Docker Container
To run the application in a Docker container, use:
```bash
docker run -p 5000:5000 <dockerhub-username>/app
```
**Open browser and visit:** http://127.0.0.1:5000/


## Distroless Image Version

### Build the Distroless Image
```bash
docker build -t app-dist -f distroless.Dockerfile .
```

### Push the Distroless Image to Docker Hub
```bash
docker tag app-dist <dockerhub-username>/app-dist:latest
docker push <dockerhub-username>/app-dist
```

### Pull the Docker Image from Docker Hub
```bash
docker pull <dockerhub-username>/app-dist 
```

### Run the Docker Container
```bash
docker run -p 5000:5000 <dockerhub-username>/app-dist
```
**Open browser and go to:** http://127.0.0.1:5000/

## Unit Tests
Unit tests for this application are written using `unittest`. To run the tests:
```bash
python -m unittest discover
```

## Continuous Integration (CI) Workflow

This project uses **GitHub Actions** for automated Continuous Integration (CI). The CI pipeline ensures:
- **Code quality** through linting (`flake8`)
- **Automated unit tests** using `unittest`
- **Building and pushing Docker images** to Docker Hub

### **CI Workflow Steps**
1. **Checkout Code:** The workflow fetches the latest code from the repository.
2. **Set Up Python Environment:** Installs Python 3.9 and dependencies from `requirements.txt`.
3. **Run Code Linter:** Uses `flake8` to check code style and quality.
4. **Execute Unit Tests:** Runs `unittest` to validate application functionality.
5. **Build Docker Image:** Creates a Docker image for the application.
6. **Push to Docker Hub:** After passing tests, the built image is pushed to Docker Hub.

### **How to View CI Results**
To see the latest CI results, visit the **https://github.com/DoryShibkova/S25-core-course-labs/actions**.

### **Run CI Locally**
To manually test CI steps locally:
```bash
# Run linter
flake8 web_app.py test_web_app.py

# Run unit tests
python -m unittest discover

# Build and run Docker container
docker build -t myapp .
docker run -p 5000:5000 myapp

