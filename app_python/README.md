[![CI Pipeline](https://github.com/emiliogain/S25-core-course-labs/actions/workflows/ci.yaml/badge.svg?branch=master)](https://github.com/emiliogain/S25-core-course-labs/actions/workflows/ci.yaml)
# Python Web Application

## Overview
This Python web application displays the current time in Moscow using Flask.

## New Features
- Visit counter persistence between restarts
- New endpoint `/visits` to show total visits
- Data stored in `visits.txt` on host machine

## Endpoints
- `/` - Shows current Moscow time and total visits (increments counter)
- `/visits` - Shows total visits without incrementing


## Local Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/emiliogain/S25-core-course-labs.git
   cd S25-core-course-labs
   git checkout lab1
   cd app_python
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the application:
   ```sh
   python main.py
   ```
4. Open `http://127.0.0.1:5000/` in your browser.

## 🐳 Running with Docker

### How to Build?
```sh
cd app_python
docker build -t  my-python-app .
```

### How to Pull?
```sh
docker pull emiliogain/my-python-app:latest
```

How to Run?
```sh
docker run -p 8080:5000 emiliogain/my-python-app
```

## Unit Tests

This project includes unit tests to verify the correctness and reliability of the application.

### **Running Unit Tests**
Run the following command to execute the tests:
```sh
pytest
```

### **What is Tested?**  

- **Status Code**: Homepage (`/`) returns **200 OK**.  
- **Template Rendering**: `index.html` loads correctly.  
- **Time Presence**: `current_time` exists in the template.  
- **Time Format**: Time follows **HH:MM:SS** format.  
- **Moscow Time**: Displays the correct time for **Europe/Moscow**.


## CI Pipeline

This project uses GitHub Actions for continuous integration (CI).
The CI pipeline is triggered on `push` and `pull_request` events to the `master` and `lab3` branches and 
the changes are in the `app_python/` directory or the `.github/workflows/ci.yaml` file.

### Steps in the CI Pipeline:
1. **Install Dependencies**: Installs the required dependencies from `app_python/requirements.txt`.
2. **Run Linter (Flake8)**: Lints the code in the project to ensure style consistency.
3. **Run Tests (Pytest)**: Executes the tests defined in the project using Pytest.

### Docker Integration:
The pipeline includes steps to build the Docker image using the `Dockerfile` located in the `app_python/` directory and push the image to Docker Hub.
This is done after successful tests to ensure the image is up-to-date with the latest code.
The Docker image is tagged with the repository’s Docker Hub username and `latest` tag.

For Docker integration, make sure the following secrets are set in the repository:
- `DOCKER_USERNAME`
- `DOCKER_PASSWORD`
