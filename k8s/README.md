# Kubernetes

## Task 1

In this task I:

- Installed `kubectl` and `minikube`;
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
