

# Kubernetes

## Overview

This document outlines the steps taken to deploy the Moscow Time app to a local Kubernetes cluster using **Minikube** and **kubectl**.



## Creating a simple deployment and service
![alt text](src/image.png)

To create a deployment for our pod:

```bash
kubectl create deployment web-app --image=alimansour000/moscow-time-app:latest
```
![alt text](src/image-1.png)

Then we have to create a service to expose our app for external access:

```bash
kubectl expose deployment web-app --type=LoadBalancer --port=5000
```
![alt text](src/image-2.png)

**Pods and services:**

```bash
$ kubectl get pod,svc
```
![alt text](src/image-3.png)

to access our app we can use:

```bash
minikube service web-app
```
![alt text](src/image-4.png)

![alt text](src/image-5.png)


Cleanup:
```bash
kubectl delete -f deployment.yml
kubectl delete -f service.yml
```
![alt text](src/image-9.png)

## Manifest files

Just like before we have to have a deployment for our pod and a service, we can do that through deployment/service manifest files.


To apply our file we run:

```bash
$ kubectl apply -f deployment.yml 
```

```bash
$ kubectl apply -f service.yml 
```
![alt text](src/image-6.png)

**Pods and services:**

```bash
$ kubectl get pod,svc
```

![alt text](src/image-7.png)
```bash
$ minikube service --all
```
![alt text](src/image-8.png)



- **Kubernetes service:**
![alt text](src/image-11.png)

- **Application service:**
![alt text](src/image-10.png)