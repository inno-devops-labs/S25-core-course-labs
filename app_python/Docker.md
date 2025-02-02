# Docker Best Practices and Docker Hub Deployment

## Introduction

This document outlines the best practices employed in the Dockerfiles for the frontend, backend, and database containers. It also provides instructions for building, tagging, and pushing the Docker images to Docker Hub, as well as using Docker Compose to run all services.

## Best Practices Implemented

### 1. Use Official Base Images

Using official base images ensures that you get a secure and well-maintained image.

```Dockerfile
FROM node:20
FROM python:3.9-slim
FROM postgres:13
```

### 2. Use Environment Variables
Environment variables are used to configure the application, making it easier to manage and update configurations.

```Dockerfile
ENV POSTGRES_DB=times
ENV POSTGRES_USER=myuser
```
### 3. Create a Non-Root User
Running the application as a non-root user enhances security by minimizing the potential damage from vulnerabilities.

```Dockerfile
RUN adduser --disabled-password --disabled-login myuser
```
### 4. Copy Only Necessary Files
Copy only the necessary files to the image to reduce its size and improve security.

```Dockerfile
COPY package*.json ./
COPY requirements.txt ./
```
### 5. Change Ownership of Files
Ensure that the files and directories have the correct ownership to avoid permission issues.

```Dockerfile
RUN chown -R myuser\:myuser /usr/local/app/frontend
RUN chown -R myuser\:myuser /usr/local/app/backend
```

AND for database script:
```sql
--init.sql
CREATE SCHEMA public;
GRANT ALL ON SCHEMA public TO myuser;
CREATE TABLE zone (
    id SERIAL NOT NULL,
     name VARCHAR(256),
    timezone VARCHAR(20),
    PRIMARY KEY (id),
);
INSERT INTO zone (name, timezone) VALUES ('London', 'Europe/London');
INSERT INTO zone (name, timezone) VALUES ('Moscow', 'Europe/Moscow');
INSERT INTO zone (name, timezone) VALUES ('New York', 'America/New_York');
INSERT INTO zone (name, timezone) VALUES ('Sydney', 'Australia/Sydney');
DROP role postgres;
```
### 6. Switch to Non-Root User
Switch to the non-root user before running the application to enhance security.

```Dockerfile
USER myuser
```
### 7. Expose Only Necessary Ports
Expose only the necessary ports to minimize the attack surface.

```Dcokerfile
EXPOSE 3000
EXPOSE 8080
EXPOSE 5432
```
### 8. Use  CMD
Use CMD to provide default arguments.


```Dockerfile
CMD ["postgres"]
CMD ["python", "main.py"]
CMD ["yarn", "start"]
```
## Building and Pushing Docker Images to Docker Hub
### 1. Build the Docker Images
Navigate to the root directory of each service (frontend, backend, database) and run the following commands to build the Docker images:


Build the frontend image
``` bash
cd frontend
docker build -t  myfront1 .
```

Build the backend image
``` bash
cd ../backend
docker build -t myback1 .
```

Build the database image
```bash
cd ../database
docker build -t mydb1 .
```
### 2. Tag the Docker Images
Tag the Docker images with your Docker Hub username and the desired tag:


Tag the frontend image
``` bash
docker tag myback1 jmartynova123/dev-lab2-front:latest
```
Tag the backend image

``` bash
docker tag myfront1 jmartynova123/dev-lab2-back:latest
```

Tag the database image 
``` bash
docker tag mydb1 jmartynova123/dev-lab2-db:latest
```
### 3. Push the Docker Images to Docker Hub
Push the Docker images to Docker Hub:


Push the frontend image

``` bash
docker push jmartynova123/dev-lab2-front:latest
```

Push the backend image

```bash
docker push jmartynova123/dev-lab2-back:latest
```
Push the database image
```bash
docker push jmartynova123/dev-lab2-db:latest
```

## Run the Services with Docker Compose
Navigate to the root directory of your project and run the following command to start all services:

``` bash
docker-compose up --build
```