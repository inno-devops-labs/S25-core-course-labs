# Python Web Application - Current Time in Moscow

## Overview

This is a simple Python web application that displays the current time in Moscow. It is built using the Flask framework and demonstrates best practices in web development.

## Features

- Displays the current time in Moscow.
- Animated cloud background to simulate a sky.

## Requirements

- Python 3.x
- Flask
- pytz

## Local Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd app_python
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Open your browser** and navigate to `http://127.0.0.1:5000/`.

## Docker Support

This application can also be run in a Docker container. Below are the instructions for building, pulling, and running the Docker image.

### Building the Docker Image

To build the Docker image for this application, follow these steps:

1. **Navigate to the app_python directory**:
   ```bash
   cd path/to/your/app_python
   ```

2. **Build the Docker image**:

   ```bash
   docker build -t your_username/app_python:latest .
   ```

   Replace `your_username` with your actual Docker Hub username.

### Pulling the Docker Image

If you want to pull the pre-built image from Docker Hub, use the following command:

```bash
docker pull chr1st1na/app_python:latest 
   ```

### Running the Docker Container

To run the Docker container, execute the following command:

```
docker run -p 5000:5000 chr1st1na/app_python:latest
```

- This command maps port 5000 on your local machine to port 5000 in the Docker container.

### Accessing the Application

After running the container, open your web browser and navigate to `http://127.0.0.1:5000/` to see the application in action.

## Conclusion

This README provides an overview of the application, its features, and instructions for both local installation and Docker usage. For more details on Docker best practices, refer to the [DOCKER.md](DOCKER.md) file.