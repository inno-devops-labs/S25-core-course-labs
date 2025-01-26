# Python Web Application

## Overview

This is a simple Python web application that displays the current time in the Moscow (MSK) timezone.  
It uses the **Flask** framework and the **pytz** library (or similar) to provide accurate local time.

## Features

- Displays hours, minutes, and seconds for the MSK timezone.
- Updates automatically when the page is refreshed.
- Follows PEP 8 coding standards and uses a virtual environment for dependencies.

## Local Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-account/your-repo.git
2. Navigate to app_python and (optionally) create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or
   venv\Scripts\activate     # Windows
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Run the application:
   ```bash
   python main.py
5. Open http://127.0.0.1:5000 in your browser.

## Docker

This application can be containerized in two ways: using a **standard Dockerfile** or a **Distroless** variant.

### How to build (Standard Dockerfile)

1. Navigate to `app_python` folder.
2. Build the Docker image (replace `your-dockerhub-user` with your Docker Hub username):
   ```bash
   docker build -t your-dockerhub-user/python-app:latest .
3. Run the container locally:
   ```bash
   docker run -it --rm -p 5000:5000 your-dockerhub-user/python-app:latest

### How to push
1. Log in to Docker Hub:
   ```bash
   docker login
2. Push the image:
   ```bash
   docker push your-dockerhub-user/python-app:latest
### How to pull
- Once pushed, anyone can pull and run:
   ```bash
   docker pull your-dockerhub-user/python-app:latest
   docker run -it --rm -p 5000:5000 your-dockerhub-user/python-app:latest
### Distroless Image Version
If you wish to use the Distroless version:
1. Build from distroless.Dockerfile:
   ```bash
   docker build -f distroless.Dockerfile -t your-dockerhub-user/python-app:distroless .
2. Run:
   ```bash
   docker run -it --rm -p 5000:5000 your-dockerhub-user/python-app:distroless
3. Compare image sizes with the regular version.