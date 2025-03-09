# Kubernetes

## Task 1

### Output of `kubectl get pods,svc` command:
```
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-5966d8b75d-2k5dw   1/1     Running   0          2m44s

NAME                 TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/app-python   NodePort    10.96.94.175   <none>        8090:31291/TCP   2m38s
service/kubernetes   ClusterIP   10.96.0.1      <none>        443/TCP          5m13s
```