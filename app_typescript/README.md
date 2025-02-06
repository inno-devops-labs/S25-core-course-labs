# React Web Application

## Overview

This is a simple typescript web application with Vite and React that shows current time in Moscow.

## Running locally

1. Make sure you have [Node.js](https://nodejs.org/en) installed.

2. Clone this repository and enter its folder

    ```bash
    git clone https://github.com/dmhd6219/S25-core-course-labs.git -b lab1
    cd S25-core-course-labs
    cd app_typescript
    ```

3. Install dependencies

    ```bash
    npm install
    ```

4. Run the application

```bash
npm run dev
```

## Running locally with Docker

### Build it locally

1. Clone this repository and enter its folder
    ```bash
    git clone https://github.com/dmhd6219/S25-core-course-labs.git -b lab1
    cd S25-core-course-labs
    cd app_python
    ```

2. Build Docker image
   ```bash
   # It may take a while.. For me it takes ~1 minute
   docker build -t dmhd6219/inno_devops_lab2_typescript_basic:latest -f Dockerfile .
   ```

3. Run the application
   ```bash
   docker run -d -p 8080:8080 dmhd6219/inno_devops_lab2_typescript_basic:latest
   ```

### Pull from DockerHub

1. Pull the image
   ```bash
   docker pull dmhd6219/inno_devops_lab2_typescript_basic:latest
   ```

2. Run the application

   ```bash
   docker run -d -p 8080:8080 dmhd6219/inno_devops_lab2_typescript_basic:latest
   ```
   
## Running locally with Distroless Image Version

### Build it locally

1. Clone this repository and enter its folder
    ```bash
    git clone https://github.com/dmhd6219/S25-core-course-labs.git -b lab1
    cd S25-core-course-labs
    cd app_python
    ```

2. Build Docker image
   ```bash
   # It may take a while.. For me it takes ~1 minute
   docker build -t dmhd6219/inno_devops_lab2_typescript_bonus:latest -f distroless.Dockerfile .
   ```

3. Run the application
   ```bash
   docker run -d -p 8080:8080 dmhd6219/inno_devops_lab2_typescript_bonus:latest
   ```

### Pull from DockerHub

1. Pull the image
   ```bash
   docker pull dmhd6219/inno_devops_lab2_typescript_bonus:latest
   ```

2. Run the application

   ```bash
   docker run -d -p 8080:8080 dmhd6219/inno_devops_lab2_typescript_bonus:latest
   ```

## Unit Tests

```bash
pytest test.py
```