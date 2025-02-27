# K8S

## Task 1

### Start minikube

To start minikube I used the following script. It did not work at first, I rebooted the laptop and everything worked just fine

```bash
[justcgh9@archlinux go]$ minikube start --driver=docker
😄  minikube v1.35.0 on Arch 
✨  Using the docker driver based on existing profile
👍  Starting "minikube" primary control-plane node in "minikube" cluster
🚜  Pulling base image v0.0.46 ...
🤷  docker "minikube" container is missing, will recreate.
🔥  Creating docker container (CPUs=2, Memory=2200MB) ...
🐳  Preparing Kubernetes v1.32.0 on Docker 27.4.1 ...
    ▪ Generating certificates and keys ...
    ▪ Booting up control plane ...
    ▪ Configuring RBAC rules ...
🔗  Configuring bridge CNI (Container Networking Interface) ...
🔎  Verifying Kubernetes components...
    ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
🌟  Enabled addons: default-storageclass, storage-provisioner
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
```

### Create and start deployment

I used the following `kubectl` commands to create and expose the Moscow time app deployment. See the outputs below

```bash
$ kubectl create deployment app-python --image=justcgh/moscow-time-app-distroless:latest
deployment.apps/app-python created
```

```bash
$ kubectl expose deployment app-python --type=NodePort --port=8080
service/app-python exposed
```

```bash
minikube service app-python
```

| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | app-python |        8080 | <http://192.168.49.2:30203> |

🎉  Opening service default/app-python in default browser...

### Pods and services

Here is the output of required commands:

```bash
$ kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-55858cbc5c-69fj1   1/1     Running   0          6m33s

NAME                 TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/app-python   NodePort    10.101.232.108   <none>        8080:30203/TCP   6m33s
service/kubernetes   ClusterIP   10.96.0.1        <none>        443/TCP          88m
```

### Validate

I used `curl http://192.168.49.2:30203` with the address displayed above to verify that everything works just fine

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Moscow Time</title>
</head>
<body style="font-family: Arial, sans-serif; text-align: center; margin-top: 100px;">
    <h1>Moscow Time</h1>
    <p>The current Moscow time is:</p>
    <h2>2025-02-26 20:20:58</h2>
</body>
</html>
```

### Cleanup

You can see the procedure for cleanup that I applied:

```bash
$ kubectl delete deployment app-python
deployment.apps "app-python" deleted
$ kubectl delete service app-python
service "app-python" deleted
```

## Task 2

### Setup

I created `deployment.yml` and `service.yml`, and filled them out analagously to the first task.

### Start

It is easy to get everything up and running using `apply` command.

```bash
$ kubectl apply -f k8s/
deployment.apps/app-python created
service/app-python created
```

### Pods and services II

Here is the output of reqired commands:

```bash
$ kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-55858cbc5c-8bvx9   1/1     Running   0          13s
pod/app-python-55858cbc5c-cp28z   1/1     Running   0          13s
pod/app-python-55858cbc5c-xnx5r   1/1     Running   0          13s

NAME                 TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/app-python   NodePort    10.101.232.108   <none>        8080:32717/TCP   13s
service/kubernetes   ClusterIP   10.96.0.1        <none>        443/TCP          82m
```

### Validation

Here is the output of `minikube service --all`

```bash
minikube service --all
```

| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | app-python |        8080 | <http://192.168.49.2:32717> |

| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |

```bash
😿  service default/kubernetes has no node port
❗  Services [default/kubernetes] have type "ClusterIP" not meant to be exposed, however for local development minikube allows you to access this !
🎉  Opening service default/app-python in default browser...
🏃  Starting tunnel for service kubernetes.
```

| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | kubernetes |             | <http://127.0.0.1:33625> |

```bash
🎉  Opening service default/kubernetes in default browser...
❗  Because you are using a Docker driver on linux, the terminal needs to be open to run it.
✋  Stopping tunnel for service kubernetes.
```

![k8s](/k8s/media/k8s.png)

![moscow](/k8s/media/moscow.png)

## Bonus task

For this task I rebuilt and pushed the image of `app_python` where the exposed port is now **8081**, not 8080 as it was in the first 2 tasks.

### Go app

I created the same files for [deployment](/k8s/deployment_go.yml) and [service](/k8s/service_go.yml) of my url shortener.

### Ingress

For this part I created an ingress [file](/k8s/ingress.yml). Then I patched my `/etc/hosts` to add a mapping from `minikube ip` to the host names I have specified in the ingress file. After that I launched everything using:

```bash
$ kubectl apply -f ./k8s
deployment.apps/app-python created
deployment.apps/app-go created
ingress.networking.k8s.io/example-ingress created
service/app-python created
service/app-go created
```

Then I enabled an add-on:

```bash
$ minikube addons enable ingress
💡  ingress is an addon maintained by Kubernetes. For any concerns contact minikube on GitHub.
You can view the list of minikube maintainers at: https://github.com/kubernetes/minikube/blob/master/OWNERS
    ▪ Using image registry.k8s.io/ingress-nginx/controller:v1.11.3
    ▪ Using image registry.k8s.io/ingress-nginx/kube-webhook-certgen:v1.4.4
    ▪ Using image registry.k8s.io/ingress-nginx/kube-webhook-certgen:v1.4.4
🔎  Verifying ingress addon...
🌟  The 'ingress' addon is enabled
```

And I started the tunnel:

```bash
$ minikube tunnel
Status:
        machine: minikube
        pid: 103521
        route: 10.96.0.0/12 -> 192.168.49.2
        minikube: Running
        services: [app-go, app-python]
    errors:
                minikube: no errors
                router: no errors
                loadbalancer emulator: no errors
```

### Results

I curled both my hostnames:

```bash
curl http://go.justcgh9.app/manage
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Manage URLs</title>
    <script src="https://unpkg.com/htmx.org"></script>
</head>
<body>
    <h1>Manage Your URLs</h1>


    <form id="add-url-form" hx-post="/urls" hx-target="#url-list ul" hx-swap="beforeend" hx-trigger="submit">
        <input type="url" name="url" placeholder="Enter a URL" required>
        <input type="text" name="alias" placeholder="Optional alias">
        <button type="submit">Add URL</button>
    </form>

    <hr>


    <div id="url-list">
        <ul>

        </ul>
    </div>

</body>
</html>
```

```bash
curl http://python.justcgh9.app/
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Moscow Time</title>
</head>
<body style="font-family: Arial, sans-serif; text-align: center; margin-top: 100px;">
    <h1>Moscow Time</h1>
    <p>The current Moscow time is:</p>
    <h2>2025-02-26 22:19:14</h2>
</body>
</html>
```
