# JavaScript (Node.js) Web Application

## Overview

This JavaScript web application displays the **current time in the Moscow (MSK) timezone**, similar to the Python application requirement. It uses:

- **Node.js** (server-side JavaScript runtime)
- **Express** (web framework)
- **moment-timezone** (time and timezone handling)

## Features

- Returns the current date/time in MSK upon visiting the root URL `/`.
- Easy to run locally using `npm install` and `npm start`.

## Local Installation

1. Clone the repository (if you have not done so already):
    ```bash
   git clone https://github.com/your-account/your-repo.git
2. Navigate into the app_js folder:
    ```bash
   cd app_js
3. Install the dependencies:
    ```bash
   npm install
4. Start the server:
    ```bash
   npm start
5. Open http://localhost:3000 in your web browser to view the current time in Moscow.

### Docker

Below are instructions for two Docker approaches:

### 1. Standard Dockerfile
1. Build the image:
   ```bash
   cd app_js
   docker build -t your-dockerhub-user/js-app:latest .
2. Run it locally:
   ```bash
   docker run -it --rm -p 3000:3000 your-dockerhub-user/js-app:latest
3. Push the image to Docker Hub:
   ```bash
   docker push your-dockerhub-user/js-app:latest
4. Pull and run from Docker Hub:
   ```bash
   docker pull your-dockerhub-user/js-app:latest
   docker run -it --rm -p 3000:3000 your-dockerhub-user/js-app:latest
### 2. Distroless (Multi-Stage) Dockerfile
We also provide a distroless.Dockerfile demonstrating a multi-stage build with a final Distroless image:
1. Build using Distroless:
   ```bash
   docker build -f distroless.Dockerfile -t your-dockerhub-user/js-app:distroless .
2. Run:
   ```bash
   docker run -it --rm -p 3000:3000 your-dockerhub-user/js-app:distroless
3. Check container size differences:
   ```bash
   docker images | grep js-app
- You should see js-app:latest (standard) and js-app:distroless.

## Continuous Integration (CI)

The Node.js application is integrated with GitHub Actions CI, which performs the following steps:
- **Dependencies Installation**: Runs `npm install`.
- **Linting**: Uses ESLint to ensure code quality.
- **Docker Steps**: Logs in to Docker Hub, builds the Docker image, and pushes it.
- **Security Scan**: Runs Snyk to scan the Docker image for vulnerabilities.

The CI workflow runs automatically when changes are pushed to the `app_js/` folder.
