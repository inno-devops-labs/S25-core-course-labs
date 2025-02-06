![CI/CD Pipeline](https://github.com/Dema-koder/S25-core-course-labs/actions/workflows/ci.yml/badge.svg)

# Moscow Time Web Application

## Overview

This is a simple Python web application that displays the current time in Moscow. The time updates each time the page is refreshed.

## Requirements

- Python 3.8 or higher
- Flask
- pytz

## Installation

1. Clone this repository:
    ```bash
    git clone <repository-url>
    ```
2. Navigate to the `app_python` directory:
   ```bash
   cd app_python
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser to see the application.

## Features

- Displays the current time in Moscow.
- Automatically updates the time upon page refresh.

## Development Details

- **Framework**: Flask
- **Timezone Handling**: pytz library
- **Code Quality**: Follows PEP 8 guidelines.

## Contribution

To contribute:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Make your changes and create a pull request.

## Docker

### Building and Running the Container

1. **Build the Docker image:**

   ```bash
   docker build -t your-dockerhub-username/app_python .
   ```

2. **Run the container:**

   ```bash
   docker run -p 5000:5000 your-dockerhub-username/app_python
   ```

3. **Push to Docker Hub:**

   ```bash
   docker tag your-dockerhub-username/app_python your-dockerhub-username/app_python:latest
   docker push your-dockerhub-username/app_python:latest
   ```

4. **Pull and run from Docker Hub:**

   ```bash
   docker pull your-dockerhub-username/app_python:latest
   docker run -p 5000:5000 your-dockerhub-username/app_python
   ```

## Continuous Integration (CI)

We use GitHub Actions for automated testing and code validation.

### **CI Workflow Steps**
1. **Install Dependencies** – All required packages from `requirements.txt` are installed.
2. **Linting (Flake8)** – The code is checked for PEP8 compliance.
3. **Run Tests (Pytest)** – Unit tests are executed to validate functionality.
4. **Build and Push Docker Image** – The container is built and pushed to Docker Hub.
5. **Vulnerability Scanning (Snyk)** – Dependencies are scanned for known security vulnerabilities.

### **How to Check CI Status?**
The latest CI run status can be seen in the repository:  
![CI Status](https://github.com/Dema-koder/S25-core-course-labs/workflows/CI/badge.svg)
