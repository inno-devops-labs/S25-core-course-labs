# Python Web Application: Moscow Time

## Overview

This web application, built with Flask, displays the current time in Moscow. The time updates dynamically every time the
page is refreshed.

## Features

- Displays the current time in Moscow (Europe/Moscow timezone).
- Lightweight and easy to run locally.
- Built using best practices and follows coding standards.

## Requirements

- Python 3.8+
- Flask
- pytz

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Milanaaaa/S25-core-course-labs.git
   cd S25-core-course-labs/app_python
   ```

2. Create virtual environment

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install requirements

   ```bash
   pip install -r requirements.txt
   ```

4. Run the app

   ```bash
   python app.py
   ```

## Docker

### How to build?

   ```bash
   cd S25-core-course-labs/app_python
   docker build -t python-web-app .
   ```

### How to pull?

   ```bash
   docker pull milanamilana/python-web-app:latest
   ```

### How to run?

   ```bash
   docker run -p 5000:5000 milanamilana/python-web-app:latest
   ```

## Distroless Image Version

### How to build? (Distroless)

   ```bash
   cd S25-core-course-labs/app_python
   docker build -t python-distroless-web-app -f distroless.Dockerfile .
   ```

### How to pull? (Distroless)

   ```bash
   docker pull milanamilana/python-distroless-web-app:latest
   ```

### How to run? (Distroless)

   ```bash
   docker run -p 5000:5000 milanamilana/python-distroless-web-app:latest
   ```
