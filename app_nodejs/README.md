# Node.js Web Application

## Overview

This is a simple web application that displays the current time in Moscow. It is built using Node.js and Express.

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd app_nodejs
    ```

2. Install the dependencies:
    ```sh
    npm install
    ```


## Usage

1. Run the application:
    ```sh
    npm start
    ```

2. Open your browser and navigate to http://localhost:3000 to see the current time in Moscow.


## Endpoints

* GET /: Displays the current time in Moscow.


## Testing

* Manually test the application by refreshing the page to ensure the time updates.
* Verify the error handling by navigating to a non-existent page.


## Docker

### Build the Docker Image
    ```sh
    docker build -t louayfarah/current_timezone_app_nodejs:latest .
    ```

### Push the Docker Image to Docker Hub
    ```sh
    docker push louayfarah/current_timezone_app_nodejs:latest
    ```

### Pull the Docker Image to Docker Hub
    ```sh
    docker pull louayfarah/current_timezone_app_nodejs:latest
    ```

### Run the Docker Image
    ```sh
    docker run -p 3000:3000 -h localhost louayfarah/current_timezone_app_nodejs:latest
    ```