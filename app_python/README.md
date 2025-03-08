[![CI Workflow](https://github.com/mngcndl/S25-core-course-labs/actions/workflows/ci.yml/badge.svg)](https://github.com/mngcndl/S25-core-course-labs/actions/workflows/ci.yml)

# Instructrions to run the project

## Requirements:

- Python 3.9
- Flask
- pytz

## To run the web application on your machine, follow the steps:

1. Clone the repository:

```bash
    git clone https://github.com/mngcndl/S25-core-course-labs
    cd S25-core-course-labs/app_python
```

2. Create virtual environment:

```bash
    python -m venv venv
    source venv/bin/activate # for MacOS and Linux
    venv\Scripts\activate # for Windows
```

3. Install dependencies locally using the command:

```bash
    pip install -r requirements.txt
```

4. Run the application:

```bash
    python app.py
```

5. Go to your web browser and open the url http://127.0.0.1:5000

## To run the web application on your machine using Docker, follow the steps:

If you already have all the files locally, build the image:

```bash
    docker build -t mangocandle/app_python:latest .
```

OR

1. Pull the image:

```bash
    docker pull mangocandle/app_python:latest .
```

2. Run the image:

```bash
    docker run -p 5000:5000 mangocandle/app_python:latest
```

## Unit tests:

For running tests, run the command:

```bash
pytest tests/
```

## CI Workflow

This project uses GitHub Actions for Continuous Integration (CI). The CI workflow includes the following steps:

1. **Dependencies**: The workflow installs all the required dependencies from `requirements.txt`.
2. **Linter**: It runs `flake8` to ensure the code follows the PEP8 style guidelines.
3. **Tests**: The workflow runs unit tests using `pytest`.
4. **Docker**: The workflow builds a Docker image and pushes it to Docker Hub for deployment.

### How to Trigger the CI Workflow

The CI workflow is triggered automatically when changes are pushed to the `lab3`.

To check the status of the CI workflow, visit the "Actions" tab in the GitHub repository.

### Docker Image

Once the workflow completes, the Docker image is built and pushed to Docker Hub under the repository name `mangocandle/app_python:latest`.

You can pull the image using the following command:

```bash
docker pull mangocandle/app_python:latest
```

Updates:

- The application now implements a visit counter.
- A new endpoint `/visits` that can be accessed via "curl http://localhost:5001/visits" command displays the stored count.
- When you access the root endpoint (`/`), the application adds 1 to the counter and writes the result to the `visits` file.
- When using Docker or docker-compose, a volume is used to persist the `visits` file.

[CI Best Practices](./CI.md)
