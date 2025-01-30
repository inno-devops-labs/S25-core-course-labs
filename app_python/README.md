# Moscow Time Web Application

## Overview
This is a simple web application that displays the current time in Moscow. The application is built using the Flask framework.

## Features
- Displays the current time in Moscow.
- Updates the time upon page refresh.

## Local Installation

### Prerequisites
- Python 3.7+
- Flask
- pytz

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/Muhhhibullo/S25-core-course-labs.git
   cd S25-core-course-labs.git/app_python

2. Usage
   ```sh
   pip install -r requirements.txt
   python3 app.py

## Docker

### Clone and Build the Docker Image
   ```sh
    git clone https://github.com/Muhhhibullo/S25-core-course-labs.git
    cd S25-core-course-labs.git/app_python
    docker build -t lab2 .
   ```
### Pull and Run the Docker Image from Docker Hub
   ```sh
    docker pull deedjei/lab2
    docker run -p 5000:5000 deedjei/lab2