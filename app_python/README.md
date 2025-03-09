# Moscow Time Web Application (Python)

## Overview
A simple web application built with Flask that displays the current time in Moscow. The application features a clean, modern UI and automatically updates the time when the page is refreshed.

## Features
- Displays current Moscow time and date
- Clean and responsive user interface
- Automatic time updates on page refresh
- Visit counter with persistence
- `/visits` endpoint to display the number of visits

## Local Installation

1. Clone the repository
2. Navigate to the `app_python` directory
3. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Unix/macOS
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the application:
   ```bash
   python app.py
   ```
6. Open your browser and visit `http://localhost:5000`

## Docker Support

### Standard Docker Image

#### Building the Image
```bash
docker build -t your-dockerhub-username/moscow-time-python:latest .
```

#### Pulling from Docker Hub
```bash
docker pull your-dockerhub-username/moscow-time-python:latest
```

#### Running the Container
```bash
docker run -d -p 5000:5000 -v $(pwd)/visits:/app/visits your-dockerhub-username/moscow-time-python:latest
```

### Distroless Image Version

The application is also available as a distroless image for enhanced security and smaller size.

#### Building the Distroless Image
```bash
docker build -t your-dockerhub-username/moscow-time-python:distroless -f distroless.Dockerfile .
```

#### Pulling the Distroless Image
```bash
docker pull your-dockerhub-username/moscow-time-python:distroless
```

#### Running the Distroless Container
```bash
docker run -d -p 5000:5000 -v $(pwd)/visits:/app/visits your-dockerhub-username/moscow-time-python:distroless
```

### Image Comparison
- Standard Image (Alpine-based): ~80MB
- Distroless Image: ~73MB

The distroless version offers enhanced security through:
- Minimal attack surface
- No shell access
- No package manager
- Runs as non-root user

Choose the distroless version for production deployments where security is a priority.

## Technologies Used
- Python 3.x
- Flask - lightweight web framework
- pytz - timezone handling library
- File-based persistence for visit counter

## Best Practices Applied
- Clean code structure with proper separation of concerns
- Modern UI/UX design principles
- Proper timezone handling using pytz
- Requirements management with requirements.txt
- Comprehensive documentation
