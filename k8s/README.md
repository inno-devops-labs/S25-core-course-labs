# Kubernetes

### Install cubectl and minikube.

![install_cubectl](screenshots/install_cubectl.png)
![img.png](screenshots/install_minikube.png)

### Deployment

1. Create deployment
```bash
kubectl create deployment app-python --image=darrpyy/devops:latest
deployment.apps/app-python created
```

2. Expose deployment
```bash
kubectl expose deployment app-python --port=8001 --type=LoadBalancer
service/app-python exposed
```

3. See information about deployments, pods, and service
```bash
kubectl get pods,deployments,svc

NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-85cf7b6c6d-9tfvz   1/1     Running   0          38s

NAME                         READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/app-python   1/1     1            1           38s

NAME                 TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/app-python   LoadBalancer   10.98.85.137   <pending>     8001:32425/TCP   8s
service/kubernetes   ClusterIP      10.96.0.1      <none>        443/TCP          88s
```

4. Start minikube tunnel
```bash
minikube tunnel
[sudo] password for darya: 
Status: 
        machine: minikube
        pid: 375227
        route: 10.96.0.0/12 -> 192.168.49.2
        minikube: Running
        services: [app-python]
    errors: 
                minikube: no errors
                router: no errors
                loadbalancer emulator: no errors
```

5. See information about deployments, pods, and service one more time
```bash
kubectl get pods,deployments,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-85cf7b6c6d-9tfvz   1/1     Running   0          13m

NAME                         READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/app-python   1/1     1            1           13m

NAME                 TYPE           CLUSTER-IP     EXTERNAL-IP    PORT(S)          AGE
service/app-python   LoadBalancer   10.98.85.137   10.98.85.137   8001:32425/TCP   12m
service/kubernetes   ClusterIP      10.96.0.1      <none>         443/TCP          13m
```

6. Remove deployment
```bash
kubectl delete deployment app-python
deployment.apps "app-python" deleted
```

7. Remove service
```bash
kubectl delete service app-python
service "app-python" deleted
```

8. See information about deployments, pods, and service one more time
```bash
kubectl get pods,deployments,svc
NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   41m
```

# Declarative Deployment of Python App

1. Create the deployment and service
```bash
kubectl apply -f app_python
deployment.apps/app-python created
ingress.networking.k8s.io/app-python created
service/app-python created
```

2. See information about deployments, pods, and service
```bash
kubectl get pods,deployments,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-54c4bd6d8c-8wgwp   1/1     Running   0          78s
pod/app-python-54c4bd6d8c-jjxsg   1/1     Running   0          78s
pod/app-python-54c4bd6d8c-m625m   1/1     Running   0          78s
pod/app-python-54c4bd6d8c-znxx7   1/1     Running   0          78s

NAME                         READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/app-python   4/4     4            4           78s

NAME                 TYPE           CLUSTER-IP     EXTERNAL-IP    PORT(S)          AGE
service/app-python   LoadBalancer   10.98.155.70   10.98.155.70   8001:31699/TCP   78s
service/kubernetes   ClusterIP      10.96.0.1      <none>         443/TCP          48m
```

3. Test application
```bash
curl 10.98.155.70:8001/
```

4. Test application using `minikube service --all`
```bash
minikube service --all
```

Screenshots:

5. Remove deployment
```bash
kubectl delete deployment app-python
```

6. Remove service
```bash
kubectl delete service app-python
```

7. See information about deployments, pods, and service one more time
```bash
kubectl get pods,deployments,svc
```