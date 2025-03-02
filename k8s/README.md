
# Lab 9: Introduction to Kubernetes

## Task 1
```
emildavlityarov@emapfff k8s % kubectl create deployment app-python --image=emapfff/app-python:latest
deployment.apps/app-python created
emildavlityarov@emapfff k8s % kubectl expose deployment app-python --type=NodePort --port=80
service/app-python exposed
emildavlityarov@emapfff k8s % minikube service app-python
|-----------|------------|-------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | app-python |          80 | http://192.168.49.2:32369 |
|-----------|------------|-------------|---------------------------|
emildavlityarov@emapfff k8s % kubectl get svc
NAME         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
app-python   NodePort    10.96.170.137   <none>        80:32369/TCP   79s
kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP        8h
emildavlityarov@emapfff k8s % kubectl get pods
NAME                          READY   STATUS             RESTARTS   AGE
app-python-6757d599c8-9s9xt   1/1     Running               0       104s
```
## Task 2 + bonus

```
emildavlityarov@emapfff k8s % kubectl get pods
NAME                          READY   STATUS    RESTARTS   AGE
app-kotlin-f48745cdc-5hmrz    1/1     Running   0          2m38s
app-kotlin-f48745cdc-srjdk    1/1     Running   0          2m38s
app-kotlin-f48745cdc-tzv96    1/1     Running   0          2m38s
app-python-67f4df6784-5srk7   1/1     Running   0          48s
app-python-67f4df6784-9tl97   1/1     Running   0          48s
app-python-67f4df6784-dkfdb   1/1     Running   0          48s

emildavlityarov@emapfff k8s % kubectl get svc
NAME         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
app-kotlin   NodePort    10.110.27.249   <none>        8080:30001/TCP   3m21s
app-python   NodePort    10.99.64.117    <none>        80:30000/TCP     3m13s
kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP          131m


emildavlityarov@emapfff k8s % minikube service --all
|-----------|------------|-------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | app-kotlin |        8080 | http://192.168.49.2:30001 |
|-----------|------------|-------------|---------------------------|
|-----------|------------|-------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | app-python |          80 | http://192.168.49.2:30000 |
|-----------|------------|-------------|---------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
* service default/kubernetes has no node port
* Starting tunnel for service app-kotlin.
* Starting tunnel for service app-python.
* Starting tunnel for service kubernetes.
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | app-kotlin |             | http://127.0.0.1:20600 |
| default   | app-python |             | http://127.0.0.1:20602 |
| default   | kubernetes |             | http://127.0.0.1:20604 |
|-----------|------------|-------------|------------------------|
* Opening service default/app-kotlin in default browser...
* Opening service default/app-python in default browser...
* Opening service default/kubernetes in default browser...
! Because you are using a Docker driver on windows, the terminal needs to be open to run it.
```