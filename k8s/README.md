# Kubernetes

## Task 1: Kubernetes Setup and Basic Deployment

### Deploying the application

Create a basic deployment with `kubectl create`:

```sh
kubectl create deployment app-python --image=my-python-app
```

### Creating deployment

```sh
$ kubectl create deployment app-python --image=shelma13/app_python:latest
deployment.apps/app-python created

$ kubectl expose deployment app-python --type=LoadBalancer --port=5000
service/app-python exposed

$ kubectl get pods,svc
```

![Deployment](images/Screenshot%20from%202025-02-25%2022-00-12.png)

### Deleting deployment

```sh
$ kubectl delete deployment app-python
deployment.apps "app-python" deleted

$ kubectl delete service app-python
service "app-python" deleted

$ kubectl get pods,svc
NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   24m
```

## Task 2: Declarative Kubernetes Manifests

```sh
$ kubectl apply -f deployment.yml
deployment.apps/app-python created

$ kubectl apply -f service.yml
service/app-python created
```

![Own deployment](images/Screenshot%20from%202025-02-25%2022-15-46.png)

```sh
$ kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-5467f97795-mnztk   1/1     Running   0          3m9s
pod/app-python-5467f97795-ncgfz   1/1     Running   0          3m9s
pod/app-python-5467f97795-xwrrq   1/1     Running   0          3m9s

NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/app-python   LoadBalancer   10.106.225.152   <pending>     5000:30794/TCP   2m21s
service/kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          39m
```

![Output](images/Screenshot%20from%202025-02-25%2022-17-33.png)

![site1](images/Screenshot%20from%202025-02-25%2022-22-27.png)
![site2](images/Screenshot%20from%202025-02-25%2022-22-33.png)

### Minikube services

```sh
$ minikube service --all
|-----------|------------|-------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | app-python |        5000 | http://192.168.49.2:30646 |
|-----------|------------|-------------|---------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
❗  Services [default/kubernetes] have type "ClusterIP" not meant to be exposed, however for local development minikube allows you to access this !
🎉  Opening service default/app-python in default browser...
🏃  Starting tunnel for service kubernetes.
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | kubernetes |             | http://127.0.0.1:33553 |
|-----------|------------|-------------|------------------------|
🎉  Opening service default/kubernetes in default browser...
❗  Because you are using a Docker driver on linux, the terminal needs to be open to run it.
```

![Output](images/Screenshot%20from%202025-02-25%2022-27-31.png)

### Enabling Ingress
```sh
$ minikube addons enable ingress
```

And after that...
```sh
$ curl http://192.168.49.2:30646/
<h1>Current Time in Moscow:</h1><p>2025-02-26 01:53:46</p>
```
![Time](images/Screenshot%20from%202025-02-25%2022-54-04.png)
