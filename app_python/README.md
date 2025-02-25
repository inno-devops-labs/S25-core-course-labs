Features
FastAPI-based API to get the current Moscow time.
Dockerized for easy deployment.
Automated testing with Pytest.
CI/CD pipeline using GitHub Actions.

Unit Tests
API Endpoints: Verifying correct responses from the /moscow-time endpoint.
Error Handling: Ensuring the application gracefully handles errors.
Business Logic: Testing time conversion and formatting logic.

Run Tests
pip install -r requirements.txt
pytest -v

To build and run the Docker container locally:
docker build -t yourusername/moscow-time:latest .
docker run -p 8000:8000 yourusername/moscow-time:latest
