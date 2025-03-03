# Kubernetes

Pods and services:

```bash
➜  k8s git:(lab9) ✗ kubectl get pods,services
NAME                                      READY   STATUS    RESTARTS   AGE
pod/timeapp-deployment-77d7cc66b4-lckqt   1/1     Running   0          7m15s
pod/timeapp-deployment-77d7cc66b4-sspq6   1/1     Running   0          7m15s
pod/timeapp-deployment-77d7cc66b4-zmrhm   1/1     Running   0          7m15s

NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP    7m56s
service/timeapp      ClusterIP   10.98.244.162   10.90.121.6   8080/TCP   4m53s
```

Deployment and app availablility:

![deployment](./images/deploy.png)

![browser](./images/browser.png)