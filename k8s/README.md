# Introduction to Kubernetes

## Task 1: Kubernetes Setup and Basic Deployment

### Deploy Application

```bash
  > minikube start

  😄  minikube v1.35.0 on Microsoft Windows 11 Home Single Language 10.0.26100.3194 Build 26100.3194
  ✨  Using the docker driver based on existing profile
  👍  Starting "minikube" primary control-plane node in "minikube" cluster
  🚜  Pulling base image v0.0.46 ...
  🔄  Restarting existing docker container for "minikube" ...
  ❗  Failing to connect to https://registry.k8s.io/ from inside the minikube container
  💡  To pull new external images, you may need to configure a proxy: https://minikube.sigs.k8s.io/docs/reference/networking/proxy/
  🐳  Preparing Kubernetes v1.32.0 on Docker 27.4.1 ...
  🔎  Verifying Kubernetes components...
      ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
  🌟  Enabled addons: default-storageclass, storage-provisioner
  🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
```

```bash
  > kubectl create deployment app-node --image=anyarylova/app_python 

  deployment.apps/app-node created
```

```bash
  > kubectl get deployments

  NAME       READY   UP-TO-DATE   AVAILABLE   AGE
  app-node   1/1     1            1           35s
```

```bash
  > kubectl get pods   

  NAME                        READY   STATUS    RESTARTS   AGE
  app-node-787c6f5ccd-47q5w   1/1     Running   0          2m40s
```

### Access Application

```bash
  > kubectl expose deployment app-node --type=LoadBalancer --port=8000

  service/app-node exposed
```

```bash
  > kubectl get pods,svc

  NAME                            READY   STATUS    RESTARTS   AGE
  pod/app-node-8645984d45-9psfm   1/1     Running   0          6m37s

  NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
  service/app-node     LoadBalancer   10.104.55.238   <pending>     8000:32083/TCP   6m13s       
  service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          20h
```

```bash
  > minikube service app-node
  |-----------|----------|-------------|---------------------------|
  | NAMESPACE |   NAME   | TARGET PORT |            URL            |
  |-----------|----------|-------------|---------------------------|
  | default   | app-node |        8000 | http://192.168.49.2:32083 |
  |-----------|----------|-------------|---------------------------|
  🏃  Starting tunnel for service app-node.
```

### Cleanup

```bash
  > kubectl delete svc,deployments app-node

  service "app-node" deleted
  deployment.apps "app-node" deleted
```

## Task 2: Declarative Kubernetes Manifests

### Manifest Files for Application

Created a `deployment.yml` manifest file with 3 replicas:

```yaml
  apiVersion: apps/v1
  kind: Deployment
  metadata:
    name: app-python-deployment
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
          image: anyarylova/app_python:latest
          ports:
          - containerPort: 8000
```

Apply the manifest `deployment.yml`:

```bash
  > kubectl apply -f k8s/deployment.yml

  deployment.apps/app-python-deployment created
```

### Service Manifest

Developed a `service.yml` manifest file:

```yaml
  apiVersion: v1
  kind: Service
  metadata:
    name: app-python-service
  spec:
    selector:
      app: app-python
    type: NodePort
    ports:
      - protocol: TCP
        port: 8000
        targetPort: 8000
    type: LoadBalancer
```

Deploy the service manifest:

```bash
  > kubectl apply -f k8s/service.yml

  service/app-python-service created
```

### Output

```bash
  > kubectl get pods,svc

  NAME                                         READY   STATUS    RESTARTS      AGE
  pod/app-python-deployment-64759766c8-46vx2   1/1     Running   1 (42s ago)   97s
  pod/app-python-deployment-64759766c8-pk9bv   1/1     Running   1 (42s ago)   97s
  pod/app-python-deployment-64759766c8-th28p   1/1     Running   1 (42s ago)   97s

  NAME                         TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
  service/app-python-service   LoadBalancer   10.108.28.55   <pending>     8000:30488/TCP   79s
  service/kubernetes           ClusterIP      10.96.0.1      <none>        443/TCP          2d16h
```

```bash
  > minikube service --all

  |-----------|--------------------|-------------|---------------------------|
  | NAMESPACE |        NAME        | TARGET PORT |            URL            |
  |-----------|--------------------|-------------|---------------------------|
  | default   | app-python-service |        8000 | http://192.168.49.2:30488 |
  |-----------|--------------------|-------------|---------------------------|
  |-----------|------------|-------------|--------------|
  | NAMESPACE |    NAME    | TARGET PORT |     URL      |
  |-----------|------------|-------------|--------------|
  | default   | kubernetes |             | No node port |
  |-----------|------------|-------------|--------------|
  😿  service default/kubernetes has no node port
  ❗  Services [default/kubernetes] have type "ClusterIP" not meant to be exposed, however for local development minikube allows you to access this !
  🏃  Starting tunnel for service app-python-service.
  🏃  Starting tunnel for service kubernetes.
  |-----------|--------------------|-------------|------------------------|
  | NAMESPACE |        NAME        | TARGET PORT |          URL           |
  |-----------|--------------------|-------------|------------------------|
  | default   | app-python-service |             | http://127.0.0.1:64156 |
  | default   | kubernetes         |             | http://127.0.0.1:64158 |
  |-----------|--------------------|-------------|------------------------|
  🎉  Opening service default/app-python-service in default browser...
  🎉  Opening service default/kubernetes in default browser...
```
