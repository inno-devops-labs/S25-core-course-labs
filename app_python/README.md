# Moscow Time Web Application

Web application that returns current Moscow time in JSON format.

## Features

- Returns JSON response with timezone and current time in human-readable and machine-readable ISO format
- Auto-updating current time on each request
- PEP8 compliant code with `Black` formatter
- Lightweight local installation

## Installation

### Prerequisites

- Python 3.9+
- `pip` package manager

### Local Setup

1. Clone the repository:

```bash
git clone https://github.com/nikitashlyahktin/S25-core-course-labs
cd S25-core-course-labs/app_python
```

1. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Start the development server:

```bash
python3 app.py
```

1. Access the API endpoint with a web browser: `http://localhost:5000`

## Docker

Docker helps to run the application without managing application dependencies by yourself.

You can either build your own docker image from `Dockerfile` or use prebuilt image from docker hub.
Then you can run the container and use the app.

### Docker Prerequisites

- Docker engine (e.g. Docker Desktop or Colima) installed and running

### Build Image

Use the following command in `app_python` directory to build the image from `Dockerfile`:

```bash
docker build -t moscow-time-app .
```

### Pull Prebuilt Image

Use the following command to pull prebuilt image from docker hub:

```bash
docker pull nshlyakhtin/devops:lab2
```

### Run Container

```bash
docker run -p 5001:5000 moscow-time-app
# or for prebuilt image:
docker run -p 5001:5000 nshlyakhtin/devops:lab2
```

## Distroless Image Version

You can use smaller and more secure distroless docker image for running the application

### Build Distroless Image

Use the following command in `app_python` directory to build the image from `distroless.Dockerfile`:

```bash
docker build -f distroless.Dockerfile -t moscow-time-app-distroless .
```

### Pull Prebuilt Distroless Image

Use the following command to pull prebuilt image from docker hub:

```bash
docker pull nshlyakhtin/devops:lab2_app_python_distroless
```

### Run Container With Distroless Image

```bash
docker run -p 5001:5000 moscow-time-app-distroless
# or for prebuilt image:
docker run -p 5001:5000 nshlyakhtin/devops:lab2_app_python_distroless
```

## Example Response

```json
{
  "current_time": "2025-01-26 13:53:55",
  "timezone": "Europe/Moscow"
}
```

## Project Structure

```txt
app_python/
├── app.py            # Main web application code
├── requirements.txt  # Dependency list
├── PYTHON.md         # Technical documentation
└── README.md         # User documentation
```

## Documentation

See [PYTHON.md](PYTHON.md) for technical implementation details.
