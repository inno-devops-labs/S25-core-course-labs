# Python Web Application - Current Time in Moscow

## Overview
This is a simple Python web application on the Flask displays the current time in Moscow.
It uses the `pytz` library to handle the time zone for Moscow.

## Features
- Displays the current time in the Moscow timezone.
- Time updates automatically on page refresh.

## Requirements
- Python
- Flask
- pytz

### Running the Application

```bash
pip install -r requirements.txt
python lab1.py
```

# Docker

## The application automatically installs all dependencies and runs inside the container.

## How to build?

```bash
docker build -t lab2:latest .
```

## How to run?

```bash
docker run -d -p 5000:5000 lab2
```
## How to pull?

```bash
docker pull ksenon9/lab2:latest
docker run -p 5000:5000 ksenon9/lab2:latest
```

