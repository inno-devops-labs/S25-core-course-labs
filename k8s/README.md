### Task 1

```bash
$ kubectl get pods,svc
NAME                                   READY   STATUS    RESTARTS   AGE
pod/app-python-deploy-b5bf56b5-5tllc   1/1     Running   0          3s

NAME                         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
service/app-python-service   ClusterIP   10.105.76.210   <none>        80/TCP    8s
service/kubernetes           ClusterIP   10.96.0.1       <none>        443/TCP   43m
```


### Task 2

```bash
$ kubectl get pods,svc
NAME                                   READY   STATUS    RESTARTS   AGE
pod/app-python-deploy-b5bf56b5-2mdd5   1/1     Running   0          34s
pod/app-python-deploy-b5bf56b5-f9tjd   1/1     Running   0          34s
pod/app-python-deploy-b5bf56b5-l44bv   1/1     Running   0          34s

NAME                         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
service/app-python-service   ClusterIP   10.100.11.59   <none>        80/TCP    28s
service/kubernetes           ClusterIP   10.96.0.1      <none>        443/TCP   39m
```


```bash
minikube service --all
|-----------|--------------------|-------------|---------------------------|
| NAMESPACE |        NAME        | TARGET PORT |            URL            |
|-----------|--------------------|-------------|---------------------------|
| default   | app-python-service |        5000 | http://192.168.49.2:31570 |
|-----------|--------------------|-------------|---------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
❗  Services [default/kubernetes] have type "ClusterIP" not meant to be exposed, however for local development minikube allows you to access this !
🎉  Opening service default/app-python-service in default browser...
👉  http://192.168.49.2:31570
🏃  Starting tunnel for service kubernetes.
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | kubernetes |             | http://127.0.0.1:37189 |
|-----------|------------|-------------|------------------------|
🎉  Opening service default/kubernetes in default browser...
👉  http://127.0.0.1:37189
❗  Because you are using a Docker driver on linux, the terminal needs to be open to run it.
kubectl get pods
```

![screen fom console](image.png)
![ip that is used by github code enviroment](image-1.png)