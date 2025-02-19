# 🌟 Moscow Time Web Application

![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![Flask Version](https://img.shields.io/badge/Flask-2.2%2B-green.svg)
![License](https://img.shields.io/badge/License-MIT-orange.svg)
![CI/CD Pipeline](https://github.com/Azaki-san/S25-core-course-labs/actions/workflows/app_python_ci.yml/badge.svg)

## 🖥️ Overview

This is a simple yet visually appealing web application that displays the current **Moscow Time (MSK)**. Built using Python's **Flask** framework, it refreshes the displayed time each time the page is reloaded. With an elegant design and clean code structure, this app is a perfect example of how to combine functionality with style.

---

## ✨ Features

- 🌍 **Real-Time Moscow Time**: Displays the current time in Moscow.
- 🎨 **Elegant Design**: Styled with CSS for a modern and polished appearance.
- ⚡ **Lightweight**: Built using Flask, making it fast and easy to deploy.
- 🛠️ **Simple Setup**: Easily install and run the application locally.

---

## ⚙️ Local Installation

Follow these steps to set up and run the application locally:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Azaki-san/S25-core-course-labs.git
   cd S25-core-course-labs/app_python

2. **Set Up a Virtual Environment (Optional)**
   ```bash
   python -m venv venv
   source venv/bin/activate     # On Linux/Mac
   .\venv\Scripts\activate      # On Windows
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

4. **Run the Application**
   ```bash
   python app.py

5. **Access the Web App Open your browser and go to http://127.0.0.1:5001 to view the Moscow time.**

## 🖥️ Example Output

Here’s how the page will look:
```plaintext
----------------------------------------
|         Moscow Time Web App          |
|                                      |
|   Current Time in Moscow:            |
|           2004-01-28 21:42:21        |
|                                      |
|     Refresh the page for updates!    |
----------------------------------------
```

## 🐳 Distroless Image Version

I implemented a **Distroless-based** image for the Python Moscow Time web application to enhance security and optimize performance.

---

### 📏 Image Size Comparison

| Image Type       | Base Image Used                        | Approx. Size |
|------------------|---------------------------------------|-------------|
| **Standard Image** | `python:3.11-alpine3.18`             | **62MB**     |
| **Distroless Image** | `gcr.io/distroless/base:nonroot`    | **71MB**     |

The **Distroless Python image is actually larger than the Alpine-based image**.

---

### 📥 How to Build the Distroless Image

```bash
docker build -f distroless.Dockerfile -t azazaki/app_python:distroless .
```

---
## 🧪 Unit Tests

Automated unit tests ensure the Moscow Time Web Application functions correctly.

### ✅ How to Run Tests Locally
1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
2. **Run Unit Tests**
   ```bash
   pytest test_app.py
   ```

### ✅ What’s Tested?
- Server Status: Ensures the / route is reachable (200 OK).
- Correct Time Format: Verifies that the displayed Moscow time is correctly formatted.

These tests are executed **automatically** in the CI/CD pipeline on every push and pull request.

---
## 🔄 CI/CD Pipeline

The CI/CD pipeline automates testing, security scanning, and Docker deployment.

### 🚀 What Happens on Every Push or PR?
1. **📦 Dependencies** → Installs required Python packages.
2. **🔍 Linter** → Runs `flake8` to check code quality.
3. **🧪 Unit Tests** → Runs `pytest` to ensure correct functionality.
4. **🛡️ Security Scan** → Uses Snyk to detect vulnerabilities.
5. **🐳 Docker Build & Push** → Builds and pushes a Docker image to Docker Hub.

---

## 🚀 Contributing

1. **Fork** this repository.
2. **Create** a new branch for your feature or fix.
3. **Commit** your changes and push to your branch.
4. **Create a Pull Request** to merge your changes into the `master` branch of this repository.

---

## 🛡️ License

This project is licensed under the **MIT License**. Feel free to use, modify, and distribute as needed.

---

## 💡 Note

This web application is created for educational purposes. Feel free to enhance it by adding new features like:
- Showing other time zones.
- Adding API integration for real-time data.
- Enhancing the design with more modern styling.
