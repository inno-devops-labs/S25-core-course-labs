# Helm Setup and Chart Creation

```bash
kubectl get pods,svc
```

Output of the command:

```bash
NAME                                         READY   STATUS    RESTARTS   AGE
pod/helm-release-python-app-8c568b7f-pt4vf   1/1     Running   0          16s

NAME                              TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/helm-release-python-app   ClusterIP   10.101.30.243   <none>        8000/TCP   16s
service/kubernetes                ClusterIP   10.96.0.1       <none>        443/TCP    4d3h
```
