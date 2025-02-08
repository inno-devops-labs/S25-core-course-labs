# Moscow time API

## Project Overview

The web application that provides the current time in Moscow.

## Technologies used

* FastAPI: web framework
* pytz: Python library for precise time zone handling

## Features

* Current time display: the web application displays the current time in Moscow.
* Dynamic update: the displayed time is updated when the page is refreshed.

## Quick start without Docker

1. Clone the repository:

   ``` bash
   git clone git@github.com:NikaChek/S25-core-course-labs.git
   ```

2. Navigate to the project folder:

   ``` bash
   cd S25-core-course-labs/app_python
   ```

3. Install dependencies:

   ``` bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ``` bash
   uvicorn main:app --reload
   ```

5. Access the application in your browser at <http://127.0.0.1:8000>.

## Docker section

This application has been containerized using Docker to make deployment easier and consistent. Below are the steps to build, pull, and run the Docker container.

### How to Build the Docker Image

1. Clone the repository:

   ``` bash
   git clone git@github.com:NikaChek/S25-core-course-labs.git
   ```

2. Navigate to the project folder:

   ``` bash
   cd S25-core-course-labs/app_python
   ```

3. Build the Docker image

   ``` bash
   docker build -t moscow-time-api .
   ```

### How to Pull the Docker Image

1. Pull the image from Docker Hub

   ``` bash
   docker pull nikachek/moscow-time-api:latest
   ```

### How to Run the Docker Container

1. Start the container

   ``` bash
   docker run -p 8000:8000 moscow-time-api
   ```
   
   If you're running the image from Docker Hub, use the following command:
   
   ``` bash
   docker run -p 8000:8000 nikachek/moscow-time-api:latest
   ```

2. Access the application in your browser at <http://127.0.0.1:8000>.

