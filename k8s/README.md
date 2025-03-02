# Kubernetes report

## Manual deployment status

```shell
tedor49@tedor49:~/S25-core-course-labs/k8s$ minikube kubectl -- get pods,svc
NAME                          READY   STATUS    RESTARTS   AGE
pod/webapp-586757944c-5jprr   1/1     Running   0          73s

NAME                 TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/kubernetes   ClusterIP      10.96.0.1      <none>        443/TCP          89s
service/webapp       LoadBalancer   10.99.58.140   <pending>     8000:32690/TCP   68s
```

## Config file deployment status

```shell
tedor49@tedor49:~/S25-core-course-labs/k8s$ minikube kubectl -- get pods,svc
NAME                          READY   STATUS    RESTARTS   AGE
pod/webapp-58bdbd548b-2wrm2   1/1     Running   0          67s
pod/webapp-58bdbd548b-4scnk   1/1     Running   0          67s
pod/webapp-58bdbd548b-mvzrx   1/1     Running   0          67s

NAME                              TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes                ClusterIP      10.96.0.1       <none>        443/TCP          81s
service/webapp-loadbalancer-svc   LoadBalancer   10.105.159.99   <pending>     8000:32000/TCP   76s
```

```shell
tedor49@tedor49:~/S25-core-course-labs/k8s$ minikube service --all
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
|-----------|-------------------------|-------------|---------------------------|
| NAMESPACE |          NAME           | TARGET PORT |            URL            |
|-----------|-------------------------|-------------|---------------------------|
| default   | webapp-loadbalancer-svc |        8000 | http://192.168.49.2:32000 |
|-----------|-------------------------|-------------|---------------------------|
❗  Services [default/kubernetes] have type "ClusterIP" not meant to be exposed, however for local development minikube allows you to access this !
🎉  Opening service default/webapp-loadbalancer-svc in default browser...
🏃  Starting tunnel for service kubernetes.
Gtk-Message: 19:37:07.185: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | kubernetes |             | http://127.0.0.1:41989 |
|-----------|------------|-------------|------------------------|
🎉  Opening service default/kubernetes in default browser...
❗  Because you are using a Docker driver on linux, the terminal needs to be open to run it.
Gtk-Message: 19:37:08.380: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.
```


