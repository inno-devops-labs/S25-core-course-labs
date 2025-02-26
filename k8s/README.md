```

meowal@meowal-1-2:~/S25-core-course-labs$ kubectl create deployment msk-time-deployment --image=meowal/msk-time-app:latest
deployment.apps/msk-time-deployment created
meowal@meowal-1-2:~/S25-core-course-labs$ kubectl get deployments
NAME                  READY   UP-TO-DATE   AVAILABLE   AGE
msk-time-deployment   0/1     1            0           5s

kubectl expose deployment msk-time-deployment --type=NodePort --port=5000
service/msk-time-deployment exposed
meowal@meowal-1-2:~/S25-core-course-labs$ kubectl get svc
NAME                  TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
kubernetes            ClusterIP   10.96.0.1        <none>        443/TCP          4m40s
msk-time-deployment   NodePort    10.106.188.200   <none>        5000:32167/TCP   4s


NAME                                      READY   STATUS    RESTARTS   AGE
pod/msk-time-deployment-fb64c7cfc-5csfj   1/1     Running   0          14m
pod/msk-time-deployment-fb64c7cfc-7m4pm   1/1     Running   0          14m
pod/msk-time-deployment-fb64c7cfc-wltfr   1/1     Running   0          14m

NAME                       TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/kubernetes         ClusterIP   10.96.0.1        <none>        443/TCP          21m
service/msk-time-service   NodePort    10.105.160.200   <none>        5000:30920/TCP   14m
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
|-----------|------------------|-------------|---------------------------|
| NAMESPACE |       NAME       | TARGET PORT |            URL            |
|-----------|------------------|-------------|---------------------------|
| default   | msk-time-service |        5000 | http://192.168.49.2:30920 |
|-----------|------------------|-------------|---------------------------|
🎉  Opening service default/msk-time-service in default browser...
🏃  Starting tunnel for service kubernetes.
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | kubernetes |             | http://127.0.0.1:44545 |
|-----------|------------|-------------|------------------------|
🎉  Opening service default/kubernetes in default browser...
```
![image](https://github.com/user-attachments/assets/9da1fc68-4b95-4c0e-bc98-d1055d542534)
