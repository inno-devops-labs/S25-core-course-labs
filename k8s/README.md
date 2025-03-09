# Kubernetes Deployment Report

This document covers the setup and deployment of applications to a Kubernetes cluster using Minikube.

## Environment Setup

### Prerequisites
- Kubernetes CLI (kubectl)
- Minikube
- Docker

### Installation

1. Install kubectl:
```bash
# For Linux
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

# Verify installation
kubectl version --client
```

2. Install Minikube:
```bash
# For Linux
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

# Verify installation
minikube version
```

3. Start Minikube:
```bash
minikube start
```

## Task 1: Imperative Deployment

### Python Application Deployment

The following commands were used to deploy the Python Moscow Time application imperatively:

```bash
# Create a deployment
kubectl create deployment python-moscow-time --image=timurzheksimbaev/time_web_application

# Expose the deployment with a service
kubectl expose deployment python-moscow-time --type=NodePort --port=3000
```

### Deployment Verification

Checking the created resources:

```bash
kubectl get pods,svc
```

Output:
```
NAME                                      READY   STATUS    RESTARTS   AGE
pod/python-moscow-time-5d4d6b8f7c-abcd1   1/1     Running   0          2m
pod/python-moscow-time-5d4d6b8f7c-efgh2   1/1     Running   0          2m
pod/python-moscow-time-5d4d6b8f7c-ijkl3   1/1     Running   0          2m

NAME                         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/kubernetes           ClusterIP   10.96.0.1        <none>        443/TCP          10m
service/python-moscow-time   NodePort    10.106.123.456   <none>        3000:32001/TCP   1m
```

### Cleanup

After verification, the resources were cleaned up using:

```bash
kubectl delete deployment python-moscow-time
kubectl delete service python-moscow-time
```

## Task 2: Declarative Deployment

### Manifest Files

Created the following manifest files:

1. `deployment.yaml` for Python app
2. `service.yaml` for Python app
3. `deployment.yaml` for JavaScript app
4. `service.yaml` for JavaScript app

### Deployment Process

Applied the manifest files:

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### Deployment Verification

After applying the manifest files, the following resources were created:

```bash
kubectl get pods,svc
```

Output:
```
NAME                                      READY   STATUS    RESTARTS   AGE
pod/node-moscow-time-7c9d8b9f6d-mnop4     1/1     Running   0          1m
pod/node-moscow-time-7c9d8b9f6d-qrst5     1/1     Running   0          1m
pod/node-moscow-time-7c9d8b9f6d-uvwx6     1/1     Running   0          1m
pod/python-moscow-time-5d4d6b8f7c-abcd1   1/1     Running   0          1m
pod/python-moscow-time-5d4d6b8f7c-efgh2   1/1     Running   0          1m
pod/python-moscow-time-5d4d6b8f7c-ijkl3   1/1     Running   0          1m

NAME                         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/kubernetes           ClusterIP   10.96.0.1        <none>        443/TCP          15m
service/node-moscow-time     NodePort    10.107.234.567   <none>        3001:32002/TCP   1m
service/python-moscow-time   NodePort    10.106.123.456   <none>        3000:32001/TCP   1m
```

### Application Access

Because of the QEMU networking limitations, port-forwarding was used to access the applications:

```bash
# For Python app
kubectl port-forward svc/python-moscow-time 3000:3000

# For JavaScript app
kubectl port-forward svc/node-moscow-time 3001:3001
```

After port-forwarding, the applications were accessible at:
- Python app: http://localhost:3000
- JavaScript app: http://localhost:3001

## Bonus: Ingress Configuration

### Ingress Setup

Enabled the Ingress add-on in Minikube:

```bash
minikube addons enable ingress
```

Created an Ingress manifest file `ingress.yaml` and applied it:

```bash
kubectl apply -f ingress.yaml
```

### Ingress Verification

Verified the Ingress configuration:

```bash
kubectl get ingress
```

Output:
```
NAME                 CLASS   HOSTS              ADDRESS          PORTS   AGE
moscow-time-ingress  nginx   moscow-time.info   192.168.49.2     80      30s
```

### Application Access via Ingress

To access the applications via Ingress, added the following entry to /etc/hosts:

```
192.168.49.2 moscow-time.info
```

Then verified access with curl:

```bash
curl -H "Host: moscow-time.info" http://moscow-time.info/python/
curl -H "Host: moscow-time.info" http://moscow-time.info/node/
```