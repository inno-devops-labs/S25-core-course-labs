# Moscow Time Web Application (Node.js)

## Overview
This is a simple Node.js web application built using Express. It displays the current time in Moscow and updates on each page refresh.

## Local Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Dyddxd/S25-core-course-labs.git
   cd app_nodejs
   ```
2. Install dependencies:
    ```bash
   npm install
    ```
3. Run the application:
    ```bash
   npm start
    ```

## Docker Distroless
1. Build:
   ```bash
   cd app_nodejs
   docker build -f distroless.Dockerfile -t app_nodejs .
   ```
2. Pull the image
   ```bash
   docker pull zerohalf/app_nodejs:nonroot
   ```
3. Run and test working app:
   ```bash
   docker run -d -p 3000:3000 --name app_nodejs zerohalf/app_nodejs:nonroot
   curl localhost:3000
   ```