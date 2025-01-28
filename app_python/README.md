# Python Web Application

## Overview

This project is a Python web application built using the Flask framework.
It displays the current time in Moscow and demonstrates how to create a simple web
service that provides meaningful real-time information in a lightweight and user-friendly manner.

## Features

- **Dynamic Functionality:** The application performs a specific task - displaying real-time data.
- **Scalable and Portable:** Containerized using Docker for easy deployment and scalability.

## Frameworks and Technologies

- **Flask Framework:** A lightweight and easy-to-use Python framework for building web applications.
- **Docker:** For containerizing the application to ensure a consistent and portable runtime environment.

## Installation

### Local Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/yourproject
   ```

2. Navigate to the project directory:

   ```bash
    cd app_python
   ```

3. Install the required dependencies:

   ```bash
    pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python app.py
   ```

5. Open your web browser and navigate to `http://localhost:5000/` to view the application.

### Docker Instruction

1. To build the Docker image run the following command in the terminal from the `app_python` directory with Dockerfile present:

   ```bash
   docker build -t app_python .
   ```

2. To run the Docker image:

   ```bash
   docker run -p 5000:5000 app_python
   ```

3. Alternatively, you can pull the Docker image from my [Dockerhub repository](https://hub.docker.com/r/vladis7love/app_python) using the following commands:

   ```bash
   docker login
   docker pull vladis7love/app_python:latest
   docker run -p 5000:5000 vladis7love/app_python
   ```

## Distroless Images

### Differences Between Distroless Images and Previous Images

1. **Size**:
   - Distroless images are significantly smaller than traditional base images (e.g., `python:slim`, `node:alpine`).
   - They only include the application runtime and its minimal dependencies, reducing bloat.

2. **Security**:
   - Distroless images remove package managers, shells, and other utilities that could be exploited by attackers.
   - They are built to follow the principle of "least privilege."

3. **Non-Root Execution**:
   - By default, Distroless images run as a non-root user, enhancing container security.

4. **Compatibility**:
   - Distroless images are optimized for production environments, ensuring that app runs with only what's strictly necessary.

### Size Comparison

![Image Size Comparison](img/distroless.png)

### Running

```bash
    docker build -t app_python:distroless -f Distroless.Dockerfile .
    docker run -p 5000:5000 app_python:distroless
   ```
