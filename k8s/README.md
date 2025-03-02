# Kubernetes Deployment


## Kubernetes Setup and Basic Deployment

```bash
kubectl create deployment python-app --image=emiliogain/my-python-app:latest
```
```bash
kubectl get deployments
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
python-app   1/1     1            1           98s
```
```bash
kubectl expose deployment python-app --type=NodePort --port=5000
service/python-app exposed
```

Check that the app is running:
```bash
minikube service python-app --url
http://127.0.0.1:56788
❗  Because you are using a Docker driver on darwin, the terminal needs to be open to run it.
```
```bash
minikube service python-app
|-----------|------------|-------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | python-app |        5000 | http://192.168.49.2:32038 |
|-----------|------------|-------------|---------------------------|
🏃  Starting tunnel for service python-app.
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | python-app |             | http://127.0.0.1:56922 |
|-----------|------------|-------------|------------------------|
🎉  Opening service default/python-app in default browser...
```
`kubectl get pods,svc` output:
```bash
NAME                             READY   STATUS    RESTARTS   AGE
pod/python-app-d8775df8f-sptml   1/1     Running   0          5m54s

NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP          6m23s
service/python-app   NodePort    10.111.45.143   <none>        5000:32038/TCP   2m22s
```

Cleanup:
```bash
❯ kubectl delete deployment python-app
deployment.apps "python-app" deleted
❯ kubectl delete service python-app
service "python-app" deleted
```

## Declarative Kubernetes Manifests

```bash
❯ kubectl apply -f .
deployment.apps/python-app created
service/python-app created
```

```bash
❯ kubectl get pods,svc
NAME                             READY   STATUS    RESTARTS   AGE
pod/python-app-6699cf56b-9tp9n   1/1     Running   0          50s
pod/python-app-6699cf56b-d66qm   1/1     Running   0          50s
pod/python-app-6699cf56b-rcq9z   1/1     Running   0          50s

NAME                 TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)        AGE
service/kubernetes   ClusterIP   10.96.0.1     <none>        443/TCP        25m
service/python-app   NodePort    10.107.42.4   <none>        80:31037/TCP   50s
```

```bash
❯ minikube service --all
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
|-----------|------------|-------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | python-app |          80 | http://192.168.49.2:31037 |
|-----------|------------|-------------|---------------------------|
❗  Services [default/kubernetes] have type "ClusterIP" not meant to be exposed, however for local development minikube allows you to access this !
🏃  Starting tunnel for service kubernetes.
🏃  Starting tunnel for service python-app.
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | kubernetes |             | http://127.0.0.1:57224 |
| default   | python-app |             | http://127.0.0.1:57226 |
|-----------|------------|-------------|------------------------|
🎉  Opening service default/kubernetes in default browser...
🎉  Opening service default/python-app in default browser...
❗  Because you are using a Docker driver on darwin, the terminal needs to be open to run it.
```

![python-app](k8s0.png)
![kubernetes](k8s1.png)