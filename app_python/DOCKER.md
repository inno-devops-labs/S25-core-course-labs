# Docker Setup for Moscow Time Web Application

[Here](https://hub.docker.com/repository/docker/zerohalf/moscow-time-app/general) you can find the docker image for working Python Moscow time app.

## Best practices

### **Dockerfile linting**:
Used `hadolinter` to check `Dockerfile` for possible issues or misconfiguration.
### **Base image as working environment**:
Used `alpine` base image to minimize the total size of docker image.
### **Non-root user**:
Created different user with usergroup for him with limited permissions.
### **Correct layers**:
Optimal number of layers to minimize the size of the image and explicitly stated `requirements.txt` and `main.py`.
### **Use of .dockerignore**:
Add unnecessary files to `.dockerignore` to reduce build context.

##  **Dockerfile Distroless Key Features**:
### **Multi-Stage Build**:
Utilizes a builder stage to install dependencies and then copies only necessary files to the final image.
### **Base Image**:
Uses gcr.io/distroless/python3:nonroot, which is a minimal, secure image.
### **Security**:
Runs the application as a non-root user by default.
### **Execution Context**:
Copies the uvicorn executable and site-packages manually to ensure all dependencies are available.