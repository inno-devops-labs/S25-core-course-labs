# Comic Fetcher

[![CI Status](https://github.com/Kazan-Strelnikova/S25-core-course-labs/actions/workflows/javascript-ci.yml/badge.svg)](https://github.com/Kazan-Strelnikova/S25-core-course-labs/actions)

## Overview

This web application fetches the latest comic from **XKCD** and displays it on the page. Upon clicking the "Do you wanna see a comic?" button, the app fetches the latest comic's details (title, image, date, and description) and shows them in the HTML.

The app is powered by a **Node.js** backend using **Express** to serve static files, including the HTML, CSS, and JavaScript for the frontend.

## Setup and Installation

### Prerequisites

- **Node.js** installed on your machine.
- **Web browser** (Google Chrome, Firefox, etc.)

### Steps to Run the App

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Kazan-Strelnikova/S25-core-course-labs.git
   cd S25-core-course-labs/app_javascript
   ```

2. **Install Node.js dependencies**:

   Navigate to the project folder and install the required dependencies:

   ```bash
   npm install
   ```

3. **Ensure that the required files are present**:
   - `server.js` - The Express server that serves the app.
   - `public/index.html` - The main HTML page.
   - `public/style_comic.css` - The styling for the comic container.
   - `public/myapp.js` - JavaScript file to fetch and display the comic.

4. **Run the server**:

   Start the server by running:

   ```bash
   node server.js
   ```

   The server will start running at `http://localhost:3000`.

5. **Open the app in your browser**:

   Go to `http://localhost:3000` in your web browser to view the application.

6. **Click the button**:
   - When you click the "Do you wanna see a comic?" button, the app will fetch the latest comic and display its title, image, release date, and description below the button.

## Docker Usage

### How to Build

To build the Docker image for this application, run:

```bash
docker build -t js-app .
```

### How to Pull

To pull the pre-built image from Docker Hub, run:

```bash
docker pull kira354/js-app:latest
```

### How to Run

To run the Docker container and serve the application, use the following command:

```bash
docker run -p 3000:3000 js-app
```

Visit `http://localhost:3000` in your browser to access the application.

## **Distroless Image Version**

### **How to Build the Distroless Image**

```bash
docker build -f distroless.Dockerfile -t kira354/app-javascript-distroless .
```

### **How to Pull the Distroless Image**

```bash
docker pull kira354/app-javascript-distroless
```

### **How to Run the Distroless Image**

```bash
docker run -p 3000:3000 kira354/app-javascript-distroless
```

## Unit Tests

This project includes unit tests to validate both backend and frontend functionality. The tests cover API endpoint responses, DOM updates, and error handling.

### Running the Tests

Ensure that dependencies are installed before running tests:

```sh
npm install
```

To execute the tests, navigate to the `app_javascript` directory and run:

```sh
cd app_javascript
npm test
```

## CI Workflow

This project integrates a GitHub Actions CI pipeline to automate testing, linting, security scanning, and Docker image deployment.

### Workflow Steps

1. **Checkout Code**: Retrieves the latest repository state.
2. **Set Up Node.js**: Configures the Node.js environment.
3. **Cache npm Dependencies**: Speeds up builds by caching dependencies.
4. **Install Dependencies**: Installs project dependencies using `npm install`.
5. **Run Tests**: Executes unit tests using Jest.
6. **Lint Code**: Checks for code style and errors using ESLint.
7. **Snyk Vulnerability Scan**: Analyzes dependencies for security vulnerabilities.
8. **Docker Login, Build & Push**: Builds a Docker image using a distroless base and pushes it to Docker Hub.
