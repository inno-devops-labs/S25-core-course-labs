# 📌 Moscow Time Web Application 🕒

## 🌍 Overview
This is a **Flask-based web application** that displays the **current time in Moscow**.  
The time **automatically updates every second** to ensure real-time accuracy.

## 📦 Features
✅ Displays real-time **Moscow time (MSK)**  
✅ **Auto-refresh** every second using JavaScript  
✅ Uses **Flask framework** for a lightweight and efficient backend  
✅ **Well-structured code** following best practices  
✅ Includes **unit tests** to ensure reliability  

## 🚀 Local Installation
Follow these steps to run the application on your local machine:

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/anasalatasiuni/S25-core-course-labs.git
cd app_python
```
### 2️⃣ Install Dependencies
Ensure you have python3 installed, then run:
```bash
pip install -r requirements.txt
```
### 3️⃣ Run the Application
```bash
python app.py
```

Visit: http://127.0.0.1:5000/ in your browser.

## 🛠 Requirements
- Python 3.x
- Flask
- pytz (for time zone handling)


## 📦 Running with Docker

This section explains how to build, pull, and run the application using Docker.
### 🔨 How to Build the Docker Image?
If you want to build the image locally, run:
```bash
docker build -t moscow-time-app .
```
This will create a Docker image named moscow-time-app.
### 🔽 How to Pull from Docker Hub?
The image is available on Docker Hub, you can pull it directly using:
```bash
docker pull anasalatasi/moscow-time-app:latest
```
### 🚀 How to Run the Container?
Once the image is built or pulled, start the container by running:
```bash
docker run -p 5000:5000 moscow-time-app
```
Then visit: http://localhost:5000


---

## 🧪 Unit Tests

This project includes **unit tests** to ensure the core functionality of the Moscow time web app works correctly.

### How to Run the Tests

1. **Clone the Repository**:
```bash
git clone https://github.com/anasalatasiuni/S25-core-course-labs.git
cd app_python
```

2. **Install Dependencies**:
```bash
pip install -r requirements.txt
```

3. **Run Unit Tests**:
```bash
python -m unittest test_app.py
```

This will run all the unit tests and show the results in the terminal.

### Test Coverage:
- **Home page load**  
- **Moscow time format**  
- **Correct Moscow timezone**

Ensure your tests pass successfully to confirm the app is functioning as expected.

---

## 🏗 CI Workflow

[![CI for Moscow time app](https://github.com/anasalatasiuni/S25-core-course-labs/actions/workflows/python-app-ci.yml/badge.svg?branch=lab3)](https://github.com/anasalatasiuni/S25-core-course-labs/actions/workflows/python-app-ci.yml)

### How CI Works for Moscow Time Web Application

This project uses **GitHub Actions** for Continuous Integration (CI). The CI pipeline consists of the following stages:

### 1️⃣ **Test Stage**
This stage is responsible for testing the code. It ensures the application runs as expected.

- **Runs on**: `ubuntu-latest`
- **Steps**:
  1. **Checkout Code**: Pulls the latest code from the repository.
  2. **Set up Python Environment**: Configures Python 3.10.
  3. **Install Dependencies**: Installs all the required dependencies using `pip`.
  4. **Run Linter**: Runs `flake8` to check for code quality issues and enforce style guides.
  5. **Run Tests**: Uses `unittest` to execute the test suite and check if all the tests pass.

### 2️⃣ **Docker Stage**
This stage builds and pushes the Docker image to **Docker Hub** after successful tests.

- **Runs on**: `ubuntu-latest`
- **Steps**:
  1. **Login to Docker Hub**: Authenticates using your Docker Hub credentials stored as GitHub secrets.
  2. **Build Docker Image**: Builds the Docker image using the `Dockerfile` in the `app_python` directory.
  3. **Push Docker Image**: Pushes the Docker image to **Docker Hub** under your Docker Hub username with the tag `moscow-time-app`.

### CI Workflow File

The CI pipeline is defined in the GitHub Actions workflow file: **.github/workflows/python-app-ci.yml**.

---
