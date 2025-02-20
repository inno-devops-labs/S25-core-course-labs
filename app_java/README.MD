# Random Hex Color Picker Web Application
A simple Java web application built with **Spring Boot** that generates and displays a random hex color code.

---

# Workflow Status

[![CI/CD Pipeline](https://github.com/Nikoali01/S25-core-course-labs/actions/workflows/ci-java.yml/badge.svg?branch=lab_3&event=push)](https://github.com/Nikoali01/S25-core-course-labs/actions/workflows/ci-java.yml)

---

## Overview
This application serves an HTML page displaying a randomly generated color along with its corresponding hex code. It uses Spring Boot for backend processing and Thymeleaf for rendering the dynamic HTML content.

---
## Features
- Displays a randomly generated color in a centered box.
- Shows the hex code of the generated color below the color box.
- Provides a button to regenerate the color by reloading the page.
- Lightweight and easy-to-understand implementation.
---
## Local Installation
### Prerequisites
- Java Development Kit (JDK) 17 or higher installed.
- Apache Maven installed.
### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/Nikoali01/S25-core-course-labs
   git checkout lab_3
   cd app_java
   ```
2. **Build the Project**
   ```bash
   mvn clean install
   ```
3. **Run the Application**
   ```bash
   mvn spring-boot:run
   ```
4. **Access the Application**
    ```bash
    http://localhost:8080/hex/color
    ```

## Unit Tests

Unit tests are implemented to ensure the reliability and correctness of the application's core functionality. Below is a summary of the tests:

1. **Test for Correct Format**:
   - Validates that the generated hex color string adheres to the format `#RRGGBB`.

2. **Test for RGB Range Validation**:
   - Ensures that each RGB component (red, green, blue) is within the valid range `[0, 255]`.

3. **Test with Mocked Random Object**:
   - Uses a mocked `Random` object to test deterministic behavior and predictability.

These tests are executed automatically as part of the CI workflow.
To start tests, navigate to the `app_java` folder
```bash
mvn test
```

## CI Workflow

The CI workflow automates the build, test, security check, and deployment processes for the application. Key stages include:

1. **Build and Lint**:
   - The project is built using Maven, and code linting is performed using Checkstyle.

2. **Run Tests**:
   - All unit tests are executed to verify the correctness of the application.

3. **Security Checks**:
   - Snyk scans the project's dependencies for vulnerabilities.

4. **Dockerization**:
   - A Docker image is built and pushed to Docker Hub, ensuring consistent deployment across environments.

The CI workflow is triggered on every push or pull request to the `app_java` directory, ensuring continuous integration and delivery.
