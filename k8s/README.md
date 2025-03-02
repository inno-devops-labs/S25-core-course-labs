# Kubernetes report

## Manual deployment status

```shell
tedor49@tedor49:~/S25-core-course-labs/k8s$ minikube kubectl -- get pods,svc
NAME                          READY   STATUS    RESTARTS   AGE
pod/webapp-586757944c-5jprr   1/1     Running   0          73s

NAME                 TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/kubernetes   ClusterIP      10.96.0.1      <none>        443/TCP          89s
service/webapp       LoadBalancer   10.99.58.140   <pending>     8000:32690/TCP   68s
```
