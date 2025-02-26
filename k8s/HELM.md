# Helm deployment

Installation after configuring

```bash
helm install app-python ./app-python/
```

```text
$ kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-786db76667-zd2kr   1/1     Running   0          2m15s

NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
service/app-python   ClusterIP   10.101.34.139   <none>        80/TCP    2m15s
service/kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP   121m
```
