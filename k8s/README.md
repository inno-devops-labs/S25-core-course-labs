# Lab 9: Introduction to Kubernetes

## Task 1: Kubernetes Setup and Basic Deployment

```txt
fridorovich@DESKTOP-FRR2QTC:/home/devops/S25-core-course-labs$ kubectl create deployment --image fridorovich04/python-web:latest python-web --port 8000
deployment.apps/python-web created
```
```txt
fridorovich@DESKTOP-FRR2QTC:/home/devops/S25-core-course-labs$ kubectl expose deployment python-web --type=LoadBalancer --port=8000
service/python-web exposed
```
```txt
fridorovich@DESKTOP-FRR2QTC:/home/devops/S25-core-course-labs$ kubectl get svc
NAME         TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          13m
python-web   LoadBalancer   10.109.193.152   <pending>     8000:31542/TCP   10s
```
```txt
fridorovich@DESKTOP-FRR2QTC:/home/devops/S25-core-course-labs$ minikube service python-web
|-----------|------------|-------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | python-web |        8000 | http://192.168.49.2:31542 |
|-----------|------------|-------------|---------------------------|
🏃  Starting tunnel for service python-web.
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | python-web |             | http://127.0.0.1:63115 |
|-----------|------------|-------------|------------------------|
🎉  Opening service default/python-web in default browser...
❗  Because you are using a Docker driver on darwin, the terminal needs to be open to run it.
```
```txt
fridorovich@DESKTOP-FRR2QTC:/home/devops/S25-core-course-labs$ kubectl get pods,svc
NAME                             READY   STATUS             RESTARTS   AGE
pod/python-web-dd5db7d98-z78k6   1/1     Running            0          81s

NAME                 TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/kubernetes   ClusterIP      10.96.0.1      <none>        443/TCP          40m
service/python-web   LoadBalancer   10.100.182.3   <pending>     8000:32481/TCP   68s
```
```txt
fridorovich@DESKTOP-FRR2QTC:/home/devops/S25-core-course-labs$ kubectl delete service python-web
service "python-web" deleted
```
```txt
fridorovich@DESKTOP-FRR2QTC:/home/devops/S25-core-course-labs$ kubectl delete deployment python-web
deployment.apps "python-web" deleted
```

## Task 2: Declarative Kubernetes Manifests

```txt
fridorovich@DESKTOP-FRR2QTC:/home/devops/S25-core-course-labs/k8s$ kubectl apply -f deployment.yml
deployment.apps/python-web created
```
```txt
fridorovich@DESKTOP-FRR2QTC:/home/devops/S25-core-course-labs/k8s$ kubectl apply -f service.yml
service/python-web created
```
```txt
fridorovich@DESKTOP-FRR2QTC:/home/devops/S25-core-course-labs/k8s$ kubectl get pods,svc
NAME                              READY   STATUS         RESTARTS   AGE
pod/python-web-8497d5fcc4-4fscn   1/1     Running        0          16s
pod/python-web-8497d5fcc4-5djp8   1/1     Running        0          16s
pod/python-web-8497d5fcc4-p5pq4   1/1     Running        0          16s

NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          51m
service/python-web   LoadBalancer   10.107.221.202   <pending>     8000:30105/TCP   7s
```
```txt
fridorovich@DESKTOP-FRR2QTC:/home/devops/S25-core-course-labs/k8s$ minikube service --all
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | python-web |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/python-web  has no node port
❗  Services [default/kubernetes default/python-web] have type "ClusterIP" not meant to be exposed, however for local development minikube allows you to access this !
🏃  Starting tunnel for service kubernetes.
🏃  Starting tunnel for service python-app-service.
|-----------|--------------------|-------------|------------------------|
| NAMESPACE |        NAME        | TARGET PORT |          URL           |
|-----------|--------------------|-------------|------------------------|
| default   | kubernetes         |             | http://127.0.0.1:64230 |
| default   | python-app-service |             | http://127.0.0.1:64231 |
|-----------|--------------------|-------------|------------------------|
🎉  Opening service default/kubernetes in default browser...
🎉  Opening service default/python-web in default browser...
❗  Because you are using a Docker driver on darwin, the terminal needs to be open to run it.
```