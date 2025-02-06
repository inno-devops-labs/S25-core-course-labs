## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (for version control)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/TimurZheksimbaev/S25-core-course-labs/tree/lab1
   cd app_python
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   
   # Windows
   .\venv\Scripts\activate
   
   # Unix/MacOS
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   or 
   pip3 install -r requirements.txt
   ```

4. **Run the Application** (choose on which port to run )
   ```bash
   flask run -g 0.0.0.0 -p 3000
   ```

5. **Open your browser and navigate to `http://localhost:3000`**


<br>

## 🐳 Docker 

### Building the Image

1. Clone the repository:
```bash
git clone https://github.com/TimurZheksimbaev/S25-core-course-labs.git
cd app_python
```

2. Build the Docker image:
```bash
docker build -t timurzheksimbaev/time_web_application:latest .
```

### Pulling the Image

Pull the image from Docker Hub:
```bash
docker pull timurzheksimbaev/time_web_application
```

### Running the Container

1. Run the container:
```bash
docker run -d -p 3000:3000 --name time_web_application timurzheksimbaev/time_web_application
```

2. Access the application:
- Open your browser and go to `http://localhost:3000`

3. Stop the Container
```bash
docker stop time_web_application
```
<br>

# ⚙️ Unit tests

## Test Structure
- **Client Fixture**: Creates test client
- **Homepage Test**: Verifies root endpoint
- **Time Endpoint**: Validates API response
- **Timezone Test**: Confirms Moscow timezone
- **Sync Test**: Checks time progression

## Key Tests

### Homepage (`test_homepage`)
Checks:
- 200 status code
- Correct page title

### Time Endpoint (`test_time_endpoint`) 
Checks:
- API availability
- JSON response format

### Timezone (`test_timezone`)
Checks:
- Correct timezone setting
- pytz configuration

### Time Sync (`test_time_synchronization`)
Checks:
- Time progression
- 1-second interval accuracy
- Response format consistency

## Run Tests
```bash
pytest test_app.py
pytest test_app.py -v    # Verbose
pytest --cov=app tests/  # Coverage
```


# Workflow description
1. Tests job runs first: Python setup, dependencies install, pytest coverage, and Snyk security scan. 
2. After success, Docker job logs in and pushes image to registry.