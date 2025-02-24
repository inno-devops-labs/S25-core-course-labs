# Kubernetes lab

## Task 1

### Output for Pods Retrieval

#### Command:

```bash
kubectl get pods
```

#### Output:

```bash
NAME                     READY   STATUS    RESTARTS   AGE
my-app-8998f8d54-wb27s   1/1     Running   0          52m
```

### Output for Services Retrieval

#### Command:

```bash
kubectl get svc
```

#### Output:

```bash
NAME         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
kubernetes   ClusterIP   10.96.0.1      <none>        443/TCP          64m
my-app       NodePort    10.102.4.245   <none>        8080:31651/TCP   118s
```

## Task 2

### Output for Pods Retrieval

#### Command:

```bash
kubectl get pods
```

#### Output:

```bash
NAME                                READY   STATUS    RESTARTS   AGE
my-app-deployment-fd678c4d4-4rg69   1/1     Running   0          95s
my-app-deployment-fd678c4d4-8f7r8   1/1     Running   0          104s
my-app-deployment-fd678c4d4-9gpwm   1/1     Running   0          86s
```

### Output for Services Retrieval

#### Command:

```bash
kubectl get svc
```

#### Output:

```bash
NAME             TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
kubernetes       ClusterIP   10.96.0.1        <none>        443/TCP          18m
my-app-service   NodePort    10.102.176.201   <none>        8000:30007/TCP   17m
```

### Output for Minikube Services

#### Command:
```bash
minikube service --all
```

#### Output:

```bash
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
|-----------|----------------|-------------|---------------------------|
| NAMESPACE |      NAME      | TARGET PORT |            URL            |
|-----------|----------------|-------------|---------------------------|
| default   | my-app-service |        8000 | http://192.168.49.2:30007 |
|-----------|----------------|-------------|---------------------------|
❗  Services [default/kubernetes] have type "ClusterIP" not meant to be exposed, however for local development minikube allows you to access this !
🎉  Opening service default/my-app-service in default browser...
🏃  Starting tunnel for service kubernetes.
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | kubernetes |             | http://127.0.0.1:44223 |
|-----------|------------|-------------|------------------------|
🎉  Opening service default/kubernetes in default browser...
❗  Because you are using a Docker driver on linux, the terminal needs to be open to run it.

```

![](https://github.com/user-attachments/assets/00e83fe3-2532-48b3-bc17-5345bf6ffdbf)

