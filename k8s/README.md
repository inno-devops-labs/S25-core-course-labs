meowal@meowal-1-2:~/S25-core-course-labs$ kubectl get pods,svc
NAME                                       READY   STATUS    RESTARTS   AGE
pod/msk-time-deployment-579669d7d9-qz2zr   1/1     Running   0          67s

NAME                          TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/kubernetes            ClusterIP   10.96.0.1        <none>        443/TCP          5m27s
service/msk-time-deployment   NodePort    10.106.188.200   <none>        5000:32167/TCP   51s


meowal@meowal-1-2:~/S25-core-course-labs$ kubectl get pods,svc
NAME                                      READY   STATUS    RESTARTS   AGE
pod/msk-time-deployment-fb64c7cfc-5csfj   1/1     Running   0          13s
pod/msk-time-deployment-fb64c7cfc-7m4pm   1/1     Running   0          13s
pod/msk-time-deployment-fb64c7cfc-wltfr   1/1     Running   0          13s

NAME                       TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/kubernetes         ClusterIP   10.96.0.1        <none>        443/TCP          7m32s
service/msk-time-service   NodePort    10.105.160.200   <none>        5000:30920/TCP   13s
meowal@meowal-1-2:~/S25-core-course-labs$ 


meowal@meowal-1-2:~/S25-core-course-labs$ minikube service --all
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
❗  Services [default/kubernetes] have type "ClusterIP" not meant to be exposed, however for local development minikube allows you to access this !
🎉  Opening service default/msk-time-service in default browser...
🏃  Starting tunnel for service kubernetes.
Gtk-Message: 00:55:48.023: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | kubernetes |             | http://127.0.0.1:46809 |
|-----------|------------|-------------|------------------------|
🎉  Opening service default/kubernetes in default browser...
❗  Because you are using a Docker driver on linux, the terminal needs to be open to run it.
Gtk-Message: 00:55:49.095: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.




