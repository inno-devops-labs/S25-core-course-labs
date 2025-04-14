# Moscow Time Display

A modern web application that displays the current time in Moscow, Russia, built with FastAPI and Python.

## 🌟 Features

- Real-time display of Moscow time
- RESTful API endpoints
- Type-safe implementation
- Comprehensive error handling
- Containerized deployment with Docker

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher (for local development)
- Docker (for containerized deployment)
- pip (Python package installer, for local development)

### Local Installation

1.Clone the repository:

```bash
git clone git@github.com:SergePolin/S25-core-course-labs.git
cd app_python
```

2.Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3.Install dependencies:

```bash
pip install -r requirements.txt
```

### Running the Application

#### Local Development

1.Start the development server:

```bash
python main.py
```

2.Open your browser and navigate to:

- Web Interface: <http://localhost:8000>
- API Documentation: <http://localhost:8000/docs>

## 🐳 Docker Deployment

### Building the Image

1.Build the Docker image locally:

```bash
docker build -t moscow-time \
  --build-arg BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ') \
  --build-arg VERSION=1.0 \
  .
```

### Running with Docker

1.Run the container with recommended security settings:

```bash
docker run -d \
  --name moscow-time \
  -p 8000:8000 \
  --security-opt no-new-privileges \
  --cap-drop ALL \
  moscow-time
```

2.Access the application:

- Web Interface: <http://localhost:8000>
- API Documentation: <http://localhost:8000/docs>

### Docker Management

#### Health Check

Monitor container health:

```bash
docker inspect --format='{{.State.Health.Status}}' moscow-time
```

#### Stop and Remove

```bash
docker stop moscow-time
docker rm moscow-time
```

#### View Logs

```bash
docker logs moscow-time
```

For more detailed Docker implementation information, see [DOCKER.md](DOCKER.md).

## 🛠️ Technical Stack

- **Backend Framework**: FastAPI
- **Template Engine**: Jinja2
- **Time Management**: pytz
- **Configuration**: pydantic-settings
- **Development Server**: uvicorn
- **Container Runtime**: Docker

## 📚 API Documentation

### Endpoints

1. `GET /`
   - Renders the main page with Moscow time
   - Response: HTML

2. `GET /get_time`
   - Returns current Moscow time in JSON format
   - Response:

     ```json
     {
       "moscow_time": "HH:MM:SS",
       "current_time": "YYYY-MM-DD HH:MM:SS TZ"
     }
     ```

## 📦 Project Structure

```bash
app_python/
├── main.py              # Main application file
├── config.py            # Configuration settings
├── requirements.txt     # Project dependencies
├── Dockerfile          # Docker configuration
├── .dockerignore       # Docker ignore rules
├── .env                # Environment variables
├── README.md           # Project documentation
├── DOCKER.md           # Docker best practices
├── PYTHON.md           # Python best practices
├── templates/          # HTML templates
│   └── index.html     # Main page template
└── .gitignore         # Git ignore rules
```

## 👥 Author

- Sergei Polin

## 🙏 Acknowledgments

- FastAPI team for the excellent framework
- Python community for the amazing ecosystem
- Docker team for container runtime
