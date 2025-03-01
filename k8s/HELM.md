# Lab 10: Introduction to Helm

## Task 1: Helm Setup and Chart Creation

### Create Heml chart

`helm create app-python`

```
PS C:\Projects\University\S25\DevOps\S25-core-course-labs\k8s> helm create app-python
Creating app-python
```

`helm install app-python ./app-python`

```
PS C:\Projects\University\S25\DevOps\S25-core-course-labs\k8s> helm install app-python ./app-python
NAME: app-python
LAST DEPLOYED: Sat Mar  1 21:54:04 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  http://app-python.local/
```

`kubectl get pods,svc`

```
PS C:\Projects\University\S25\DevOps\S25-core-course-labs\k8s> kubectl get pods,svc                        
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-696b768f9d-xtl4s   1/1     Running   0          30s

NAME                 TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
service/app-python   ClusterIP   10.100.178.151   <none>        80/TCP    31s
service/kubernetes   ClusterIP   10.96.0.1        <none>        443/TCP   21m
```

### Verify Helm chart

`minikube service --all`

```
PS C:\Projects\University\S25\DevOps\S25-core-course-labs\k8s> minikube service --all                          
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | app-python |             | No node port |
|-----------|------------|-------------|--------------|
* service default/app-python has no node port
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
* service default/kubernetes has no node port
! Services [default/app-python default/kubernetes] have type "ClusterIP" not meant to be exposed, however for local development minikube allows you to access this !    
* Starting tunnel for service app-python.
* Starting tunnel for service kubernetes.
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | app-python |             | http://127.0.0.1:61249 |
| default   | kubernetes |             | http://127.0.0.1:61251 |
|-----------|------------|-------------|------------------------|
* Opening service default/app-python in default browser...
* Opening service default/kubernetes in default browser...
! Because you are using a Docker driver on windows, the terminal needs to be open to run it.
```

![app_python3](assets/app_python3.png)

![dashboard](assets/dashboard.png)