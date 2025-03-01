# Lab 9: Introduction to Kubernetes

## Task 1: Kubernetes Setup and Basic Deployment

### Activate `minicube` for local cluster:

`minikube start`

```
PS C:\Projects\University\S25\DevOps\S25-core-course-labs\k8s> minikube start                                                                            
* minikube v1.35.0 on Microsoft Windows 11 Pro 10.0.26100.3194 Build 26100.3194
* Using the docker driver based on existing profile
* Starting "minikube" primary control-plane node in "minikube" cluster
* Pulling base image v0.0.46 ...
* Restarting existing docker container for "minikube" ...
* Preparing Kubernetes v1.32.0 on Docker 27.4.1 ...
! Failing to connect to https://registry.k8s.io/ from both inside the minikube container and host machine
* To pull new external images, you may need to configure a proxy: https://minikube.sigs.k8s.io/docs/reference/networking/proxy/
* Verifying Kubernetes components...
  - Using image gcr.io/k8s-minikube/storage-provisioner:v5
* Enabled addons: default-storageclass, storage-provisioner

! C:\Program Files\Docker\Docker\resources\bin\kubectl.exe is version 1.30.5, which may have incompatibilities with Kubernetes 1.32.0.
  - Want kubectl v1.32.0? Try 'minikube kubectl -- get pods -A'
* Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
```

### Create deployment:

`kubectl create deployment app-python --image=dmhd6219/inno_devops_lab2_python_bonus:latest`

```
PS C:\Projects\University\S25\DevOps\S25-core-course-labs\k8s> kubectl create deployment app-python --image=dmhd6219/inno_devops_lab2_python_bonus:latest
deployment.apps/app-python created
```

### Expose deployment:

`kubectl expose deployment app-python --type=LoadBalancer --port=8000`

```
PS C:\Projects\University\S25\DevOps\S25-core-course-labs\k8s> kubectl expose deployment app-python --type=LoadBalancer --port=8000
service/app-python exposed
```

### Get current pods and services:

`kubectl get pods,svc`

```
PS C:\Projects\University\S25\DevOps\S25-core-course-labs\k8s> kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-768cdb75c5-v9ltt   1/1     Running   0          2m2s

NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/app-python   LoadBalancer   10.107.141.197   <pending>     8000:32751/TCP   91s
service/kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          3d18h
```

### Open deployment:

`minikube service app-python --url`

```
PS C:\Projects\University\S25\DevOps\S25-core-course-labs\k8s> minikube service app-python --url
http://127.0.0.1:56015
! Because you are using a Docker driver on windows, the terminal needs to be open to run it.
```

![app_python](assets/app_python.png)

### Remove resources:

`kubectl delete deployment app-python`

```
PS C:\Projects\University\S25\DevOps\S25-core-course-labs\k8s> kubectl delete deployment app-python
deployment.apps "app-python" deleted
```

`kubectl delete svc app-python`

```
PS C:\Projects\University\S25\DevOps\S25-core-course-labs\k8s> kubectl delete svc app-python
service "app-python" deleted
```

`kubectl get pods,svc`

```
PS C:\Projects\University\S25\DevOps\S25-core-course-labs\k8s> kubectl get pods,svc
NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   3d18h
```

## Task 2: Declarative Kubernetes Manifests

### Apply manifests for app_python:

`kubectl apply -f app_python`

```
PS C:\Projects\University\S25\DevOps\S25-core-course-labs\k8s> kubectl apply -f app_python
deployment.apps/app-python created
service/app-python-service created
```

`kubectl get pods,svc`

```
PS C:\Projects\University\S25\DevOps\S25-core-course-labs\k8s> kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-65cf4749b8-d772n   1/1     Running   0          21s
pod/app-python-65cf4749b8-nxlbz   1/1     Running   0          21s
pod/app-python-65cf4749b8-xzsnw   1/1     Running   0          21s

NAME                         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
service/app-python-service   ClusterIP   10.101.131.199   <none>        80/TCP    21s
service/kubernetes           ClusterIP   10.96.0.1        <none>        443/TCP   3d19h
```

`minikube service --all`

```
PS C:\Projects\University\S25\DevOps\S25-core-course-labs\k8s> minikube service --all
|-----------|--------------------|-------------|--------------|
| NAMESPACE |        NAME        | TARGET PORT |     URL      |
|-----------|--------------------|-------------|--------------|
| default   | app-python-service |             | No node port |
|-----------|--------------------|-------------|--------------|
* service default/app-python-service has no node port
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
* service default/kubernetes has no node port
! Services [default/app-python-service default/kubernetes] have type "ClusterIP" not meant to be exposed, however for local development minikube allows you to access this !
* Starting tunnel for service app-python-service.
* Starting tunnel for service kubernetes.
|-----------|--------------------|-------------|------------------------|
| NAMESPACE |        NAME        | TARGET PORT |          URL           |
|-----------|--------------------|-------------|------------------------|
| default   | app-python-service |             | http://127.0.0.1:60388 |
| default   | kubernetes         |             | http://127.0.0.1:60390 |
|-----------|--------------------|-------------|------------------------|
* Opening service default/app-python-service in default browser...
* Opening service default/kubernetes in default browser...
! Because you are using a Docker driver on windows, the terminal needs to be open to run it.
```

### Open deployment:

![app_python2](assets/app_python2.png)
