## Overview
A web application that provides random quotes, built using Java and Spring Boot.

## Requirements
- JDK 17 or later must be installed.

## Installation

1. Navigate to the project directory.

2. Build the application using Maven:
   ```bash
   ./mvnw clean install

3. Run the Spring Boot application:
    ```bash
   java -jar target/app-java-1.0.jar

Once the application is running, open it in your browser at http://localhost:8080/quotes/random.

## Installation via Docker

### 📥 From Docker Hub
1. Pull the image:
   ```bash
   docker pull vechkanovvv/app_java:v1
   
2. Run the container:
   ```bash
   docker run -d -p 8080:8080 vechkanovvv/app_java:v1
### 🛠️ Via Console (Build Locally)
1. Build the image:
   ```bash
   docker build -t vechkanovvv/app_java:v1 .
2. Run the container:
   ```bash
   docker run -d -p 8080:8080 vechkanovvv/app_java:v1

Now your Spring Boot application is running at http://localhost:8080/quotes/random.
