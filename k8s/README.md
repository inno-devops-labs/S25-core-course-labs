# Kubernetes Setup and Basic Deployment
```bash
sg@sg-BBR-WAX9:~$ minikube start
😄  minikube v1.35.0 на Ubuntu 22.04
E0225 12:36:17.181130   10853 start.go:812] api.Load failed for minikube: filestore "minikube": Docker machine "minikube" does not exist. Use "docker-machine ls" to list machines. Use "docker-machine create" to add a new one.
✨  Используется драйвер docker на основе существующего профиля
👍  Starting "minikube" primary control-plane node in "minikube" cluster
🚜  Pulling base image v0.0.46 ...
    > index.docker.io/kicbase/sta...:  500.31 MiB / 500.31 MiB  100.00% 17.33 M
❗  minikube was unable to download gcr.io/k8s-minikube/kicbase:v0.0.46, but successfully downloaded docker.io/kicbase/stable:v0.0.46@sha256:fd2d445ddcc33ebc5c6b68a17e6219ea207ce63c005095ea1525296da2d1a279 as a fallback image
🔥  Creating docker container (CPUs=2, Memory=2200MB) ...

🧯  Docker is nearly out of disk space, which may cause deployments to fail! (85% of capacity). You can pass '--force' to skip this check.
💡  Предложение: 

    Try one or more of the following to free up space on the device:
    
    1. Run "docker system prune" to remove unused Docker data (optionally with "-a")
    2. Increase the storage allocated to Docker for Desktop by clicking on:
    Docker icon > Preferences > Resources > Disk Image Size
    3. Run "minikube ssh -- docker system prune" if using the Docker container runtime
🍿  Related issue: https://github.com/kubernetes/minikube/issues/9024

🐳  Подготавливается Kubernetes v1.32.0 на Docker 27.4.1 ...
    ▪ Generating certificates and keys ...
    ▪ Booting up control plane ...
    ▪ Configuring RBAC rules ...
🔗  Configuring bridge CNI (Container Networking Interface) ...
🔎  Компоненты Kubernetes проверяются ...
    ▪ Используется образ gcr.io/k8s-minikube/storage-provisioner:v5
🌟  Включенные дополнения: storage-provisioner, default-storageclass
🏄  Готово! kubectl настроен для использования кластера "minikube" и "default" пространства имён по умолчанию
```
## Creating deployment
```bash
sg@sg-BBR-WAX9:~$ kubectl create deployment my-django-app --image=g1l1a/my-django-app:v2.4
deployment.apps/my-django-app created
```

## Creating service
```bash
sg@sg-BBR-WAX9:~$ kubectl expose deployment my-django-app --type=NodePort --port=8000
service/my-django-app exposed
```
```bash
sg@sg-BBR-WAX9:~$ kubectl get services
NAME            TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
kubernetes      ClusterIP   10.96.0.1        <none>        443/TCP          87m
my-django-app   NodePort    10.111.212.137   <none>        8000:31075/TCP   35s
```
## App's respose
```bash
sg@sg-BBR-WAX9:~$ minikube service my-django-app
|-----------|---------------|-------------|---------------------------|
| NAMESPACE |     NAME      | TARGET PORT |            URL            |
|-----------|---------------|-------------|---------------------------|
| default   | my-django-app |        8000 | http://192.168.49.2:31075 |
|-----------|---------------|-------------|---------------------------|
```
```bash
sg@sg-BBR-WAX9:~$ curl http://192.168.49.2:31075 
<h1>Current Time in Moscow: 2025-02-25 14:07:20</h1>
```
## View pods and services
```bash
sg@sg-BBR-WAX9:~$ kubectl get pods,svc
NAME                                 READY   STATUS    RESTARTS   AGE
pod/my-django-app-594476dd76-9mpnp   1/1     Running   0          31s

NAME                    TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/kubernetes      ClusterIP   10.96.0.1      <none>        443/TCP          94m
service/my-django-app   NodePort    10.100.8.134   <none>        8000:31775/TCP   5s
```

## Clean up
```bash
sg@sg-BBR-WAX9:~$ kubectl delete service my-django-app
service "my-django-app" deleted
sg@sg-BBR-WAX9:~$ kubectl delete deployment my-django-app
deployment.apps "my-django-app" deleted
```

# Declarative Kubernetes Manifests

## Creating Manifest Files
```bash
sg@sg-BBR-WAX9:~/DevOps/S25-core-course-labs/k8s$ kubectl apply -f python-app-deployment.yml
deployment.apps/my-django-app created
sg@sg-BBR-WAX9:~/DevOps/S25-core-course-labs/k8s$ kubectl apply -f python-app-service.yml
service/my-django-app created
```

## View pods and services
```bash
sg@sg-BBR-WAX9:~/DevOps/S25-core-course-labs/k8s$ kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/my-django-app-69cb667-2xzsc   1/1     Running   0          2m42s
pod/my-django-app-69cb667-q2fdh   1/1     Running   0          2m42s
pod/my-django-app-69cb667-sg2nn   1/1     Running   0          2m42s

NAME                    TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes      ClusterIP   10.96.0.1       <none>        443/TCP          4h24m
service/my-django-app   NodePort    10.98.209.136   <none>        8082:32721/TCP   2m24s
```
## All services
```bash
sg@sg-BBR-WAX9:~/DevOps/S25-core-course-labs/k8s$ minikube service --all
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
|-----------|---------------|--------------------|---------------------------|
| NAMESPACE |     NAME      |    TARGET PORT     |            URL            |
|-----------|---------------|--------------------|---------------------------|
| default   | my-django-app | my-django-app/8082 | http://192.168.49.2:32721 |
|-----------|---------------|--------------------|---------------------------|
❗  Services [default/kubernetes] have type "ClusterIP" not meant to be exposed, however for local development minikube allows you to access this !
🎉  Opening service default/my-django-app in default browser...
🏃  Starting tunnel for service kubernetes.
Окно или вкладка откроются в текущем сеансе браузера.
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | kubernetes |             | http://127.0.0.1:40645 |
|-----------|------------|-------------|------------------------|
🎉  Opening service default/kubernetes in default browser...
❗  Because you are using a Docker driver on linux, the terminal needs to be open to run it.
Окно или вкладка откроются в текущем сеансе браузера.
```
![Screenshot](image.png)

# Bonus Task
## Creating deployment and service manifests for dart app
```bash
sg@sg-BBR-WAX9:~/DevOps/S25-core-course-labs/k8s$ kubectl apply -f dart-app-deplo
yment.yml
deployment.apps/my-dart-app created
sg@sg-BBR-WAX9:~/DevOps/S25-core-course-labs/k8s$ kubectl apply -f dart-app-servi
ce.yml
service/my-dart-app created
```
## View pods, services and ingress
```bash
(venv) sg@sg-BBR-WAX9:~/DevOps/S25-core-course-labs/k8s$ kubectl get pods,svc,ingress
NAME                               READY   STATUS    RESTARTS       AGE
pod/my-dart-app-75dcc6cc48-5rm5d   1/1     Running   13 (22m ago)   60m
pod/my-dart-app-75dcc6cc48-kt87l   1/1     Running   13 (23m ago)   60m
pod/my-dart-app-75dcc6cc48-s4klk   1/1     Running   13 (23m ago)   60m
pod/my-django-app-69cb667-2xzsc    1/1     Running   0              73m
pod/my-django-app-69cb667-q2fdh    1/1     Running   0              73m
pod/my-django-app-69cb667-sg2nn    1/1     Running   0              73m

NAME                    TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/kubernetes      ClusterIP   10.96.0.1        <none>        443/TCP          5h34m
service/my-dart-app     NodePort    10.101.222.145   <none>        8081:32742/TCP   59m
service/my-django-app   NodePort    10.98.209.136    <none>        8082:32721/TCP   72m

NAME                                CLASS   HOSTS                           ADDRESS        PORTS   AGE
ingress.networking.k8s.io/ingress   nginx   pythonapp.local,dartapp.local   192.168.49.2   80      88s
```
## my-django-app
```bash
sg@sg-BBR-WAX9:~/DevOps/S25-core-course-labs/k8s$ curl --resolve "pythonapp.local:80:192.168.49.2" -i http://pythonapp.local
HTTP/1.1 200 OK
Date: Tue, 25 Feb 2025 15:40:32 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 52
Connection: keep-alive
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin
Cross-Origin-Opener-Policy: same-origin

<h1>Current Time in Moscow: 2025-02-25 18:40:32</h1>
```
## my-dart-app
```bash
sg@sg-BBR-WAX9:~/DevOps/S25-core-course-labs/k8s$ curl --resolve "dartapp.local:80:192.168.49.2" -i http://dartapp.local
HTTP/1.1 200 OK
Date: Tue, 25 Feb 2025 15:38:39 GMT
Content-Type: text/html
Content-Length: 1223
Connection: keep-alive
Last-Modified: Tue, 25 Feb 2025 14:28:36 GMT
ETag: "67bdd394-4c7"
Accept-Ranges: bytes

<!DOCTYPE html>
<html>
<head>
  <!--
    If you are serving your web app in a path other than the root, change the
    href value below to reflect the base path you are serving from.

    The path provided below has to start and end with a slash "/" in order for
    it to work correctly.

    For more details:
    * https://developer.mozilla.org/en-US/docs/Web/HTML/Element/base

    This is a placeholder for base href that will be replaced by the value of
    the `--base-href` argument provided to `flutter build`.
  -->
  <base href="/">

  <meta charset="UTF-8">
  <meta content="IE=Edge" http-equiv="X-UA-Compatible">
  <meta name="description" content="A new Flutter project.">

  <!-- iOS meta tags & icons -->
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black">
  <meta name="apple-mobile-web-app-title" content="nothern_lights_app">
  <link rel="apple-touch-icon" href="icons/Icon-192.png">

  <!-- Favicon -->
  <link rel="icon" type="image/png" href="favicon.png"/>

  <title>nothern_lights_app</title>
  <link rel="manifest" href="manifest.json">
</head>
<body>
  <script src="flutter_bootstrap.js" async></script>
</body>
</html>
```