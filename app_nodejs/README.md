# Moscow Time Web Application (Node.js)

## Overview
A simple web application built with Express.js that displays the current time in Moscow. This application serves as a bonus implementation alongside the Python version, demonstrating the same functionality using Node.js.

## Features
- Real-time Moscow time display
- Clean and modern user interface
- Automatic time updates on page refresh

## Local Installation

1. Clone the repository
2. Navigate to the `app_nodejs` directory
3. Install dependencies:
   ```bash
   npm install
   ```
4. Start the application:
   ```bash
   npm start
   ```
5. Open your browser and visit `http://localhost:3000`

## Technologies Used
- Node.js
- Express.js - web framework
- moment-timezone - timezone handling library

## Best Practices Applied
- Modern JavaScript syntax
- Clean code architecture
- Proper error handling
- Efficient dependency management with package.json
- Comprehensive documentation

## Docker Support

### Standard Docker Image

#### Building the Image
```bash
docker build -t your-dockerhub-username/moscow-time-nodejs:latest .
```

#### Pulling from Docker Hub
```bash
docker pull your-dockerhub-username/moscow-time-nodejs:latest
```

#### Running the Container
```bash
docker run -d -p 3000:3000 your-dockerhub-username/moscow-time-nodejs:latest
```

### Distroless Image Version

The application is also available as a distroless image for enhanced security and smaller size.

#### Building the Distroless Image
```bash
docker build -t your-dockerhub-username/moscow-time-nodejs:distroless -f distroless.Dockerfile .
```

#### Pulling the Distroless Image
```bash
docker pull your-dockerhub-username/moscow-time-nodejs:distroless
```

#### Running the Distroless Container
```bash
docker run -d -p 3000:3000 your-dockerhub-username/moscow-time-nodejs:distroless
```

### Image Comparison
- Standard Image (Alpine-based): ~150MB
- Distroless Image: ~126MB

The distroless version offers enhanced security through:
- Minimal attack surface
- No shell access
- No package manager
- Runs as non-root user

Choose the distroless version for production deployments where security is a priority.
