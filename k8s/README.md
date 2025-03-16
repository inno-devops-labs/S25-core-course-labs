```
dpttk@codenv:~/uni/devops/S25-core-course-labs$ kubectl get pods,svc
NAME                           READY   STATUS    RESTARTS   AGE
pod/web-app-59655d5d67-9bd7p   1/1     Running   0          2m8s

NAME                 TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/kubernetes   ClusterIP   10.96.0.1      <none>        443/TCP          16m
service/web-app      NodePort    10.101.74.58   <none>        5000:30110/TCP   106s
```


```
dpttk@codenv:~/uni/devops/S25-core-course-labs$ kubectl delete deployment web-app
deployment.apps "web-app" deleted
dpttk@codenv:~/uni/devops/S25-core-course-labs$ kubectl delete service web-app
service "web-app" deleted
```