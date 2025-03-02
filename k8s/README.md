## Lab 9: Introduction to Kubernetes

This document provides an overview of the Kubernetes setup, deployments, services, and ingress configurations performed during the lab.

---

### Environment Setup

#### Kubernetes Tools Installation
- Installed `kubectl` and `minikube` on Ubuntu.
- Started the Minikube cluster using:
  ```bash
  minikube start
  ```
### Minikube IP
The Minikube cluster IP address is `192.168.49.2`.

---

### Task 1: Basic Deployment and Service

#### Step 1: Create Deployments
Created two deployments:
- `first-node` with the image `nickwidbestie/region-time-api`.
- `second-node` with the image `nickwidbestie/random-color-picker:6d9f319aeb8fe1782ca1a1037371a90ab8867a3f`.

Commands used:
```bash
kubectl create deployment first-node --image=nickwidbestie/region-time-api
kubectl create deployment second-node --image=nickwidbestie/random-color-picker:6d9f319aeb8fe1782ca1a1037371a90ab8867a3f
```

### Step 2: Expose Services
Exposed both deployments as NodePort services:

- `first-node` on port `80`.
- `second-node` on port `8081`.

Commands used:
```bash
kubectl expose deployment first-node --type=NodePort --port=80
kubectl expose deployment second-node --type=NodePort --port=8081
```

### Step 3: Access Services
Accessed the services using `minikube service`:

```bash
minikube service first-node
minikube service second-node
```

### URLs:
- `first-node`: http://192.168.49.2:30814
- `second-node`: http://192.168.49.2:31846

---

### Step 4: Cleanup
Deleted the deployments and services after testing:

```bash
kubectl delete deployment first-node
kubectl delete service first-node
kubectl delete deployment second-node
kubectl delete service second-node
```

### Task 2: Declarative Manifests

#### Step 1: Create Python and Java Deployments
Applied YAML manifests for Python and Java applications:

- `python-deployment.yml` and `python-service.yml`.
- `java-deployment.yml` and `java-service.yml`.

Commands used:
```bash
kubectl apply -f python-deployment.yml
kubectl apply -f python-service.yml
kubectl apply -f java-deployment.yml
kubectl apply -f java-service.yml
```

### Step 2: Verify Pods and Services
Checked the status of pods and services:

```bash
kubectl get pods,svc
```

Output:
```bash
NAME                                      READY   STATUS    RESTARTS   AGE
pod/java-app-deployment-668554854-h7q5v   1/1     Running   0          6s
pod/java-app-deployment-668554854-n4rf4   1/1     Running   0          6s
pod/java-app-deployment-668554854-qnk62   1/1     Running   0          6s
pod/python-app-deployment-75b9fff778-6p4xr 1/1     Running   0          20s
pod/python-app-deployment-75b9fff778-mg29j 1/1     Running   0          20s
pod/python-app-deployment-75b9fff778-ndvrr 1/1     Running   0          20s

NAME                          TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/java-app-service      NodePort    10.98.39.156    <none>        8081:32205/TCP   6s
service/kubernetes            ClusterIP   10.96.0.1       <none>        443/TCP          16m
service/python-app-service    NodePort    10.107.133.226  <none>        80:30120/TCP     20s
```

### Step 3: Access Services
Accessed the services using `minikube service --all`:

```bash
minikube service --all
```

### Step 4: Cleanup
Deleted the deployments and services:

```bash
kubectl delete -f python-deployment.yml
kubectl delete -f python-service.yml
kubectl delete -f java-deployment.yml
kubectl delete -f java-service.yml
```

### Bonus Task: Ingress Configuration

#### Step 1: Enable Ingress Addon
Enabled the Minikube ingress addon:

```bash
minikube addons enable ingress
```

#### Step 2: Apply Ingress Manifest
Applied the ingress manifest (`ingress.yml`) to route traffic to `python-app.local` and `java-app.local`:

```bash
kubectl apply -f ingress.yml
```

#### Step 3: Verify Ingress
Checked the ingress resource:

```bash
kubectl get ingress
```

Output:
```bash
NAME    CLASS    HOSTS                            ADDRESS         PORTS   AGE
ingress nginx    python-app.local,java-app.local  192.168.49.2    80      43s
```

#### Step 4: Test Ingress
Tested access to `python-app.local`:

```bash
curl --resolve "python-app.local:80:192.168.49.2" http://python-app.local/time/moscow
```

Result:
```commandline
<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Moscow Time</title>
        <style>
            body {
                text-align: center;
                font-family: Arial, sans-serif;
                margin-top: 50px;
            }
            img {
                margin-top: 20px;
                max-width: 100%;
                height: auto;
            }
        </style>
    </head>
    <body>
        <h1><b>Current Time in Moscow:</b> 2025-03-02 20:25:19.281443+03:00</h1>
        <img src="https://kudamoscow.ru/uploads/9151b31fb2ef1543969b65e6bc111bea.png" alt="Moscow Image">
    </body>
    </html>

```