# Python Web Application: Current Date in Moscow

## Overview
This web application built with **FastAPI** to display the current formatted date and time in Moscow. The application dynamically updates the date whenever the page is refreshed.

## Features
- Displays the current date in Moscow (`dd.mm.YYYY HH:MM:SS` format).
- Dynamically updates on page refresh.
- Lightweight and high-performance using **FastAPI**.
- Clean HTML design.

## Installation

### Prerequisites
- Python 3.8 or later
- pip (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/creepydanunity/S25-core-course-labs.git
   cd app_python

2. Install dependencies:
    ```bash
    pip install -r requirements.txt

3. Run the application:
    ```bash
    uvicorn main:app --reload

4. Access at:
    http://127.0.0.1:8000

## Docker

### Build the container
```sh
docker build -t fastapi-mt .
```

### Run the container
```sh
docker run -p 8000:8000 fastapi-mt
```

### Run via Docker Hub
```sh
docker pull iucd/fastapi-mt:latest
docker run -p 8000:8000 iucd/fastapi-mt
```

## Distroless Image Version

### Build the container
```sh
docker build -t fastapi-mt:distroless -f distroless.Dockerfile .
```

### Run the container
```sh
docker run -p 8000:8000 fastapi-mt:distroless
```

### Run via Docker Hub
```sh
docker pull iucd/fastapi-mt:distroless
docker run -p 8000:8000 iucd/fastapi-mt:distroless
```