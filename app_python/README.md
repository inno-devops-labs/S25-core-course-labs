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