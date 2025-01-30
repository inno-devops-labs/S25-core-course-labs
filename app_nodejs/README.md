# Node.js Web Application

## Overview

This web application displays the current time in Abu Dabi. It is built using Node.js and Express, with a client-side HTML page that dynamically fetches the 
time.

## Installation

### Prerequisites

- Node.js installed
- npm package manager installed

### Steps

1. Clone the repository.
2. Install dependencies using command:

    ```bash
     npm install
    ```

3. Run the application:

    ```bash
     node app.js
    ```

4. Open browser and go to:
`
   http://localhost:3000
`

## DOCKER

### Build

To build the Docker image:

```bash
  docker build --no-cache -t app_nodejs:latest .
```

### Pull

To pull the Docker image:

```bash
  docker pull ilsiia/app_nodejs:latest  
```

### Run

To run the Docker image:

```bash
  docker run -p 3000:3000 ilsiia/app_nodejs:latest
```

Or if port 3000 on your machine is in use, replace the port 5000 with the free port like that:

```bash
  docker run -p <free port>:3000 ilsiia/app_nodejs:latest
```

## Distroless Image Version

### Pull Distroless Image

To pull the distroless image:

```bash
  docker pull ilsiia/nodejs_app:distroless
```

### Run Distroless Image

To run the distroless image:

```bash
  docker run -p 3000:3000 ilsiia/nodejs_app:distroless
```

If port 3000 is not free on your machine change it with free one:

```bash
  docker run -p <free_port>:3000 ilsiia/nodejs_app:distroless
```

### Build Distroless Image

To build the distroless image:

```bash
  docker build -t nodejs_app:distroless -f distroless.Dockerfile .
```


