# Moscow Time Web-Application

This is a simple web application that displays the current time in Moscow. The application is developed using Python and FastAPI framework.

## Table of Contents

- [Table of Contents](#table-of-contents)
  - [Installation](#installation)
    - [Requirements](#requirements)
    - [Manual](#manual)
    - [Docker](#docker)
    - [Distroless Image Version](#distroless-image-version)

## Installation

### Requirements

- Python 3.8 or higher
- `pip` package manager

### Manual

- Clone this branch to your local machine

```bash
git clone git@github.com:saleemasekrea000/S25-core-course-labs.git -b lab1
```

- Navigate to the `app_python` folder

```bash
cd app_python
```

- Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

- Install the required packages

```bash
pip install -r requirements.txt
```

- Run the application

```bash
cd ..
```

```bash
uvicorn app_python.app:app
```

The application will be available at [localhost:8000](http://localhost:8000/)

![First Opening](img/2.png)

## Docker

- To build the image, use the following command:

```bash
docker build -t saleemasekrea/app_python .
```

- To pull the image from the Docker Hub, use the following command:

```bash
docker pull saleemasekrea/app_python:latest
```

- After building or pulling the image, the container can be run with the following command:

```bash
docker run -p 8000:8000 saleemasekrea/app_python
```

The application will be available at [localhost:8000](http://localhost:8000/)

## Distroless Image Version

- To build the image, use the following command:

```bash
docker build -f distroless.Dockerfile -t saleemasekrea/distroless_python_app .
```

- To pull the image from the Docker Hub, use the following command:

```bash
docker pull saleemasekrea/distroless_python_app:latest
```

- After building or pulling the image, the container can be run with the following command:

```bash
docker run -p 8001:8001 saleemasekrea/distroless_python_app 
```
The application will be available at [localhost:8001](http://localhost:8001/)
