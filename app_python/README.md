# Python web application - Moscow Timezone

## Overview
This project is a simple Python web application that displays the current time in Moscow. The application uses the **Flask** framework for creating the web server and **pytz** for timezone management.

## Features
- Displays the current time in Moscow.
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
