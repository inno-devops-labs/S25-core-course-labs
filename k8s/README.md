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
