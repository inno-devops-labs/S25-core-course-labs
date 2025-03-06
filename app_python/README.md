![example workflow](https://github.com/Lekski1/S25-core-course-labs/actions/workflows/python_ci.yml/badge.svg)

# Moscow Time Web Application

## Overview

This is a web application that displays with each page refresh the current time in Moscow (Moscow +3). The web application uses Python with FastAPI framework and Jinja2 for templating. The application is designed for easy and fast installation.  

## Installation guide 

### Prerequisites

Before you begin, ensure you have the following installed:

*   **Python 3.7+**
*   **pip 19.0+**

### Steps

1.  **Clone the Repository:**

    Clone the project repository to your local machine and navigate to the project directory:

    ```bash
    git clone <repo_url>
    cd <project_directory>
    ```

2.  **Install Dependencies:**

    Change your current directory to `app_python` and install the required libraries:

    ```bash
    cd app_python
    pip install -r requirements.txt
    ```

3.  **Run the Application:**

    Execute the following command to start the application:

    ```bash
    python app.py
    ```

### Troubleshooting

If you encounter an error, please ensure that port 8000 is available. You can either make this port available or modify the port number in the `app.py` file to another available port.


## How to Install using Docker?

Below are the instructions for installing the web application using Docker.

Make sure you have Docker installed on your computer.

### Environment Setup
```
cd app_python/
docker build -t lekski/python-web-app:latest .
```

### Launching the Web App
```
docker run -d -p 8000:8000 lekski/python-web-app:latest
```

You can access the web app at `127.0.0.1:8000`.

### Stopping the Container
```
docker ps
docker stop <container_id>
```

## Distroless Image Version
## How to Install using distroless Docker?

Below are the instructions for installing the web application using distroless Docker.

Make sure you have Docker installed on your computer.

### Environment Setup
```
cd app_python/
docker build -t lekski/python-web-app-distroless:latest -f distroless.Dockerfile .
```

### Launching the Web App
```
docker run -d -p 8000:8000 lekski/python-web-app-distroless:latest
```

You can access the web app at `127.0.0.1:8000`.

### Stopping the Container
```
docker ps
docker stop <container_id>
```

## Unit-tests
The following will provide instructions on how to run unit tests. 
1. Go to the app_python directory 
   ```
   cd app_python
   ```
2. Running unit testing   
   For detailed output of test information:
   ```
   python -m unittest unit_test/app_test.py -v 
   ```
   Minimum testing information: 
   ```
   python -m unittest unit_test/app_test.py
   ```

   Your output should be similar to this(when tested correctly):
   ```
   Ran 2 tests in 0.243s

   OK
   ```

## CI/CD Github Actions
The project has github actions configured to automatically deploy the web-app application when push or pull request to the master branch. 

Settings for workflows:
1.  Navigate to the repository settings: Settings → Secrets → Actions
2.  Create two secrets: `DOCKER_USERNAME` - your Docker login, `DOCKER_PASSWORD` - your Docker login password and `SNYK_TOKEN` - your Snyk api token

## Lab 12
Updated the python web application to the requirement of 12 lab work and added an endpoint that counts the number of visits. 

Also updated monitoring/docker-compose.yaml and added a volume to store a file with the number of visits to the site. 
```
lekski@LAPTOP-EA8M0FT5:/mnt/c/Users/Honor/Desktop/S25-core-course-labs$ curl 127.0.0.1:8000
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./static/css/main.css">
    <title>Moscow</title>
</head>
<body>
    <div class="time">
        <h1 id='main_text'>MSC Time</h1>
        <h1 id='msc-time'>03-03-2025 22:00:41</h1>
    </div>
</body>
</html>
lekski@LAPTOP-EA8M0FT5:/mnt/c/Users/Honor/Desktop/S25-core-course-labs$ curl 127.0.0.1:8000/visits
Visits №1
```