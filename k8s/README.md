# Kubernetes Deployment Documentation

## Project Overview
This project demonstrates a multi-application deployment in Kubernetes using Minikube. We have successfully deployed:
1. Python Flask application (marketer7/flask-time)
2. Nginx server

## Deployment Components
- Python Flask app with 3 replicas
- Nginx server with 3 replicas
- NodePort Services for both applications
- Ingress controller for routing

## Implementation Steps

### 1. Initial Setup
- Created k8s directory
- Set up basic manifest files (deployment.yml, service.yml)
- Started Minikube cluster

### 2. Python App Deployment
```bash
kubectl apply -f deployment.yml
kubectl apply -f service.yml
```

### 3. Nginx Deployment
```bash
kubectl apply -f nginx-deployment.yml
kubectl apply -f nginx-service.yml
```

### 4. Ingress Configuration
```bash
minikube addons enable ingress
kubectl apply -f ingress.yml
```

## Current Status

### Pods and Services Status
```bash
kubectl get pods,svc
```
Output:
```
NAME                              READY   STATUS    RESTARTS   AGE
pod/python-app-7f54594587-62v55   1/1     Running   0          23s
pod/python-app-7f54594587-c4fhd   1/1     Running   0          23s
pod/python-app-7f54594587-xttc2   1/1     Running   0          23s

NAME                         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes           ClusterIP   10.96.0.1       <none>        443/TCP          17m
service/python-app-service   NodePort    10.100.50.185   <none>        8000:30000/TCP   17s
```

### Service Configuration
- Python App: NodePort 30000
- Nginx: NodePort 30001

### Ingress Rules
- python-app.local → Python Flask application
- nginx-app.local → Nginx server

## Access Information
To access the applications:
1. Add the following entries to /etc/hosts:
```bash
<minikube-ip> python-app.local
<minikube-ip> nginx-app.local
```

2. Access via browser or curl:
```bash
curl python-app.local
curl nginx-app.local
```

## Verification
Both applications are successfully deployed and accessible through their respective endpoints:
- Python Flask app: http://python-app.local
- Nginx server: http://nginx-app.local

## Screenshots
![image](image.png)

## Next Steps
- Monitor application performance
- Set up resource limits
- Implement health checks
- Configure horizontal pod autoscaling



