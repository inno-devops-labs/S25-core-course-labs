# Python Web Application: Current Moscow Timezone

## Overview

This is a simple web application that displays the current time in Moscow. It is built using FastAPI and follows best practices for web development.

## Installation

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd app_python
   ```
2. Create and activate a virtual environment (It is recommended to use 3.11+ Python environment):
    ```sh
    python3 -m venv env
    source env/bin/activate
    ```
3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```sh
    ./run_server.sh
    ```

2. Open your browser and navigate to http://localhost:8000/current-time/moscow to see the current time in Moscow.


## Endpoints

* GET /current-time/{zone}: Displays the current time in the specified zone.


## Testing

* Manually test the application by refreshing the page to ensure the time updates.
* Verify the error handling by entering an invalid time zone.


## Docker

### Build the Docker Image
    ```sh
    docker build -t louayfarah/current_timezone_app:latest .
    ```

### Push the Docker Image to Docker Hub
    ```sh
    docker push louayfarah/current_timezone_app:latest  
    ```

### Pull the Docker Image to Docker Hub
    ```sh
    docker pull louayfarah/current_timezone_app:latest  
    ```

### Run the Docker Image
    ```sh
    docker run -p 8000:8000 -h localhost louayfarah/current_timezone_app:latest
    ```