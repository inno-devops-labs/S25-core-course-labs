# Helm app 

### Output after upgrading (I installed it previously)

```bash
Release "my-app" has been upgraded. Happy Helming!
NAME: my-app
LAST DEPLOYED: Sat Mar 15 13:31:17 2025
NAMESPACE: default
STATUS: deployed
REVISION: 6
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=my-app,app.kubernetes.io/instance=my-app" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
  ```

### Output from ```bash kubectl get pods,svc```

```bash
NAME                          READY   STATUS    RESTARTS   AGE
pod/my-app-5984f84d58-5gblx   1/1     Running   0          13s

NAME                 TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1     <none>        443/TCP   18m
service/my-app       ClusterIP   10.111.9.86   <none>        80/TCP    16m
```

### Output from kubectl describe pod

```bash
Name:             my-app-5984f84d58-5gblx
Namespace:        default
Priority:         0
Service Account:  my-app
Node:             minikube/192.168.49.2
Start Time:       Sat, 15 Mar 2025 13:31:17 +0300
Labels:           app.kubernetes.io/instance=my-app
                  app.kubernetes.io/managed-by=Helm
                  app.kubernetes.io/name=my-app
                  app.kubernetes.io/version=1.16.0
                  helm.sh/chart=my-app-0.1.0
                  pod-template-hash=5984f84d58
Annotations:      <none>
Status:           Running
IP:               10.244.0.8
IPs:
  IP:           10.244.0.8
Controlled By:  ReplicaSet/my-app-5984f84d58
Containers:
  my-app:
    Container ID:   docker://6e0856b23d9dac939269a66f1dbf3eb0945fc671aa5175fcd36b07248e7a1590
    Image:          app_python:latest
    Image ID:       docker://sha256:91fff24401005dd01d623da9b00d18deabcf5e53b6773a2f9ec0b5fbe6552b05
    Port:           80/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Sat, 15 Mar 2025 13:31:17 +0300
    Ready:          True
    Restart Count:  0
    Liveness:       http-get http://:8080/ delay=0s timeout=1s period=10s #success=1 #failure=3
    Readiness:      http-get http://:8080/ delay=10s timeout=1s period=5s #success=1 #failure=3
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-2mpbc (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       True 
  ContainersReady             True 
  PodScheduled                True 
Volumes:
  kube-api-access-2mpbc:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  27s   default-scheduler  Successfully assigned default/my-app-5984f84d58-5gblx to minikube
  Normal  Pulled     27s   kubelet            Container image "app_python:latest" already present on machine
  Normal  Created    27s   kubelet            Created container: my-app
  Normal  Started    26s   kubelet            Started container my-app
```

### Here is screenshot from minikube dashboard:

![img_2.png](img_2.png)


### Output from minikube service my-app
```bash
|-----------|--------|-------------|--------------|
| NAMESPACE |  NAME  | TARGET PORT |     URL      |
|-----------|--------|-------------|--------------|
| default   | my-app |             | No node port |
|-----------|--------|-------------|--------------|
😿  service default/my-app has no node port
❗  Services [default/my-app] have type "ClusterIP" not meant to be exposed, however for local development minikube allows you to access this !
🏃  Starting tunnel for service my-app.
|-----------|--------|-------------|------------------------|
| NAMESPACE |  NAME  | TARGET PORT |          URL           |
|-----------|--------|-------------|------------------------|
| default   | my-app |             | http://127.0.0.1:46685 |
|-----------|--------|-------------|------------------------|
🎉  Opening service default/my-app in default browser...
❗  Because you are using a Docker driver on linux, the terminal needs to be open to run it.
Gtk-Message: 13:32:52.451: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.
```

### Get pods,svc once more

```bash
NAME                          READY   STATUS    RESTARTS   AGE
pod/my-app-5984f84d58-5gblx   1/1     Running   0          7m46s

NAME                 TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1     <none>        443/TCP   25m
service/my-app       ClusterIP   10.111.9.86   <none>        80/TCP    24m
```