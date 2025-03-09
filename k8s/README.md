# Kubernetes

## Prerequisites

- `ubuntu` 24.10
- `docker` installed and configured
- `minikube` installed
- `kubectl` installed


## Installation

- Run this commands to install `minikube` and `kubectl`:

```bash 
sudo apt update
sudo snap install kubectl --classic
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

- Verify Installation:

```bash
kubectl version --client
minikube version
```

- Output:

```bash
egor@egor-100-HP:~/PycharmProjects/S25-core-course-labs$ kubectl version --client
Client Version: v1.32.2
Kustomize Version: v5.5.0

egor@egor-100-HP:~/PycharmProjects/S25-core-course-labs$ minikube version
minikube version: v1.35.0
commit: dd5d320e41b5451cdf3c01891bc4e13d189586ed-dirty
```

## Create `deployment.yaml` (Deployment) and `service.yaml` (Service)

- deployment.yaml:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-python
spec:
  replicas: 3
  selector:
    matchLabels:
      app: app-python
  template:
    metadata:
      labels:
        app: app-python
    spec:
      containers:
      - name: app-python
        image: zdragonlord1010/app-python:latest
        imagePullPolicy: IfNotPresent
        ports:
        - containerPort: 5000
      restartPolicy: Always
```

- service.yaml:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: app-python-service
spec:
  selector:
    app: app-python
  ports:
    - protocol: TCP
      port: 5000
      targetPort: 5000
  type: NodePort
```

## Prepare `docker`

- Run this commands to prepare your image
- The commands `docker tag` and `docker push` are only needed if you didn't have a `docker image` in advance.

```bash
docker login
docker tag app-python <username>/app-python:latest
docker push <username>/app-python:latest
```

- Output:

```bash
egor@egor-100-HP:~/PycharmProjects/S25-core-course-labs$ docker login

USING WEB BASED LOGIN
To sign in with credentials on the command line, use 'docker login -u <username>'

Your one-time device confirmation code is: ZGPX-SWLH
Press ENTER to open your browser or submit your device code here: https://login.docker.com/activate

Waiting for authentication in the browser…
WARNING! Your password will be stored unencrypted in /home/egor/snap/docker/2976/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credential-stores

Login Succeeded
```

- Check image on Docker Hub:

![DockerHub.jpg](Data%20for%20report/DockerHub.jpg)

## Deployment

1. Start Minikube:

```bash
minikube start
```

- Output:

```bash
egor@egor-100-HP:~/PycharmProjects/S25-core-course-labs$ minikube start
😄  minikube v1.35.0 on Ubuntu 24.10
✨  Automatically selected the docker driver. Other choices: ssh, none
📌  Using Docker driver with root privileges
👍  Starting "minikube" primary control-plane node in "minikube" cluster
🚜  Pulling base image v0.0.46 ...
💾  Downloading Kubernetes v1.32.0 preload ...
    > preloaded-images-k8s-v18-v1...:  333.57 MiB / 333.57 MiB  100.00% 4.90 Mi
    > gcr.io/k8s-minikube/kicbase...:  500.30 MiB / 500.31 MiB  100.00% 5.77 Mi
🔥  Creating docker container (CPUs=2, Memory=3700MB) ...
🐳  Preparing Kubernetes v1.32.0 on Docker 27.4.1 ...
    ▪ Generating certificates and keys ...
    ▪ Booting up control plane ...
    ▪ Configuring RBAC rules ...
🔗  Configuring bridge CNI (Container Networking Interface) ...
🔎  Verifying Kubernetes components...
    ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
🌟  Enabled addons: storage-provisioner, default-storageclass
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
egor@egor-100-HP:~/PycharmProjects/S25-core-course-labs$ kubectl config use-context minikube
Switched to context "minikube".
egor@egor-100-HP:~/PycharmProjects/S25-core-course-labs$ kubectl get nodes
NAME       STATUS   ROLES           AGE   VERSION
minikube   Ready    control-plane   62s   v1.32.0
```

2. Apply the deployment and service:

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

- Output:

```bash
egor@egor-100-HP:~/PycharmProjects/S25-core-course-labs$ kubectl apply -f k8s/deployment.yaml
deployment.apps/app-python created
egor@egor-100-HP:~/PycharmProjects/S25-core-course-labs$ kubectl apply -f k8s/service.yaml
service/app-python-service created
```

3. Verify deployment:

```bash
kubectl get pods,svc
```

- Output:

```bash
egor@egor-100-HP:~/PycharmProjects/S25-core-course-labs/k8s$ kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
app-python-88dfbdd7b-pgngl        1/1     Running   0          11h
app-python-88dfbdd7b-tldhn        1/1     Running   0          11h
app-python-88dfbdd7b-vz2pm        1/1     Running   0          11h

NAME                         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python-service   NodePort    10.106.253.237  <none>        5000:31248/TCP   2h
service/kubernetes           ClusterIP   10.96.0.1       <none>        443/TCP          10h
```

4. Application Access:

```bash
minikube service app-python-service
minikube service --all
```

- Output:

```bash
egor@egor-100-HP:~/PycharmProjects/S25-core-course-labs/k8s$ minikube service --all
|-----------|--------------------|-------------|---------------------------|
| NAMESPACE |        NAME        | TARGET PORT |            URL            |
|-----------|--------------------|-------------|---------------------------|
| default   | app-python-service |        5000 | http://192.168.49.2:31248 |
|-----------|--------------------|-------------|---------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
❗  Services [default/kubernetes] have type "ClusterIP" not meant to be exposed, however for local development minikube allows you to access this !
🎉  Opening service default/app-python-service in default browser...
🏃  Starting tunnel for service kubernetes.
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | kubernetes |             | http://127.0.0.1:44763 |
|-----------|------------|-------------|------------------------|
🎉  Opening service default/kubernetes in default browser...
❗  Because you are using a Docker driver on linux, the terminal needs to be open to run it.
```

- Content of http://192.168.49.2:31248:

![app.jpg](Data%20for%20report/app.jpg)

- Content of http://127.0.0.1:44763:

![kubernetes.jpg](Data%20for%20report/kubernetes.jpg)

## Cleanup

To delete the deployment and service:

```bash
kubectl delete -f deployment.yaml
kubectl delete -f service.yaml
minikube stop
```

