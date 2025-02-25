# Kubernetes Overview

## Create and Expose without manifest files

```text
PS C:\Users\egora\PycharmProjects\S25-core-course-labs\k8s> kubectl create deployment flask-app --image=rwkals/app_python_distroless --port=5000
deployment.apps/flask-app created
PS C:\Users\egora\PycharmProjects\S25-core-course-labs\k8s> kubectl expose deployment flask-app --type=NodePort --port=80 --target-port=5000
service/flask-app exposed
```

### `kubectl get pods,svc`

```text
PS C:\Users\egora\PycharmProjects\S25-core-course-labs\k8s> kubectl get pods,svc
NAME                             READY   STATUS    RESTARTS   AGE
pod/flask-app-77d7646bc7-w4f5p   1/1     Running   0          19s

NAME                 TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
service/flask-app    NodePort    10.100.68.26   <none>        80:31805/TCP   2s
service/kubernetes   ClusterIP   10.96.0.1      <none>        443/TCP        52m
```

### Define url

```text
PS C:\Users\egora\PycharmProjects\S25-core-course-labs\k8s> minikube service flask-app --url
http://127.0.0.1:61540
! Because you are using a Docker driver on windows, the terminal needs to be open to run it.
```

[Running app screenshot](screenshots/kub/app_python_running.png)

### Cleaning-up

```text
PS C:\Users\egora\PycharmProjects\S25-core-course-labs\k8s> kubectl delete deployment flask-app
PS C:\Users\egora\PycharmProjects\S25-core-course-labs\k8s> kubectl delete service flask-app
service "flask-app" deleted
```

```text
PS C:\Users\egora\PycharmProjects\S25-core-course-labs\k8s> kubectl get pods,svc
NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   76m
```

## Create and Expose with manifest files

```text
PS C:\Users\egora\PycharmProjects\S25-core-course-labs> kubectl apply -f k8s
deployment.apps/flask-deployment created
service/flask-service created
```

```text
PS C:\Users\egora\PycharmProjects\S25-core-course-labs> kubectl get pods,svc
NAME                                   READY   STATUS    RESTARTS   AGE
pod/flask-deployment-96bcc8688-22xgr   1/1     Running   0          28s
pod/flask-deployment-96bcc8688-56v5n   1/1     Running   0          28s
pod/flask-deployment-96bcc8688-v4dnw   1/1     Running   0          28s

NAME                    TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
service/flask-service   NodePort    10.97.204.102   <none>        80:30001/TCP   29s
service/kubernetes      ClusterIP   10.96.0.1       <none>        443/TCP        80m
```

```text
PS C:\Users\egora\PycharmProjects\S25-core-course-labs> minikube service --all
|-----------|---------------|------------------|---------------------------|
| NAMESPACE |     NAME      |   TARGET PORT    |            URL            |
|-----------|---------------|------------------|---------------------------|
| default   | flask-service | flask-service/80 | http://192.168.49.2:30001 |
|-----------|---------------|------------------|---------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
* service default/kubernetes has no node port
! Services [default/kubernetes] have type "ClusterIP" not meant to be exposed, however for local development minikube allows you to access this !
* Starting tunnel for service flask-service.
* Starting tunnel for service kubernetes.
|-----------|---------------|-------------|------------------------|
| NAMESPACE |     NAME      | TARGET PORT |          URL           |
|-----------|---------------|-------------|------------------------|
| default   | flask-service |             | http://127.0.0.1:62642 |
| default   | kubernetes    |             | http://127.0.0.1:62644 |
|-----------|---------------|-------------|------------------------|
* Opening service default/flask-service in default browser...
* Opening service default/kubernetes in default browser...
! Because you are using a Docker driver on windows, the terminal needs to be open to run it.
```

[Screenshot](screenshots/kub/app_python_matches.png)

## Bonus

Kotlin ktor app manifest is added in k8s as well as ingress.

Firstly, I loaded an image in minikube, then apply k8s folder again. After that `minikube addons enable ingress` and `minikube tunnel`.

```text
PS C:\Users\egora\PycharmProjects\S25-core-course-labs> kubectl get po,svc,ingress
NAME                                   READY   STATUS    RESTARTS   AGE
pod/flask-deployment-96bcc8688-65wsm   1/1     Running   0          25m
pod/flask-deployment-96bcc8688-jf2hb   1/1     Running   0          25m
pod/flask-deployment-96bcc8688-r6k9d   1/1     Running   0          25m
pod/ktor-deployment-5b489f59f5-fxzz6   1/1     Running   0          25m
pod/ktor-deployment-5b489f59f5-gvpgm   1/1     Running   0          25m

NAME                    TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/flask-service   NodePort    10.101.122.17   <none>        80:30001/TCP     25m
service/ktor-service    NodePort    10.99.30.173    <none>        8080:30002/TCP   25m
service/kubernetes      ClusterIP   10.96.0.1       <none>        443/TCP          138m

NAME                                    CLASS    HOSTS                            ADDRESS        PORTS   AGE
ingress.networking.k8s.io/app-ingress   <none>   flask-app.local,ktor-app.local   192.168.49.2   80      48m
```

Both, python and kotlin apps are available:

```text
PS C:\Users\egora\PycharmProjects\S25-core-course-labs> minikube service flask-service --url
http://127.0.0.1:65289
! Because you are using a Docker driver on windows, the terminal needs to be open to run it.
```

[Screenshot](screenshots/kub/app_python_b.png)

```text
PS C:\Users\egora\PycharmProjects\S25-core-course-labs> minikube service ktor-service --url 
http://127.0.0.1:65349
! Because you are using a Docker driver on windows, the terminal needs to be open to run it.
```

[Screenshot](screenshots/kub/app_kotlin_b.png)
