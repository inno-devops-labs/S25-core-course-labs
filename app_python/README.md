# Moscow Time Web Application

![CI Status](https://github.com/Ali12hamdan/S25-core-course-labs/actions/workflows/py-ci.yml/badge.svg)

## Overview
This is a simple web application that displays the current time in Moscow. It is built using **Python** and **Flask**, and containerized using **Docker**.

---

## Docker Instructions

### **How to Build**
1. Clone the repository:
   ```bash
   git clone git clone --branch lab2 https://github.com/Ali12hamdan/S25-core-course-labs.git

   docker pull ali12hamdan/moscow-time:1.0

   docker run -p 5001:5001 ali12hamdan/moscow-time-app:1.0



### Unit Tests
Run tests with:
```bash
pytest test_app.py -v
```

### CI/CD
This project uses GitHub Actions for continuous integration:

 - **Tests**: Linting, unit tests, and Docker builds run on every push.

 - **Docker Image**: Automatically built and pushed to Docker Hub.