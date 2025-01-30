# Moscow Time Web Application

A Flask-based web application that displays the current time in Moscow (MSK) in `HH:MM:SS` format.  
**Containerized with Docker for production-ready deployment.**

## Features
- Real-time Moscow time display
- Auto-refresh on page reload
- Unit tests with mocked time values
- Dockerized with security best practices
- Non-root container execution

---

## Installation

### 1. Local Setup (Development)
```bash
git clone --branch lab1 https://github.com/YehiaSobeh/S25-core-course-labs.git
cd S25-core-course-labs/app_python

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install dependencies and run
pip install -r requirements.txt
python app.py
```
Visit http://localhost:5000.

### 2. Docker Setup (Production)

#### Pull and Run from Docker Hub
```bash
docker pull yehiasobeh/moscow-time-app:latest
docker run -p 5000:5000 yehiasobeh/moscow-time-app
```

#### Build from Source
```bash
docker build -t yehiasobeh/moscow-time-app:latest .
docker run -p 5000:5000 yehiasobeh/moscow-time-app
```

#### Push to Docker Hub (Developers)
```bash
docker login
docker push yehiasobeh/moscow-time-app:latest
```

### 3. Run Tests
```bash
python -m pytest tests/
```

## Project Structure
```
app_python/
├── app.py               # Main application logic
├── Dockerfile           # Docker build instructions
├── DOCKER.md            # Docker best practices
├── tests/               # Unit tests
├── requirements.txt     # Python dependencies
├── .dockerignore        # Docker context exclusions
├── .gitignore           # Git exclusions
└── README.md            # Project documentation
```

## Security Practices
🛡️ **Non-root execution**: Container runs as unprivileged user `myuser`.  
🛡️ **Debug mode disabled**: `FLASK_ENV=production` enforced in Docker.  
🛡️ **Minimal dependencies**: Only essential packages in `requirements.txt`.  
🛡️ **Alpine base image**: Small footprint with security updates.  

## Documentation
- **PYTHON.md**: Python-specific best practices  
- **DOCKER.md**: Docker implementation details  

---

