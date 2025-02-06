# Moscow Time Web App

## Overview

This Python web application displays the current time in Moscow. The time updates every time the page is refreshed.

## Features

- Displays Moscow time.
- Lightweight Flask application.
- Uses `pytz` to get accurate timezone data.

## Installation

### Clone the Repository

```sh
git clone https://github.com/Damncaf-goin-crazy/S25-core-course-labs/tree/master
cd app_python
```

### Run the python app

```sh
python time_app.py
```

### Go to <http://127.0.0.1:5000/> in your web browser

## Docker Setup

### **1. Build the Docker Image**

```sh
docker build -t <docker name>/moscow-time-app .
```

### **2. Run the Docker Container Locally**

```sh
docker run -p 5000:5000 <docker name>/moscow-time-app
```

### **3. Push Image to Docker Hub**

```sh
docker login
docker tag <docker name>/moscow-time-app <docker name>/moscow-time-app:latest
docker push <docker name>/moscow-time-app:latest
```

### **4. Pull and Run from Docker Hub**

```sh
docker pull <docker name>/moscow-time-app:latest
docker run -p 5000:5000 <docker name>/moscow-time-app:latest

```

## Running Unit Tests Locally

```sh
python -m pytest test_app.py
```

## GitHub Actions CI

This project uses GitHub Actions to automate:

- Code Testing  
- Linting  
- Docker Build & Push  

### **Workflow Includes**

1. **Install Dependencies**  
2. **Run Linter (flake8)**  
3. **Run Unit Tests (`pytest`)**  
4. **Build & Push Docker Image**
