# Java Web Application - Omsk Timezone

![CI Workflow](https://github.com/DoryShibkova/S25-core-course-labs/actions/workflows/java-ci.yml/badge.svg)

## Overview
This project is a simple Java web application that displays the current time in Omsk. The application uses the Spark framework for creating the web server and Java's built-in **ZonedDateTime** and **ZoneId** classes for timezone management.
## Features
- Displays the current time in Omsk.
- Automatically updates the time upon refreshing the webpage.

## Technology Stack
- **Java:** Programming language used to develop the application.
- **Spark Framework:** Lightweight web framework for handling HTTP requests.

## Installation steps

Steps to configure the app locally:
1. **Clone the repository:**
   ```bash
       git clone https://github.com/DoryShibkova/S25-core-course-labs
   ```
2. **Navigate to the project directory:**
   ```bash
       cd app_Java
   ```
3. **Download the Spark framework:**
   - Visit Spark Framework and download the spark-core JAR file.
   - Place the JAR file in project directory.
     
4. **Compile the application:**
   ```bash
       javac -cp spark-core-2.9.3.jar OmskTimeApp.java
   ```
5. **Run the application:**
   ```bash
       java -cp .:spark-core-2.9.3.jar OmskTimeApp
   ```
6. **Open browser and go to:** http://localhost:4567/

     
## Docker

### Login to Docker Hub
Before building or pulling the Docker image, login into Docker Hub:
```bash
docker login
```
You will be prompted to enter your Docker Hub username and password.

### How to Build the Docker Image
To build the Docker image for this application, navigate to the project directory and run:
```bash
docker build -t appjava .
```

### How to Push the Docker Image to Docker Hub
```bash
docker tag appjava <dockerhub-username>/appjava:latest
docker push <dockerhub-username>/appjava
```

### How to Pull the Docker Image from Docker Hub
```bash
docker pull <dockerhub-username>/appjava
```

### How to Run the Docker Container
To run the application in a Docker container, use:
```bash
docker run -p 4567:4567 <dockerhub-username>/appjava
```
**Open browser and visit:** http://localhost:4567/
 
     
## Distroless Image Version

### Build the Distroless Image
```bash
docker build -t appjava-dist -f distroless.Dockerfile .
```

### Push the Distroless Image to Docker Hub
```bash
docker tag appjava-dist <dockerhub-username>/appjava-dist:latest
docker push <dockerhub-username>/appjava-dist
```

### Pull the Docker Image from Docker Hub
```bash
docker pull <dockerhub-username>/appjava-dist
```

### Run the Docker Container
```bash
docker run -p 4567:4567 <dockerhub-username>/appjava-dist
```
**Open browser and go to:** http://localhost:4567

## Unit Tests
Unit tests for this application are written using JUnit. To run the tests locally:
```
bash
mvn test
```
## Continuous Integration (CI) Workflow
This project uses **GitHub Actions** for automated **Continuous Integration (CI)**. The CI pipeline ensures:

- **Code quality** through compilation and dependency validation.
- **Automated unit tests** using JUnit.
- **Building and pushing Docker images** to Docker Hub.
- **Security scanning** using Snyk.

## CI Workflow Steps
1. **Checkout Code:** The workflow fetches the latest code from the repository.
2. **Set Up Java Environment:** Installs Java 11 and configures Maven.
3. **Cache Dependencies:** Uses GitHub cache to speed up Maven dependency resolution.
4. **Build with Maven:** Compiles the Java project using mvn clean package.
5. **Run Unit Tests:** Executes JUnit tests using mvn test.
6. **Security Scan:** Scans dependencies for vulnerabilities using Snyk.
7. **Build Docker Image:** Creates a Docker image for the application.
8. **Push to Docker Hub:** If tests pass, the built image is pushed to Docker Hub.

## How to View CI Results
To see the latest CI results, visit the **https://github.com/DoryShibkova/S25-core-course-labs/actions**

## Run CI Locally
To manually test CI steps locally, run:
```
bash
# Run unit tests with Maven
mvn test

# Build the project
mvn clean package

# Build and run Docker container
docker build -t appjava .
docker run -p 4567:4567 appjava
``` 
