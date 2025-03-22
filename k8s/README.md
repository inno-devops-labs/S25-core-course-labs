# Kubernetes ☸

## Setup and Basic Deployment

Use `minikube` for local cluster:

```bash
minikube start
```

Create a deployment and expose:

```bash
ebob@laptop ~ % kubectl create deployment moscow-time --image=ebob/moscow-time:v1.1
deployment.apps/moscow-time created
ebob@laptop ~ % kubectl expose deployment moscow-time --type=LoadBalancer --port=8080
service/moscow-time exposed
ebob@laptop ~ % kubectl get pods,svc
NAME                               READY   STATUS    RESTARTS   AGE
pod/moscow-time-849cb46c68-nvmcc   1/1     Running   0          27s

NAME                  TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes    ClusterIP      10.96.0.1       <none>        443/TCP          72m
service/moscow-time   LoadBalancer   10.101.142.76   127.0.0.1     8080:32533/TCP   6s
```

Verify availability:

```bash
ebob@laptop ~ % curl 127.0.0.1:8080
<html><body><h1>Current time and date in Moscow</h1><p>Time: 02:52:55</p><p>Date: 23.02.2025</p></body></html>
```

Cleanup:

```bash
ebob@laptop ~ % kubectl delete deployment moscow-time
deployment.apps "moscow-time" deleted
ebob@laptop ~ % kubectl delete svc moscow-time
service "moscow-time" deleted
ebob@laptop ~ % kubectl get pods,svc
NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   81m
```

## Declarative Kubernetes Manifests

To apply manifests, run:

```bash
kubectl apply -f deployment.yml
```

### `kubectl get pods,svc`

```bash
ebob@laptop ~ % kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/moscow-time-db47bdf76-jnv9q   1/1     Running   0          5m27s
pod/moscow-time-db47bdf76-khrbk   1/1     Running   0          5m27s
pod/moscow-time-db47bdf76-sp4xc   1/1     Running   0          5m27s

NAME                          TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
service/kubernetes            ClusterIP   10.96.0.1       <none>        443/TCP   37m
service/moscow-time-service   ClusterIP   10.110.66.123   <none>        80/TCP    5m22s
```

### `minikube service --all`

```bash
ebob@laptop ~ % minikube service --all
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
|-----------|---------------------|-------------|--------------|
| NAMESPACE |        NAME         | TARGET PORT |     URL      |
|-----------|---------------------|-------------|--------------|
| default   | moscow-time-service |             | No node port |
|-----------|---------------------|-------------|--------------|
😿  service default/moscow-time-service has no node port
❗  Services [default/kubernetes default/moscow-time-service] have type "ClusterIP" not meant to be exposed, however for local development minikube allows you to access this !
🏃  Starting tunnel for service kubernetes.
🏃  Starting tunnel for service moscow-time-service.
|-----------|---------------------|-------------|------------------------|
| NAMESPACE |        NAME         | TARGET PORT |          URL           |
|-----------|---------------------|-------------|------------------------|
| default   | kubernetes          |             | http://127.0.0.1:61906 |
| default   | moscow-time-service |             | http://127.0.0.1:61907 |
|-----------|---------------------|-------------|------------------------|
🎉  Opening service default/kubernetes in default browser...
🎉  Opening service default/moscow-time-service in default browser...
❗  Because you are using a Docker driver on darwin, the terminal needs to be open to run it.
```

Screenshot from browser:

<img width="560" alt="screenshot" src="https://github.com/user-attachments/assets/3dc62692-6418-42f2-97c9-6c2166a44531" />

## Ruby App and Ingress

Apply manifests for Ruby app:

```bash
ebob@laptop ~ % kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/moscow-time-db47bdf76-jnv9q   1/1     Running   0          22m
pod/moscow-time-db47bdf76-khrbk   1/1     Running   0          22m
pod/moscow-time-db47bdf76-sp4xc   1/1     Running   0          22m
pod/omsk-time-6f8d56f4c4-2cnbt    1/1     Running   0          6m11s
pod/omsk-time-6f8d56f4c4-t9vmq    1/1     Running   0          6m11s
pod/omsk-time-6f8d56f4c4-z6426    1/1     Running   0          6m11s

NAME                          TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
service/kubernetes            ClusterIP   10.96.0.1       <none>        443/TCP   53m
service/moscow-time-service   ClusterIP   10.110.66.123   <none>        80/TCP    21m
service/omsk-time-service     ClusterIP   10.97.58.80     <none>        80/TCP    6m3s
```

Set up Nginx Ingress Controller:

Run:

```bash
minikube addons enable ingress
```

Verify:

```bash
ebob@laptop ~ % kubectl get deployments -n ingress-nginx
NAME                       READY   UP-TO-DATE   AVAILABLE   AGE
ingress-nginx-controller   1/1     1            1           59m
```

Apply `ingress.yml` manifest:

```bash
ebob@laptop ~ % kubectl get ingress
NAME                  CLASS   HOSTS                               ADDRESS        PORTS   AGE
application-ingress   nginx   moscow-time.local,omsk-time.local   192.168.49.2   80      13m
```

Add these lines to `/etc/hosts`:

```bash
127.0.0.1 moscow-time.local
127.0.0.1 omsk-time.local
```

Then run `curl`:

```bash
ebob@laptop ~ % curl http://moscow-time.local/
<html><body><h1>Current time and date in Moscow</h1><p>Time: 02:31:36</p><p>Date: 23.02.2025</p></body></html>

ebob@laptop ~ % curl http://omsk-time.local/
Current time in Omsk: 2025-02-23 05:32:22
```

<img width="511" alt="ingress-screenshot" src="https://github.com/user-attachments/assets/b9177771-2ac5-4c1a-9a96-05118cbdd128" />
