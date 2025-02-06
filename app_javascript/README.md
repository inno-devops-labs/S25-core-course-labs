# JavaScript Web Application

## Overview
This web application displays the current time in Moscow using Node.js and Express.js.

Features

•	Displays current Moscow time.

•	Refresh the page to see updated time.

## Requirements
- Node.js
- npm
- express
- moment-timezone

## Local Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ramilevna/S25-core-course-labs.git
   ```
   
2.	Navigate to the app_javascript directory:

   ```bash
   cd app_javascript
   ```

3.	Install dependencies:

   ```bash
   npm install
   ```

4.	Run the application:

   ```bash
   node server.js
   ```

5.	Open the application in your browser:

    URL: http://127.0.0.1:3000/

## Docker Running

1. Build the Image

   ```bash
   docker build -t ramilevna/app_javascript:latest .
   ```
2. Run the Container

   ```bash
   docker run --rm -p 3000:3000 ramilevna/app_javascript:latest
   ```

3. Pull and Run from Docker Hub

   ```bash
   docker pull ramilevna/app_javascript:v1.0
   docker run --rm -p 3000:3000 ramilevna/app_javascript:v1.0
   ```
   
## Distroless Image Version
I implemented Distroless images for better security and efficiency.

- **Python App**: Uses `gcr.io/distroless/python3-debian12:nonroot`
- **JavaScript App**: Uses `gcr.io/distroless/nodejs18-debian12:nonroot`
- **Benefits**:
  - Smaller size
  - No shell (reduced attack surface)
  - Optimized performance
##  Docker (Distroless Dockerfiles) Running:

1. Build the Distroless Images

   ```bash
   docker build -t app_javascript:distroless -f distroless.Dockerfile .
   ```
2. Run the Distroless Containers

   ```bash
   docker run --rm -p 3000:3000 app_javascript:distroless
   ```
   
---

## Unit Tests

### Overview

Unit tests are a crucial part of the development process to ensure that the application’s features and components work as expected. These tests are written using Jest, a JavaScript testing framework that allows for easy test creation and execution.

### Running Unit Tests

To run the unit tests for the application, execute the following command:

```bash
npx jest
```

This will run all the test suites and output the results, indicating whether the tests have passed or failed.

# Javascript Application CI/CD Pipeline

![CI Status](https://github.com/ramilevna/S25-core-course-labs/actions/workflows/ci.yml/badge.svg)