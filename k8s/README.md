# Kubernetes Deployment

## Task 1: Basic Deployment

The application has been deployed using the imperative approach with `kubectl create` and `kubectl expose` commands.

### Current Status of Pods and Services

```bash
NAME                              READY   STATUS    RESTARTS   AGE
pod/python-app-665559646f-mt8br   1/1     Running   0          12s

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          3h23m
service/python-app   LoadBalancer   10.97.221.137   <pending>     8000:32085/TCP   6s
```

The deployment is running successfully with one replica, and the service is exposed as a LoadBalancer on port 8000. The application can be accessed at the `/time` endpoint.

## Task 2: Declarative Deployment

The application has been redeployed using declarative manifests (`deployment.yml` and `service.yml`).

### Current Status of Pods and Services

```bash
NAME                              READY   STATUS    RESTARTS   AGE
pod/python-app-6587847574-56zfw   1/1     Running   0          7s
pod/python-app-6587847574-j4fbk   1/1     Running   0          7s
pod/python-app-6587847574-llb5j   1/1     Running   0          7s

NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          24m
service/python-app   LoadBalancer   10.102.200.178   <pending>     8000:32602/TCP   7s
```

### Minikube Service Information

```bash
|-----------|------------|-------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | python-app |        8000 | http://192.168.49.2:32085 |
|-----------|------------|-------------|---------------------------|
```

### Service Verification

Running `minikube service --all` shows all available services and their URLs:

```bash
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|

|-----------|------------|-------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | python-app |        8000 | http://192.168.49.2:32085 |
|-----------|------------|-------------|---------------------------|

|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | kubernetes |             | http://127.0.0.1:55453 |
| default   | python-app |             | http://127.0.0.1:55454 |
|-----------|------------|-------------|------------------------|
```

Browser verification screenshots:
1. [Kubernetes Service Screenshot](kubernetes_service.png)
2. [Python App Service Screenshot](python_app_service.png)

The deployment is now running with 3 replicas as specified in the manifest, and the service is exposed as a LoadBalancer on port 8000. The application can be accessed through the minikube service URL at the `/time` endpoint. 