# Python web application: Moscow Time

## Overview

This web application displays the current time in Moscow, Russia.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package manager)

## Installation

**1. Clone the repository:**
*git clone <https://github.com/zDragonLORD1010/S25-core-course-labs.git>*

**2. Navigate to the project folder:**
*cd /your_path/S25-core-course-labs/app_python*

**3. Install dependencies:**
*pip install -r requirements.txt*

**4. Running the application**

- Start the Flask development server:
*python app.py*
- Open your browser:
Navigate to http://127.0.0.1:5000/ to view the application.
- Check the output:
You should see the current time in Moscow displayed on the page.

## Docker

### Steps to build, push, and run Docker

- **Build the Docker Image:**
_docker build -t moscow-time-app:1.0 ._

- **Run Docker locally:**
_docker run -p 5000:5000 moscow-time-app:1.0_

### Push to Docker Hub (put your dockerhub username instead of your_username)

- **Tag the image:**
*docker tag moscow-time-app:1.0 your_username/moscow-time-app:1.*

- **Push the image:**
*docker push <username>/moscow-time-app:1.0*

### Pull and run Docker

- *docker pull your_username/moscow-time-app:1.0*
- *docker run -p 5000:5000 your_username/moscow-time-app:1.0*