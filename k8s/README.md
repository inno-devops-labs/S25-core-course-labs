NAME                         READY   STATUS    RESTARTS   AGE
pod/my-app-8c95b7794-2wh5r   1/1     Running   0          18h
pod/my-app-8c95b7794-n9twc   1/1     Running   0          18h

NAME                     TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
service/kubernetes       ClusterIP   10.96.0.1       <none>        443/TCP        18h
service/my-app-service   NodePort    10.103.24.135   <none>        80:30007/TCP   18h
