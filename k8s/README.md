# Kubernetes Guide

## Deploying Applications in Kubernetes

Kubernetes allows to deploy and manage containerized applications efficiently. This section covers the basic steps to create and expose a deployment.

* Creating a Deployment

Use the following command to create a deployment for a Python application:

```shell
kubectl create deployment app-python --image=maksalena/server_app:latest     
deployment.apps/app-python created
```

* Checking Deployments

To list all existing deployments, run:

```shell
kubectl get deployments
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
app-python   1/1     1            1           5m11s
```

* Exposing a Deployment as a Service

Expose the deployment to allow external access using a LoadBalancer service:

```shell
kubectl expose deployment app-python --type=LoadBalancer --port=8080
service/app-python exposed
```

* Listing Pods and Services

Check the running pods and services with:

```shell
kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-6f49cdf4b8-vch5n   1/1     Running   0          10m

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python   LoadBalancer   10.99.169.216   <pending>     8080:31152/TCP   2m18s
service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          11m

```

* Cleaning Up Resources

To delete services and deployments, use:

```shell
kubectl delete svc python-service go-service
kubectl delete deployment --all
```

## Declarative Approach to Kubernetes Deployment

Instead of creating resources imperatively, define them in YAML files and apply them declaratively.

* Applying Configuration Manifests

Apply deployment and service configurations from YAML files:

```shell
kubectl apply -f app_python/deployment.yaml
deployment.apps/python-deployment created
kubectl apply -f app_python/service.yaml
service/python-service created

```

* Checking Deployed Resources

Verify that pods and services are running:

```shell
kubectl get pods,svc
NAME                                    READY   STATUS    RESTARTS   AGE
pod/python-deployment-cf645b767-4r8jm   1/1     Running   0          38s
pod/python-deployment-cf645b767-7j4hx   1/1     Running   0          38s
pod/python-deployment-cf645b767-ksgct   1/1     Running   0          38s

NAME                     TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python       LoadBalancer   10.99.169.216   <pending>     8080:31152/TCP   17m
service/kubernetes       ClusterIP      10.96.0.1       <none>        443/TCP          25m
service/python-service   LoadBalancer   10.111.209.63   <pending>     8080:31584/TCP   20s

```

* Checking Service Availability

To view service URLs using Minikube, execute:

```shell
minikube service --all
|-----------|------------|-------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | app-python |        8080 | http://192.168.49.2:31152 |
|-----------|------------|-------------|---------------------------|

```
