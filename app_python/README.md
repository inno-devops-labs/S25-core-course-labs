# Moscow Time Web Application

## Overview
This is a simple Python web application built using FastAPI. It displays the current time in Moscow and updates on each page refresh.

## Local Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Dyddxd/S25-core-course-labs.git
   cd app_python
   ```
2. Install dependencies:
    ```bash
   pip install -r requirements.txt
    ```
3. Run the application:
    ```bash
   uvicorn main:app --reload
    ```

## Docker
1. Build:
   ```bash
   cd app_python
   docker build -t moscow-time-app .
   ```
2. Pull the image:
   ```bash
   docker pull zerohalf/moscow-time-app:latest
   ```
3. Run and test working app:
   ```bash
   docker run -d -p 8000:8000 --name moscow-time-container zerohalf/moscow-time-app:latest
   curl localhost:8000
   ```

## Docker Distroless
1. Build:
   ```bash
   cd app_python
   docker build -t fastapi-distroless -f distroless.Dockerfile .
   ```
2. Pull the image
   ```bash
   docker pull zerohalf/fastapi-distroless:nonroot
   ```
3. Run and test working app:
   ```bash
   docker run -d -p 8000:8000 --name fastapi_distroless zerohalf/fastapi-distroless:nonroot
   curl localhost:8000
   ```