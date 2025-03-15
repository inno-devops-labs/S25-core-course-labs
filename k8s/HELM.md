# Helm

## Task 1

### Output of `kubectl get pods,svc` command:
```
NAME                      READY   STATUS             RESTARTS      AGE
pod/app-9b5c6fd7d-6mctk   0/1     CrashLoopBackOff   6 (56s ago)   15m

NAME                 TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)   AGE
service/app          ClusterIP   10.99.83.94   <none>        80/TCP    15m
service/kubernetes   ClusterIP   10.96.0.1     <none>        443/TCP   140m
```