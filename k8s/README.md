# Lab 9: Introduction to Kubernetes | Mametov Eldar

This report details the steps I took to successfully complete Lab 9, learning the fundamentals of Kubernetes, and also the steps for completing the bonus task.

## Task 1: Kubernetes Setup and Basic Deployment

To complete the first task, focusing on Kubernetes setup and basic deployment, I reviewed all the provided documentation. I followed the guide's steps to install kubectl and minikube. Then, I created a resource for my application, which I named `web-app`. For the initial example, I used `python-web-app`. (Later, for the extra application, I renamed the files and now have two files for python and golang web applications).

To confirm the successful deployment of the application, I am attaching the output of `kubectl get pods,svc`:
```
lekski@LAPTOP-EA8M0FT5:/mnt/c/Users/Honor/Desktop/S25-core-course-labs$ kubectl get pods,svc
NAME                        READY   STATUS    RESTARTS   AGE
pod/myapp-f7f7669fd-cdwtn   1/1     Running   0          46s

NAME                 TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/kubernetes   ClusterIP   10.96.0.1      <none>        443/TCP          83s
service/myapp        NodePort    10.108.77.51   <none>        8000:31814/TCP   8s
lekski@LAPTOP-EA8M0FT5:/mnt/c/Users/Honor/Desktop/S25-core-course-labs$ minikube ip
192.168.49.2
```


I also verified the web application's functionality using curl: 
```
lekski@LAPTOP-EA8M0FT5:/mnt/c/Users/Honor/Desktop/S25-core-course-labs/k8s$ curl 192.168.49.2:31814
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="./static/css/main.css">
        <title>Moscow</title>
    </head>
    <body>
        <div class="time">
            <h1 id='main_text'>MSC Time</h1>
            <h1 id='msc-time'>23-02-2025 19:53:55</h1>
        </div>
    </body>
</html>
```

## Task 2: Declarative Kubernetes Manifests
For the second task, focusing on declarative Kubernetes manifests, I read the specified documentation in the task description and created service.yml for my web application (named it python-service.yml).

Below you can see the console output and screenshots confirming the completion of the second task:
```
lekski@LAPTOP-EA8M0FT5:/mnt/c/Users/Honor/Desktop/S25-core-course-labs$ kubectl get pods,svc
NAME                                            READY   STATUS    RESTARTS   AGE
pod/python-web-app-deployment-89f558595-gn5cf   1/1     Running   0          2m39s
pod/python-web-app-deployment-89f558595-h894z   1/1     Running   0          2m39s
pod/python-web-app-deployment-89f558595-x9rns   1/1     Running   0          2m39s

NAME                             TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/kubernetes               ClusterIP   10.96.0.1        <none>        443/TCP          179m
service/python-web-app-service   NodePort    10.106.233.164   <none>        8000:31028/TCP   2m38s
```

```
lekski@LAPTOP-EA8M0FT5:/mnt/c/Users/Honor/Desktop/S25-core-course-labs$ minikube service --all
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
|-----------|------------------------|-------------|---------------------------|
| NAMESPACE |          NAME          | TARGET PORT |            URL            |
|-----------|------------------------|-------------|---------------------------|
| default   | python-web-app-service |        8000 | http://192.168.49.2:31028 |
|-----------|------------------------|-------------|---------------------------|
❗  Services [default/kubernetes] have type "ClusterIP" not meant to be exposed, however for local development minikube allows you to access this !
🏃  Starting tunnel for service kubernetes.
🏃  Starting tunnel for service python-web-app-service.
|-----------|------------------------|-------------|------------------------|
| NAMESPACE |          NAME          | TARGET PORT |          URL           |
|-----------|------------------------|-------------|------------------------|
| default   | kubernetes             |             | http://127.0.0.1:34289 |
| default   | python-web-app-service |             | http://127.0.0.1:39701 |
|-----------|------------------------|-------------|------------------------|
🎉  Opening service default/kubernetes in default browser...
👉  http://127.0.0.1:34289
🎉  Opening service default/python-web-app-service in default browser...
👉  http://127.0.0.1:39701
❗  Because you are using a Docker driver on linux, the terminal needs to be open to run it.
```

Screenshot of the application running:
![alt text](image.png)

## Bonus Task: Additional Configuration and Ingress

For the bonus task, involving additional configuration and Ingress, I repeated all the steps I performed previously for my Python web application, but this time I did it for my additional application in golang. I don't see the point in demonstrating its functionality again, as the code was analogous, so it's logical.

Then, following the guide (the link to which is provided in the task), I wrote ingress.yml and tested it. Below are the commands demonstrating the ingress functionality:

```
</html>lekski@LAPTOP-EA8M0FT5:/mnt/c/Users/Honor/Desktop/S25-core-course-labs$ kubectl get ingress web-apps-ingress
NAME               CLASS    HOSTS                                       ADDRESS        PORTS   AGE
web-apps-ingress   <none>   python-web-app.local,golang-web-app.local   192.168.49.2   80      25m
```

```
lekski@LAPTOP-EA8M0FT5:/mnt/c/Users/Honor/Desktop/S25-core-course-labs$ curl http://python-web-app.local
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="./static/css/main.css">
        <title>Moscow</title>
    </head>
    <body>
        <div class="time">
            <h1 id='main_text'>MSC Time</h1>
            <h1 id='msc-time'>24-02-2025 10:13:47</h1>
        </div>
    </body>
</html>
```

```
lekski@LAPTOP-EA8M0FT5:/mnt/c/Users/Honor/Desktop/S25-core-course-labs$ curl http://golang-web-app.local
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="./static/css/main.css">
        <title>RandNumber web application</title>
    </head>
    <body>
        <div class="number">
            <h1 id='main_text'>Random Number:</h1>
            <h1 id='main_text'>63</h1>
            <button onclick="location.reload()">Refresh Page</button>
        </div>
    </body>
</html>
```
As you can see, ingress is working correctly, and I can access my web applications through specified hostnames.