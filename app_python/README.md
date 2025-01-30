# Moscow Time Web App

This is a python application built with FastAPI and jinja2 to display current time in Moscow.

## Features

- Displays Moscow time
- Renders HTML dynamically using jinja2

## Requirements

- Python 3.12.7 (built and tested on this version)
- `pip` package manager

## Installation

1. Clone the repo:

    ```bash
    git clone https://github.com/justcgh9/S25-core-course-labs.git
    cd S25-core-course-labs/app_python
    ```

2. Install the dependencies

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the run.sh script:

    ```bash
    bash run.sh
    ```

2. Visit the page in the browser by this url:

    ```bash
    http://localhost:8080/
    ```

## Docker

This is an instruction for running the application in a docker container

First of all, there is a choice: to build or to pull the image.
After that you will be able to run this image in a docker container

### Build the image

There is a [Dockerfile](/app_python/Dockerfile) in this project. To build the image use this script

```bash
docker build -t moscow-time-app .
```

### Pull the image

Alternative approach: pull the image from the dockerhub

```bash
docker pull justcgh/moscow-time-app:latest
```

### Run the image

If you built the image use this script:

```bash
docker run -p 8080:8080 moscow-time-app
```

If you pulled it:

```bash
docker run -p 8080:8080 justcgh/moscow-time-app:latest
```

## Distroless Docker Version

In this version of the app, I've switched to a **Distroless** Docker image for better performance, security, and efficiency.

### How to Build the Docker Image

1. Ensure you have Docker installed on your machine.
2. Navigate to the `app_python` directory where the `Dockerfile` is located.
3. Run the following command to build the Docker image:

   ```bash
   docker build  -t moscow-time-app-distroless -f distroless.Dockerfile .
   ```

   This will build the Docker image based on the `distroless.Dockerfile`.

### How to Pull the Docker Image

If you want to pull the pre-built image from a Docker Hub, use the following command:

```bash
docker pull justcgh/moscow-time-app-distroless:latest
```

### How to Run the Docker Container

Once the image is built or pulled, you can run the container with this commands.
If you built the image use this script:

```bash
docker run -p 8080:8080 moscow-time-app-distroless
```

If you pulled it:

```bash
docker run -p 8080:8080 justcgh/moscow-time-app-distroless:latest
```

This will start the container and expose the application on port `8080`. You can access the app by navigating to `http://localhost:8080` in your browser.
