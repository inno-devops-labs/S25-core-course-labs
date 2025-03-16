# Kubernetes

## Outputs

First of all:

```bash
minikube start
```

Then:

```bash
$ kubectl create deployment python-node --image=muhammaduss/app-python
deployment.apps/python-node created
```

Expose to outside network:

```bash
$ kubectl expose deployment python-node --type=LoadBalancer --port=8080
service/python-node exposed
```

Run command to see pods and services:

```bash
$ kubectl get pods, svc
NAME                               READY   STATUS    RESTARTS   AGE
pod/hello-node-c74958b5d-cf9bm     1/1     Running   0          82m
pod/python-node-54cdc885f4-hvztd   1/1     Running   0          29m

NAME                  TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes    ClusterIP      10.96.0.1       <none>        443/TCP          84m
service/python-node   LoadBalancer   10.103.60.157   <pending>     8080:30364/TCP   24m
```

Cleaning up:

```bash
$ kubectl delete service python-node
service "python-node" deleted
$ kubectl delete deployment python-node
deployment.apps "python-node" deleted
```

## Declarative Manifests

After applying manifests:

```bash
$ kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-7d65fbd5bb-8lp4z   1/1     Running   0          17m
pod/app-python-7d65fbd5bb-dbfrx   1/1     Running   0          17m
pod/app-python-7d65fbd5bb-n598v   1/1     Running   0          17m

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python   LoadBalancer   10.103.126.19   <pending>     8080:32529/TCP   9m48s
service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          115m
```

```bash
$ minikube service --all
|-----------|------------|-------------|-----------------------------|
| NAMESPACE |    NAME    | TARGET PORT |             URL             |
|-----------|------------|-------------|-----------------------------|
| default   | app-python |        8080 | http://192.168.59.100:32529 |
|-----------|------------|-------------|-----------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
❗  Services [default/kubernetes] have type "ClusterIP" not meant to be exposed, however for local development minikube allows you to access this !
🎉  Opening service default/app-python in default browser...
E0302 23:30:54.918598    6916 out.go:502] unable to execute error getting ssh port: get port 22 for "minikube": virtualbox container inspect -f "'{{(index (index .NetworkSettings.Ports "22/tcp") 0).HostPort}}'" minikube: exec: "virtualbox": executable file not found in %PATH%
stdout:

stderr:
: template: error getting ssh port: get port 22 for "minikube": virtualbox container inspect -f "'{{(index (index .NetworkSettings.Ports "22/tcp") 0).HostPort}}'" minikube: exec: "virtualbox": executable file not found in %!P(string=index)ATH&{%!
(string=index of untyped nil)}stdout:

stderr:
:1:96: executing "error getting ssh port: get port 22 for \"minikube\": virtualbox container inspect -f \"'{{(index (index .NetworkSettings.Ports \"22/tcp\") 0).HostPort}}'\" minikube: exec: \"virtualbox\": executable file not found in %PATH%\nstdout:\n\nstderr:\n" at <index .NetworkSettings.Ports "22/tcp">: error calling %!s(MISSING): %!w(MISSING) - returning raw string.

❌  Exiting due to DRV_PORT_FORWARD: error getting ssh port: get port 22 for "minikube": virtualbox container inspect -f "'{{(index (index .NetworkSettings.Ports "22/tcp") 0).HostPort}}'" minikube: exec: "virtualbox": executable file not found in %PATH%
stdout:

stderr:


╭──────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                              │
│    😿  If the above advice does not help, please let us know:                                                │
│    👉  https://github.com/kubernetes/minikube/issues/new/choose                                              │
│                                                                                                              │
│    Please run `minikube logs --file=logs.txt` and attach logs.txt to the GitHub issue.                       │
│    Please also attach the following file to the GitHub issue:                                                │
│    - C:\Users\muhammad\AppData\Local\Temp\minikube_service_96f3c5459edaadebfd901c97ef0c2c90bddabf01_0.log    │
│                                                                                                              │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

Check the IP:

```bash
$ curl http://192.168.59.100:32529/time


StatusCode        : 200
StatusDescription : OK
Content           : {"time":"2025-03-02 23:39:24.723470+03:00"}
RawContent        : HTTP/1.1 200 OK
                    Content-Length: 43
                    Content-Type: application/json
                    Date: Sun, 02 Mar 2025 20:39:24 GMT
                    Server: uvicorn

                    {"time":"2025-03-02 23:39:24.723470+03:00"}
Forms             : {}
Headers           : {[Content-Length, 43], [Content-Type, application/json], [Date, Sun, 02 Mar 2025 20:39:24 GMT], [Server, uvicorn]}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : System.__ComObject
RawContentLength  : 43


```
