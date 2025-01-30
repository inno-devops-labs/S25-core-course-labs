# Python Web Application

## Overview

This web application displays the current time in Moscow. The app is written in Python and built using Flask .

## Installation

### Prerequisites

- Python 3.x is installed.
- All requirements from requirements.txt are installed.

### Steps

1. Clone the repository and go to `app_python` folder.
2. Install the dependencies from requirements.txt file:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python app.py
   ```

4. Open the app on link:
`http://127.0.0.1:5000/`
  
## Docker

### Build

To build the Docker image:

```bash
  docker build --no-cache -t app_python:latest .
```

### Pull

To pull the Docker image:

```bash
  docker pull ilsiia/app_python:latest  
```

### Run

To run the Docker image:

```bash
  docker run -p 5000:5000 ilsiia/app_python:latest
```

Or if port 5000 on your machine is in use, replace the port 5000 with the free port like that:

```bash
  docker run -p <free port>:5000 ilsiia/app_python:latest
```

## Distroless Image Version

### Pull distroless image

To pull the docker image:

```bash
  docker pull ilsiia/python-app:distroless
```

### Run distroless image

To run the docker image:

```bash
  docker run --rm -p 5000:5000 python-app:distroless
```

Or if you have somathing runnong in port 5000 on your machine change port with the free one:

```bash
  docker run --rm -p <free_port>:5000 python-app:distroless
```

### Build distroless image

To build the image:

```bash
  docker build -t python-app:distroless -f distroless.Dockerfile .
```


