# Python Web Application - Moscow Time Display

## Overview

This Python web application displays the current time in Moscow. It updates every time the page is refreshed, ensuring the displayed time is always current.

## Features

- Displays current date and time in Moscow timezone.
- Simple application using Flask.

## Prerequisites

- Python 3.x
- pip package manager

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/MrTonyNeon/S25-core-course-labs -b lab1
   cd app_python
   ```

2. **Set Up Virtual Environment (Optional but Recommended):**

   ```bash
   python3 -m venv venv
   venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Application:**

   ```bash
   python app.py
   ```

2. **Access in Browser:**

   - Navigate to `http://localhost:8080/`

## Project Structure

- `app.py` - Main application file.
- `requirements.txt` - List of dependencies.
- `PYTHON.md` - Documentation on framework choice and best practices.
- `README.md` - Project documentation.
- `.gitignore` - Git ignore file.

## .gitignore

A clean `.gitignore` file is maintained to exclude:

- `venv/` - Virtual environment files.
- `__pycache__/` - Python cache files.

---

## Docker

The application is containerized using Docker for ease of deployment and consistency across environments.

### 5.1. Containerization process

This section provides instructions on how to containerize the application using Docker. It covers how to build the Docker image locally, how to pull it from a Docker registry (if available), and how to run the Docker container.

### 5.2. How to build?

`docker build -t achulakov/app_python:v1.0 .`

### 5.3.  How to pull?

`docker pull achulakov/app_python:v1.0`

### 5.4. How to run?

`cd .\app_python\`
`docker run -p 8080:8080 achulakov/app_python:v1.0`
