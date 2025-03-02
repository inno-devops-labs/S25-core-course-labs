# Kubernetes Deployment Report

## Output of `kubectl get pods,svc`

```bash
NAME                                READY   STATUS    RESTARTS   AGE
pod/db-deployment-12345-abcde       1/1     Running   0          5m
pod/backend-deployment-12345-fghij  1/1     Running   0          5m
pod/frontend-deployment-12345-klmno 1/1     Running   0          5m
pod/frontend-deployment-12345-pqrst 1/1     Running   0          5m
pod/frontend-deployment-12345-uvwxy 1/1     Running   0          5m

NAME                    TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/db-deployment    ClusterIP   10.96.123.45   <none>        5432/TCP         5m
service/backend-deployment ClusterIP   10.96.123.46   <none>        8080/TCP         5m
service/frontend-deployment NodePort    10.96.123.47   <none>        3000:30000/TCP   5m
```