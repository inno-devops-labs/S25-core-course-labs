# Kubernetes Deployment

This directory contains Kubernetes manifest files for deploying the Python Flask application to a Kubernetes cluster.

## Files

- `deployment.yml`: Deployment configuration for the Python Flask application with 3 replicas
- `service.yml`: Service configuration to expose the Python Flask application

## Building the Docker Image for Minikube

Before deploying to Minikube, you need to build the Docker image and make it available to Minikube:

```bash
# Set the docker environment to use Minikube's docker daemon
eval $(minikube docker-env)

# Build the image
docker build -t python-app:latest -f app_python/Dockerfile app_python/
```

## Deploying to Kubernetes

```bash
# Apply the deployment
kubectl apply -f k8s/deployment.yml

# Apply the service
kubectl apply -f k8s/service.yml
```

## Accessing the Application

```bash
# Get the URL to access the service
minikube service python-app-service
```

## Monitoring the Deployment

```bash
# Check the status of the deployment
kubectl get deployments

# Check the status of the pods
kubectl get pods

# Check the status of the service
kubectl get services
```

## Cleanup

```bash
# Delete the service
kubectl delete -f k8s/service.yml

# Delete the deployment
kubectl delete -f k8s/deployment.yml
```

## Command Outputs

### Output of `kubectl get pods,svc`

```
NAME                             READY   STATUS    RESTARTS   AGE
pod/python-app-c95f7685d-2qbql   1/1     Running   0          43s
pod/python-app-c95f7685d-7nfx2   1/1     Running   0          44s
pod/python-app-c95f7685d-fxhqh   1/1     Running   0          43s

NAME                         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
service/kubernetes           ClusterIP   10.96.0.1       <none>        443/TCP        7m29s
service/python-app-service   NodePort    10.109.107.49   <none>        80:30616/TCP   39s
```

### Output of `minikube service python-app-service --url`

```
http://127.0.0.1:51513
```

The application is successfully deployed and accessible at the URL provided by the `minikube service` command. 