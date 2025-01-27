# Overview

This Python web application displays the current time in Moscow using FastAPI.

## Features
- Displays the current time in Moscow in the format `YYYY-MM-DD HH:MM:SS`
- Handles time zones using the `pytz` library
- Built with FastAPI

## Endpoints
### `GET /msc_time`
Returns the current time in Moscow.

**Response:**
```json
{
  "current_time_in_moscow": "2025-01-25 12:34:56"
}
```

## Local Installation

Follow the steps below to set up the application locally on your machine.

### 1. Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/vtecovsky/S25-core-course-labs
cd app_python
```

### 2. Setup a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```


### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Running
```bash
python main.py
```

## Running in Docker container

### 1. Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/vtecovsky/S25-core-course-labs
cd app_python
```

### 2.1 Build docker image locally

```bash
docker build -t app_python .
```

### 2.2 Pull from the registry

Start by cloning the repository to your local machine:

```bash
docker login
docker pull vtecovsky/app_python:latest
```

### 3.1 Run docker container from local build

Start by cloning the repository to your local machine:

```bash
docker run --rm -p 8000:8000 app_python
```

### 3.2 Run docker container based on the image pulled from the registry

Start by cloning the repository to your local machine:

```bash
docker run --rm -p 8000:8000 vtecovsky/app_python
```

