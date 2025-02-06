# Moscow Time Web Application

A simple and elegant web application that displays the current time in Moscow, built with Python and Flask.

## Overview

This web application provides real-time Moscow time display with a clean, responsive interface. Built as part of the DevOps Engineering course Lab 1, it demonstrates Python web development best practices, proper timezone handling, and comprehensive testing.

## Features

- Real-time Moscow timezone display using pytz
- Clean, minimalist user interface
- Automatic time updates on page refresh
- Comprehensive test coverage with pytest
- Well-documented codebase following PEP standards
- Containerized deployment ready

## Technologies Used

- **Backend Framework**: Flask 3.0.2
- **Python Version**: 3.8+
- **Time Handling**: pytz 2024.1
- **Testing**: pytest 8.1.1
- **Frontend**: HTML5/CSS3
- **Code Quality**: pylint, Black formatter
- **Container**: Docker

## Docker

The application is available as a Docker container on Docker Hub:
[eleanorpi/moscow-time-app](https://hub.docker.com/repository/docker/eleanorpi/moscow-time-app/general)

### Docker Features
- Multi-stage build for optimized image size
- Non-root user execution for security
- Health checks for monitoring
- Alpine-based for minimal footprint
- Proper security practices

### Building Locally
```bash
# Clone the repository
git clone https://github.com/elpicode/S25-core-course-labs.git
cd app_python

# Build the image
docker build -t eleanorpi/moscow-time-app .
```

### Running from Docker Hub
```bash
# Pull the image
docker pull eleanorpi/moscow-time-app

# Run the container
docker run -d -p 5000:5000 --name moscow-time eleanorpi/moscow-time-app

# Check container health
docker inspect --format='{{json .State.Health}}' moscow-time

# View logs
docker logs moscow-time
```

### Accessing the Application
The application will be available at:
```
http://localhost:5000
```

For detailed information about Docker configuration, best practices, and security measures, see [DOCKER.md](DOCKER.md).

## Manual Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/elpicode/S25-core-course-labs.git
   cd app_python
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   .\venv\Scripts\activate
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   flask run --host=0.0.0.0 --port=5000
   ```

5. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```
