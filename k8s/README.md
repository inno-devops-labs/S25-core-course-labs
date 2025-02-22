# Kubernetes Setup and Basic Deployment

```bash
kubectl get pods,svc
```

**Output of the command:**

```bash
NAME                                         READY   STATUS    RESTARTS   AGE
pod/python-app-deployment-7b4664f997-4fm4g   1/1     Running   0          21s

NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   70m
```