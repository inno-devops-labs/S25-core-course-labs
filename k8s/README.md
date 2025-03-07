# K8S

## Deploy using `kubectl create`

```angular2html
dasha@LAPTOP-382BEF3K:~/devops/devops_labs/k8s$  kubectl create deployment python-app --image=dtolmach/python-app-monitor:latest --port=8000
deployment.apps/python-app created
dasha@LAPTOP-382BEF3K:~/devops/devops_labs/k8s$  kubectl expose deployment python-app --type=NodePort --port=80 --target-port=8000
service/python-app exposed
dasha@LAPTOP-382BEF3K:~/devops/devops_labs/k8s$  kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/python-app-7b48846ccd-pg2pj   1/1     Running   0          23s

NAME                 TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
service/kubernetes   ClusterIP   10.96.0.1      <none>        443/TCP        62m
service/python-app   NodePort    10.98.115.40   <none>        80:30907/TCP   8s
```

## Deploy with manifests

![img](/attachments/img_11.png)

![img](/attachments/img_12.png)

```angular2html
dasha@LAPTOP-382BEF3K:~/devops/devops_labs/k8s$ minikube service --all
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
|-----------|--------------------|-------------|---------------------------|
| NAMESPACE |        NAME        | TARGET PORT |            URL            |
|-----------|--------------------|-------------|---------------------------|
| default   | python-app-service |          80 | http://192.168.49.2:31377 |
|-----------|--------------------|-------------|---------------------------|
❗  Services [default/kubernetes] have type "ClusterIP" not meant to be exposed, however for local development minikube allows you to access this !
🏃  Starting tunnel for service kubernetes.
🏃  Starting tunnel for service python-app-service.
|-----------|--------------------|-------------|------------------------|
| NAMESPACE |        NAME        | TARGET PORT |          URL           |
|-----------|--------------------|-------------|------------------------|
| default   | kubernetes         |             | http://127.0.0.1:44209 |
| default   | python-app-service |             | http://127.0.0.1:44925 |
|-----------|--------------------|-------------|------------------------|
🎉  Opening service default/kubernetes in default browser...
👉  http://127.0.0.1:44209
    
```


### `kubectl get pods,svc`

![img](/attachments/img_13.png)


## Go app 

```angular2html
dasha@LAPTOP-382BEF3K:~/devops/devops_labs/k8s$ minikube service --all
|-----------|----------------|-------------|--------------|
| NAMESPACE |      NAME      | TARGET PORT |     URL      |
|-----------|----------------|-------------|--------------|
| default   | go-app-service |             | No node port |
|-----------|----------------|-------------|--------------|
😿  service default/go-app-service has no node port
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
|-----------|--------------------|-------------|--------------|
| NAMESPACE |        NAME        | TARGET PORT |     URL      |
|-----------|--------------------|-------------|--------------|
| default   | python-app-service |             | No node port |
|-----------|--------------------|-------------|--------------|
😿  service default/python-app-service has no node port
❗  Services [default/go-app-service default/kubernetes default/python-app-service] have type "ClusterIP" not meant to be exposed, however for local development  minikube allows you to access this !
🏃  Starting tunnel for service go-app-service.
🏃  Starting tunnel for service kubernetes.
🏃  Starting tunnel for service python-app-service.
|-----------|--------------------|-------------|------------------------|
| NAMESPACE |        NAME        | TARGET PORT |          URL           |
|-----------|--------------------|-------------|------------------------|
| default   | go-app-service     |             | http://127.0.0.1:37195 |
| default   | kubernetes         |             | http://127.0.0.1:36293 |
| default   | python-app-service |             | http://127.0.0.1:46037 |
|-----------|--------------------|-------------|------------------------|
🎉  Opening service default/go-app-service in default browser...
👉  http://127.0.0.1:37195
🎉  Opening service default/kubernetes in default browser...
👉  http://127.0.0.1:36293
🎉  Opening service default/python-app-service in default browser...
👉  http://127.0.0.1:46037
❗  Because you are using a Docker driver on linux, the terminal needs to be open to run it.

```

## Ingress

### Python
```angular2html
dasha@LAPTOP-382BEF3K:~/devops/devops_labs$ curl --resolve "python-app.local:80:127.0.0.1" -i http://127.0.0.1:34389
HTTP/1.1 200 OK
date: Wed, 26 Feb 2025 18:35:07 GMT
server: uvicorn
content-length: 50
content-type: application/json

{"moscow_time":"2025-02-26T21:35:08.585684+03:00"}
```

### Go

```angular2html
dasha@LAPTOP-382BEF3K:~/devops/devops_labs/k8s$ curl --resolve "go-app.local:80:127.0.0.1" -i http://127.0.0.1:8080
HTTP/1.1 200 OK
Date: Wed, 26 Feb 2025 18:37:28 GMT
Content-Length: 44
Content-Type: text/plain; charset=utf-8

{"moscow_time": "2025-02-26T21:37:28+03:00"}
```