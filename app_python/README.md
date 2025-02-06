# Moscow Time Web Application

This is a Python web application built with **FastAPI** that displays the current time in Moscow. The application is designed to follow best practices described in this [repo](https://github.com/zhanymkanov/fastapi-best-practices). Read about it in `PYTHON.md`.

---

## Project Structure

```
moscow_time_app/
├── src/
│   └── main.py              # FastAPI application code
├── tests/
│   └── test_main.py         # Unit tests for the application
├── .dockerignore            # List of files that ignores by docker
├── .gitignore               # List of files that ignores by git
├── DOCKER.md                # Docker documentation
├── Dockerfile               # Configuration file for docker
├── PYTHON.md                # Justification for my salary as a Python developer :-)
├── README.md                # Project documentation
└── requirements.txt         # Project dependencies
```

---

## Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/KonstantinPetrovichQWERTY/IU-DevOps-S25.git
   cd moscow_time_app
   ```

2. **Create a virtual environment**:

   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment**:
   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

4. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

---

## Running the Application

To start the FastAPI application, run the following command:

```bash
uvicorn app_python.src.main:app --reload
```

- The `--reload` flag enables auto-reloading, so the server restarts whenever you make changes to the code.
- Open your browser and navigate to `http://127.0.0.1:8000/get_moscow_time`. You should see the current time in Moscow displayed in JSON format.
- To see the SwaggerUI documentation navigate to `http://127.0.0.1:8000/docs`.

---

## Running the Unit Tests

First of all, install required dependencies to your virtual environment (venv):

```bash
pip install pytest requests
```

To start the tests, run the following command in `app_python` directory:

```bash
pytest tests/test_main.py -v 
```

If everything is correct, the test should pass:

```bash
============================= test session starts =============================
collected 4 items

tests/test_main.py::test_get_moscow_time PASSED                          [ 25%]
tests/test_main.py::test_moscow_time_format PASSED                       [ 50%]
tests/test_main.py::test_moscow_time_updates PASSED                      [ 75%]
tests/test_main.py::test_moscow_time_timezone PASSED                     [100%]

============================== 4 passed in 2.05s ==============================
```

---

## Docker

Or you can simply use docker to run and build the application:

1. **How to build?**
To build the Docker image locally, navigate to the project directory (app_python) and run the following command. This will create a Docker image tagged as `moscow-time-app`.

   ```bash
   docker build -t moscow-time-app .
   ```

2. **How to run?**
To run the Docker container, use the following command. The `-d` flag runs the container in detached mode, and `-p 8000:8000` maps port 8000 on your local machine to port 8000 in the container.

   ```bash
   docker run -d -p 8000:8000 moscow-time-app:1.0
   ```

3. **How to pull?**
You can pull docker image from DockerHub [repo](https://hub.docker.com/repository/docker/konstantinqwertin/moscow-time-app/general).

   ```bash
   docker pull konstantinqwertin/moscow-time-app:1.0
   docker run -d -p 8000:8000 konstantinqwertin/moscow-time-app:1.0
   ```

---

## Testing the Application

To run the unit tests, use the following command:

```bash
pytest
```

### Test Cases

1. **Test Endpoint Response**:
   - Verifies that the `/get_moscow_time` endpoint returns a valid response (contain `'moscow_time'` key) with a status code of `200`.

2. **Test Time Format**:
   - Ensures that the returned time is in the correct `YYYY-MM-DD HH:MM:SS` format.

3. **Test Time Updates**:
   - Confirms that the displayed time updates between requests.

---

## Dependencies

All dependencies you can find in `requirements.txt`.

---

## Continuous Integration (CI) with GitHub Actions

This project uses GitHub Actions for Continuous Integration (CI) to automate building, testing, and linting.

### CI Workflow Overview

The CI pipeline performs the following steps:

- **Install Dependencies:**
   Installs Python dependencies from `requirements.txt`.
- **Run Linter:**
   Checks code style and formatting using `flake8`.
- **Run Tests:**
   Executes unit tests using pytest.
- **Build and Push Docker Image:**
   Builds a Docker image and pushes it to Docker Hub.

### Setting Up the CI Pipeline

**Docker Hub Credentials:**

To push Docker images, add your Docker Hub credentials as GitHub Secrets:

- `DOCKER_HUB_USERNAME`: Your Docker Hub username.

- `DOCKER_HUB_TOKEN`: Your Docker Hub access token.

These secrets are used in the `docker-build-and-push` job.

### Workflow File

The CI workflow is defined in `.github/workflows/ci.yml`.

### Running the Pipeline

The pipeline runs automatically on every push and pull_request to the master branch.

You can also manually trigger the workflow from the Actions tab in your GitHub repository.

---
