## Moscow Time Web Application

[![CI Pipeline](https://github.com/whatislav/S25-core-course-labs/actions/workflows/master.yml/badge.svg)]

### Overview
This Flask-based web application displays the current time in Moscow.

### Installation

1. **Clone the Repository:**
   ```sh
   git clone <repository-url>
   cd app_python
   ```
2. **Create a Virtual Environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```
3. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the Application:**
   ```sh
   python app.py
   ```
5. **Access the Web App:**
   - Main page: `http://127.0.0.1:5000/`
   - Visit counter: `http://127.0.0.1:5000/visits`
   - Prometheus metrics: `http://127.0.0.1:5000/metrics`

### File Structure
- `app.py` - Main entry point of the application.
- `services/get_time_service.py` - Service class handling time retrieval.
- `config.py` - Stores configuration settings (timezone).
- `templates/current_time.html` - HTML template for displaying time.
- `data/visits.txt` - Persistent storage for visit counter.

### Docker Support

#### How to Build the Docker Image:
```sh
docker build -t moscow-time-app .
```

#### How to Run the Container:
```sh
docker run -p 5000:5000 moscow-time-app
```

#### How to Pull and Run from Docker Hub:
```sh
docker pull whatislav/moscow-time-app:1.0
docker run -p 5000:5000 whatislav/moscow-time-app:1.0
```

### Persistence
The application maintains a visit counter that persists across container restarts using a volume mount. The counter is stored in `/data/visits.txt` inside the container, which is mapped to `./data/visits.txt` on the host.

### Unit Tests

This application includes comprehensive unit tests to ensure its reliability and correctness. The tests are written using Python's `unittest` framework and cover both business logic and Flask routes.

#### Running Unit Tests
To execute the unit tests, follow these steps:

1. Navigate to the project directory:
   ```sh
   cd app_python
   ```

2. Activate the virtual environment (if not already active):
   ```sh
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Run the tests:
   ```sh
   python -m unittest discover tests
   ```

### Continuous Integration (CI) Workflow

This project uses GitHub Actions for continuous integration (CI) and deployment. The CI workflow automates the process of building, testing, and deploying the application to Docker Hub.

#### CI Workflow Details

1. **Trigger**: 
   - The workflow is triggered on pushes to the `master` branch or when pull requests are opened against the `master` branch.

2. **Workflow File**:
   - The CI configuration is defined in `.github/workflows/master.yml`.

3. **Working Directory**:
   - Steps are executed in the `app_python` directory.

4. **Steps in the Workflow**:
   - **Dependencies**: Installs the project dependencies using `pip` in the `app_python` directory.
   - **Linter**: Runs a linter (`flake8`) to ensure code quality in the `app_python` directory.
   - **Tests**: Executes unit tests to validate functionality in the `app_python/tests` directory.
   - **Docker Build & Push**: Builds the Docker image from the `app_python/Dockerfile` and pushes it to Docker Hub.

5. **Environment-Specific Secrets**:
   - The Docker login step uses secrets stored in the "prod" environment of the GitHub repository.
   - These secrets include:
     - **`DOCKER_USERNAME`**: Docker Hub username.
     - **`DOCKER_PASSWORD`**: Docker Hub personal access token.

6. **Docker Integration**:
   - Logs in to Docker Hub using credentials stored in the "prod" environment.
   - Builds the Docker image using the `app_python/Dockerfile`.
   - Pushes the image to Docker Hub with the tag `latest`.