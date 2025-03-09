# Lab 9: Introduction to Kubernetes

This lab focuses on setting up a local Kubernetes environment using Minikube, deploying applications, and creating Kubernetes manifests. Below are the tasks completed, along with evidence and outputs.

---

## Task 1: Kubernetes Setup and Basic Deployment

### 1. Learn About Kubernetes

Studied the fundamentals of Kubernetes, including its components and architecture. Referenced the official Kubernetes documentation:

- [What is Kubernetes?](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/)
- [Kubernetes Components](https://kubernetes.io/docs/concepts/overview/components/)

### 2. Install Kubernetes Tools

Installed `kubectl` and `minikube` to manage the Kubernetes cluster locally. Followed the official guide:

- [Kubernetes Tools Installation](https://kubernetes.io/docs/tasks/tools/)

### 3. Deploy Your Application

Deployed a Python application using the following command:

```bash
kubectl create deployment moscow-time-app --image=ali12hamdan/moscow-time-app:
```

**Screenshot of Deployment Creation:**
![Deployment Creation](screen-sh/1.jpg)

**List of Deployments:**

![List Deployments](screen-sh/2.jpg)

### 4. Access Your Application

Exposed the application using a Service and retrieved its URL:

```bash
minikube service moscow-time-app --url
```

**Output:**

```out
http://192.168.49.2:30417
```

**Screenshot of Service URL:**

![Service URL](screen-sh/10.jpg)

### 5. Verify Deployment and Service

Checked the status of Pods and Services:

```bash
kubectl get pods,svc
```

**Screenshots:**

![Pods and Services](screen-sh/3.jpg)

### 6. Cleanup

Removed the Deployment and Service to maintain a clean environment:

```bash
kubectl delete deployment moscow-time-app
kubectl delete service moscow-time-app
```

![clean](screen-sh/4.jpg)

---

## Task 2: Declarative Kubernetes Manifests

### 1. Create Deployment Manifest

Created a `deployment.yml` file to deploy the Python application with 3 replicas. Applied the manifest:

```bash
kubectl apply -f deployment.yml
```

**Screenshot of Deployment Application:**

![Deployment Applied](screen-sh/5.jpg)

### 2. Create Service Manifest

Created a `service.yml` file to expose the application. Applied the manifest:

```bash
kubectl apply -f service.yml
```

### 3. Verify Deployment and Service

Checked the status of Pods and Services:

```bash
kubectl get pods,svc
```

**Screenshot:**
![Pods and Services](screen-sh/6.jpg)

### 4. Access Services via Minikube

Retrieved the URLs for all services:

```bash
minikube service --all
```

**Screenshots:**
![Minikube Service Output](screen-sh/7.jpg)
![Python Service in Browser](screen-sh/8.jpg)
![Kubernetes Service in Browser](screen-sh/9.jpg)

---
