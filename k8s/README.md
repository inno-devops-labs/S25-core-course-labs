# Kubernetes

## Installation and Setup
Ensure that `kubectl` and `minikube` are installed:
```bash
kubectl version --client
minikube version
```
Start the Minikube cluster:
```bash
minikube start
```

## Application Deployment
Deploy the application using the `kubectl create` command:
```bash
kubectl create deployment myapp --image=doryshibkova03/myapp:latest
```

## Expose Application
Create a service to expose the application:
```bash
kubectl expose deployment myapp --type=LoadBalancer --port=8000
```

## Verify Deployment and Service
List running pods and services:
```bash
kubectl get pods,svc
```
```
NAME                                    READY   STATUS             RESTARTS      AGE
pod/myapp-deployment-7b86c865fd-2p969   1/1     Running            0             16s
pod/myapp-deployment-7b86c865fd-bmbmw   1/1     Running            0             16s
pod/myapp-deployment-7b86c865fd-hf7qj   1/1     Running            0             16s

NAME                    TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/kubernetes      ClusterIP      10.96.0.1      <none>        443/TCP          29m
service/myapp-service   LoadBalancer   10.105.64.39   127.0.0.1     8000:30899/TCP   76s
```

## Cleanup
Delete the deployment and service:
```bash
kubectl delete deployment myapp
kubectl delete service myapp
```
---

# Kubernetes Manifests
```
minikube service --all
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
|-----------|---------------|-------------|---------------------------|
| NAMESPACE |     NAME      | TARGET PORT |            URL            |
|-----------|---------------|-------------|---------------------------|
| default   | myapp-service |        8000 | http://192.168.49.2:30899 |
|-----------|---------------|-------------|---------------------------|
❗  Services [default/kubernetes] have type "ClusterIP" not meant to be exposed, however for local development minikube allows you to access this !
🎉  Opening service default/myapp-service in default browser...
🏃  Starting tunnel for service kubernetes.
|-----------|---------------|-------------|------------------------|
| NAMESPACE |     NAME      | TARGET PORT |          URL           |
|-----------|---------------|-------------|------------------------|
| default   | myapp-service |             | http://127.0.0.1:30899 |
| default   | kubernetes    |             | http://127.0.0.1:37645 |
|-----------|---------------|-------------|------------------------|
🎉  Opening service default/kubernetes in default browser...
❗  Because you are using a Docker driver on linux, the terminal needs to be open to run it.
```
![alt text](https://github.com/DoryShibkova/S25-core-course-labs/blob/lab9/k8s/image2.jpg)

![alt text](https://github.com/DoryShibkova/S25-core-course-labs/blob/lab9/k8s/image1.jpg)
```
dariashib@dariashib-virtual-machine:~/S25-core-course-labs/app_python$ curl 127.0.0.1:30899
<h1>Time in Moscow</h1><p>2025-02-24 16:58:56</p>
```
---

# App Java

![alt text](https://github.com/DoryShibkova/S25-core-course-labs/blob/lab9/k8s/image3.jpg)

```
kubectl get pods,svc
NAME                                      READY   STATUS    RESTARTS   AGE
pod/appjava-deployment-5465dcb687-5dz4f   1/1     Running   0          104s
pod/appjava-deployment-5465dcb687-fvpxv   1/1     Running   0          104s
pod/appjava-deployment-5465dcb687-gm4qr   1/1     Running   0          104s

NAME                      TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)    AGE
service/appjava-service   ClusterIP   10.103.8.60   <none>        8080/TCP   93s
service/kubernetes        ClusterIP   10.96.0.1     <none>        443/TCP    13m
```
```
dariashib@dariashib-virtual-machine:~/S25-core-course-labs/app_python$ curl http://appjava.local
<h1>Time in Omsk</h1><p>2025-02-24 20:04:56</p>
```
