# Kubernetes

## Task 1

In this task I:

- Installed `kubectl` and `minikube`;
- Started `minikube`:
```sh
(venv) vm@vm ~/U/L/P/D/S25-core-course-labs (lab9)> minikube start
😄  minikube v1.35.0 on Ubuntu 24.04
✨  Using the virtualbox driver based on existing profile
👍  Starting "minikube" primary control-plane node in "minikube" cluster
🔄  Restarting existing virtualbox VM for "minikube" ...
🐳  Preparing Kubernetes v1.32.0 on Docker 27.4.0 ...
🔗  Configuring bridge CNI (Container Networking Interface) ...
🔎  Verifying Kubernetes components...
    ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
🌟  Enabled addons: default-storageclass, storage-provisioner
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
```
- Created `Deployment` resource for my app:
```sh
(venv) vm@vm /m/v/d/h/V/U/L/P/D/S/k8s (lab9)> kubectl create deployment python-app --image=voronm1522/devops:python-app eployment.apps/python-app created
(venv) vm@vm /m/v/d/h/V/U/L/P/D/S/k8s (lab9)> kubectl get deployments.apps 
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
python-app   1/1     1            1           45s
```
- Created `ervice` for this resourse:
```sh
(venv) vm@vm /m/v/d/h/V/U/L/P/D/S/k8s (lab9)> kubectl expose deployment python-app --port=5000 --type=LoadBalancer
service/python-app exposed
(venv) vm@vm /m/v/d/h/V/U/L/P/D/S/k8s (lab9)> kubectl get service
NAME         TYPE           CLUSTER-IP    EXTERNAL-IP   PORT(S)          AGE
kubernetes   ClusterIP      10.96.0.1     <none>        443/TCP          62m
python-app   LoadBalancer   10.107.1.18   <pending>     5000:32480/TCP   3s
```
- Checked availability:
```sh
(venv) vm@vm /m/v/d/h/V/U/L/P/D/S/k8s (lab9) [0|115]> minikube service python-app
|-----------|------------|-------------|-----------------------------|
| NAMESPACE |    NAME    | TARGET PORT |             URL             |
|-----------|------------|-------------|-----------------------------|
| default   | python-app |        5000 | http://192.168.59.100:32480 |
|-----------|------------|-------------|-----------------------------|
🎉  Opening service default/python-app in default browser...
```
![Demo](img/work_demonstration.png)
- Cleaned:
```sh
(venv) vm@vm /m/v/d/h/V/U/L/P/D/S/k8s (lab9) [0|14]> kubectl delete service python-app
service "python-app" deleted
(venv) vm@vm /m/v/d/h/V/U/L/P/D/S/k8s (lab9)> kubectl get services 
NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   152m
(venv) vm@vm /m/v/d/h/V/U/L/P/D/S/k8s (lab9)> kubectl delete deployment python-app
deployment.apps "python-app" deleted
(venv) vm@vm /m/v/d/h/V/U/L/P/D/S/k8s (lab9)> kubectl get deployments
No resources found in default namespace.
```

- Asked output:
```sh
(venv) vm@vm /m/v/d/h/V/U/L/P/D/S/k8s (lab9)> kubectl get pods,svc
NAME                             READY   STATUS    RESTARTS   AGE
pod/python-app-b88468c57-bbtpv   1/1     Running   0          57s

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          3h12m
service/python-app   LoadBalancer   10.102.41.188   <pending>     5000:30393/TCP   45s
```

## Task 2

In this task I:

- Created `python-app/deployment.yml` and applied it:
```sh
(venv) vm@vm /m/v/d/h/V/U/L/P/D/S/k8s (lab9)> kubectl apply -f python-app/deployment.yml
deployment.apps/python-app created
(venv) vm@vm /m/v/d/h/V/U/L/P/D/S/k8s (lab9)> kubectl get deployments
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
python-app   3/3     3            0           4s
```
- Created `python-app/service.yml` and applied it:
```sh
(venv) vm@vm /m/v/d/h/V/U/L/P/D/S/k8s (lab9) [0|1]> kubectl apply -f python-app/service.yml

service/python-app-service created
(venv) vm@vm /m/v/d/h/V/U/L/P/D/S/k8s (lab9)> 
(venv) vm@vm /m/v/d/h/V/U/L/P/D/S/k8s (lab9)> kubectl get services
NAME                 TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
kubernetes           ClusterIP   10.96.0.1        <none>        443/TCP    3h9m
python-app-service   ClusterIP   10.104.237.164   <none>        5000/TCP   14s
```
