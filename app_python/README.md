# Python Web Application - Current Time in Moscow

This is a simple web application built using **Python** and the **Flask** framework to display the current time in **Moscow**, Russia.

## Overview

This web app shows the current time in Moscow, updating each time the page is refreshed. It uses the **Flask** framework for creating the web server and the **pytz** library for handling timezones.

## Features

- Displays the current time in Moscow.
- Automatically updates the time on page refresh.
- Built with **Flask** for simplicity and efficiency.

## Setup and Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Steps to Run the App

1. **Clone the repository**:

    ```bash
        git clone https://github.com/Kazan-Strelnikova/S25-core-course-labs.git
        cd S25-core-course-labs/app_python
    ```

2. **Install dependencies**:

    ```bash
        pip install -r requirements.txt
    ```

3. **Run the application**:

    ```bash
    python app.py
    ```

4. **Open the app in your browser: Go to <http://localhost:5000> to see the current time in Moscow.**

## Docker Usage

This project can be easily run in a Docker container. Follow the instructions below to build, pull, and run the Dockerized application.

### How to Build

1. Make sure Docker is installed and running on your machine.

2. In the root folder of the project, build the Docker image with the following command:

   ```bash
   docker build -t kira354/app-python .
   ```

### How to Pull

If you want to use the pre-built image from Docker Hub, run the following command:

```bash
docker pull kira354/app-python:latest
```

### How to Run

After building or pulling the image, run the following command to start the application:

```bash
docker run -p 5000:5000 kira354/app-python
```

This will run the application inside the Docker container and map port 5000 of the container to port 5000 on your local machine. You can now access the application by visiting [http://localhost:5000](http://localhost:5000) in your browser.

## **Distroless Image Version**

### **How to Build the Distroless Image**

1. Build the Docker image for the Distroless version:

   ```bash
   docker build -f distroless.Dockerfile -t kira354/app-python-distroless .
   ```

### **How to Pull the Distroless Image**

To pull the Distroless version of the app from Docker Hub:

```bash
docker pull kira354/app-python-distroless
```

### **How to Run the Distroless Image**

To run the Distroless image:

```bash
docker run -p 5000:5000 kira354/app-python-distroless
```
