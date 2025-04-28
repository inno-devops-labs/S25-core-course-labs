# Flask Application Deployment in Minikube

## Deployment Steps

### 1. Start Minikube
```sh
minikube start
```
### Load the Docker Image into Minikube
```sh
minikube image load chr1st1na/app-python
```

### 3. Deploy the Application
```sh
kubectl apply -f deployment.yaml
```
### 4. Verify the Deployment
Check the status of pods and services:

```sh
kubectl get pods,svc
```
Example output:

```pgsql
svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-55ffc5b5f5-sdxrw   1/1     Running   0          7m46s

NAME                         TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
service/app-python-service   LoadBalancer   10.98.178.53   <pending>     80:30522/TCP   7m19s
service/kubernetes           ClusterIP      10.96.0.1      <none>        443/TCP        9m24s
```
### 5. Access the Application
To get the application URL:

```sh
minikube service app-python --url
```
### Task 2
```
minikube service --all
```
Output:
```|-----------|--------------------|-------------|---------------------------|
| NAMESPACE |        NAME        | TARGET PORT |            URL            |
|-----------|--------------------|-------------|---------------------------|
| default   | app-python-service |          80 | http://192.168.49.2:30522 |
|-----------|--------------------|-------------|---------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
❗  Services [default/kubernetes] have type "ClusterIP" not meant to be exposed, however for local development minikube allows you to access this !
🏃  Starting tunnel for service app-python-service.
🏃  Starting tunnel for service kubernetes.
|-----------|--------------------|-------------|------------------------|
| NAMESPACE |        NAME        | TARGET PORT |          URL           |
|-----------|--------------------|-------------|------------------------|
| default   | app-python-service |             | http://127.0.0.1:51367 |
| default   | kubernetes         |             | http://127.0.0.1:51369 |
|-----------|--------------------|-------------|------------------------|
🎉  Opening service default/app-python-service in default browser...
🎉  Opening service default/kubernetes in default browser...
❗  Because you are using a Docker driver on windows, the terminal needs to be open to run it.





```

![running](1.png)

## Cleanup
To remove the deployment and service:

```sh
kubectl delete -f deployment.yaml
```
Verify that resources are removed:

```sh
kubectl get pods,svc
```







