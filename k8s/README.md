## K8s

The output of the command `kubectl get pods,svc`
```
kubectl get pods,svc
NAME                                          READY   STATUS    RESTARTS   AGE
pod/moscow-time-deployment-6bcbb8d58c-7nw7n   1/1     Running   0          3m1s
pod/moscow-time-deployment-6bcbb8d58c-jcsp7   1/1     Running   0          3m1s
pod/moscow-time-deployment-6bcbb8d58c-pqcnv   1/1     Running   0          3m1s

NAME                          TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes            ClusterIP   10.96.0.1       <none>        443/TCP          2d14h
service/moscow-time-service   NodePort    10.103.54.240   <none>        8000:30768/TCP   2d12h
```
The output of the command `minikube service --all`
```
minikube service --all
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
|-----------|---------------------|-------------|---------------------------|
| NAMESPACE |        NAME         | TARGET PORT |            URL            |
|-----------|---------------------|-------------|---------------------------|
| default   | moscow-time-service |        8000 | http://192.168.49.2:30768 |
|-----------|---------------------|-------------|---------------------------|
❗  Services [default/kubernetes] have type "ClusterIP" not meant to be exposed, however for local development minikube allows you to access this !
🎉  Opening service default/moscow-time-service in default browser...
🏃  Starting tunnel for service kubernetes.
Opening in existing browser session.
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | kubernetes |             | http://127.0.0.1:42235 |
|-----------|------------|-------------|------------------------|
🎉  Opening service default/kubernetes in default browser...
❗  Because you are using a Docker driver on linux, the terminal needs to be open to run it.
Opening in existing browser session.
```

The ip mathcing screenshot.
![minicuve](/k8s/media/minicube-image.png)


The application is accessible from outside.
![app](/k8s//media/app-image.png)