# Kubernetes Deployment

## Contents

- `deployment.yml`: Manifest file for deploying the application with 3 replicas
- `service.yml`: Manifest file for exposing the application via a NodePort service

## Prerequisites

- Minikube installed and running
- kubectl configured to use Minikube
- Docker image of the application built (moscow-time-app:latest)

## Building the Docker Image

Before deploying to Kubernetes, build the Docker image:

```bash
# From the app_python directory
docker build -t moscow-time-app:latest .
```

## Deploying to Kubernetes

To deploy the application using the manifest files:

```bash
# Apply the deployment
kubectl apply -f k8s/deployment.yml

# Apply the service
kubectl apply -f k8s/service.yml
```

## Accessing the Application

```bash
# Get the URL to access the service
minikube service moscow-time-app --url
```

## Cleaning Up

To remove the deployed resources:

```bash
kubectl delete -f k8s/service.yml
kubectl delete -f k8s/deployment.yml
``` 