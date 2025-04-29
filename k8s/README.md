
### Task 1
```bash

(devopss) daniilzimin@MacBook-Pro k8s % kubectl get pods,svc
NAME                              READY   STATUS              RESTARTS   AGE
pod/python-app-5c4479676f-tm87h   0/1     ContainerCreating   0          45s

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          2m23s
service/python-app   LoadBalancer   10.107.200.16   <pending>     9200:31794/TCP   26s
```


### Task2
```bash
(devopss) daniilzimin@MacBook-Pro k8s % kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-6dbf97d6c5-8b2kx   1/1     Running   0          15s
pod/app-python-6dbf97d6c5-x6lgx   1/1     Running   0          15s
pod/app-python-6dbf97d6c5-zqjsp   1/1     Running   0          15s

NAME                 TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/app-python   NodePort    10.98.129.71   <none>        9200:32458/TCP   9s
service/kubernetes   ClusterIP   10.96.0.1      <none>        443/TCP          4m23s
```


```bash
(devopss) daniilzimin@MacBook-Pro k8s % minikube service --all
|-----------|------------|-------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | app-python |        9200 | http://192.168.49.2:32458 |
|-----------|------------|-------------|---------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
❗  Services [default/kubernetes] have type "ClusterIP" not meant to be exposed, however for local development minikube allows you to access this !
🏃  Starting tunnel for service app-python.
🏃  Starting tunnel for service kubernetes.
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | app-python |             | http://127.0.0.1:51236 |
| default   | kubernetes |             | http://127.0.0.1:51238 |
|-----------|------------|-------------|------------------------|
🎉  Opening service default/app-python in default browser...
🎉  Opening service default/kubernetes in default browser...
❗  Because you are using a Docker driver on darwin, the terminal needs to be open to run it.
```

![screen](assets/k8s.png)