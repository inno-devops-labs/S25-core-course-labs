# Helm Setup and Chaet Creation

### helm install myapp ./myapp
```
NAME: myapp
LAST DEPLOYED: Tue Feb 25 22:17:49 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=myapp,app.kubernetes.io/instance=myapp" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT

```
### kubectl get pods,svc
```
NAME                         READY   STATUS    RESTARTS   AGE
pod/myapp-7fdbcfb478-nr68g   1/1     Running   0          74s

NAME                 TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1        <none>        443/TCP   3h43m
service/myapp        ClusterIP   10.100.242.107   <none>        80/TCP    74s
```

### minikube service --all
```
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
|-----------|-------|-------------|--------------|
| NAMESPACE | NAME  | TARGET PORT |     URL      |
|-----------|-------|-------------|--------------|
| default   | myapp |             | No node port |
|-----------|-------|-------------|--------------|
😿  service default/myapp has no node port
❗  Services [default/kubernetes default/myapp] have type "ClusterIP" not meant to be exposed, however for local development minikube allows you to access this !
🏃  Starting tunnel for service kubernetes.
🏃  Starting tunnel for service myapp.
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | kubernetes |             | http://127.0.0.1:43759 |
| default   | myapp      |             | http://127.0.0.1:43405 |
|-----------|------------|-------------|------------------------|
🎉  Opening service default/kubernetes in default browser...
🎉  Opening service default/myapp in default browser...
❗  Because you are using a Docker driver on linux, the terminal needs to be open to run it.

```

# Helm Chart Hooks

### kubectl get po
```
NAME                                READY   STATUS      RESTARTS   AGE
helm-hooks-myapp-6cbc7bd8bc-mz72k   1/1     Running     0          32s
myapp-7fdbcfb478-nr68g              1/1     Running     0          15h
post-install-job-wddjj              0/1     Completed   0          32s
preinstall-hook                     0/1     Completed   0          55s
```
### kubectl describe po preinstall-hook
```
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 26 Feb 2025 14:16:18 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.24
IPs:
  IP:  10.244.0.24
Containers:
  pre-install-container:
    Container ID:  docker://0150ac1b861d2245df7847c86c80fea815e842f91fb868f70a0eb0049c829ea5
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The pre-install hook is running && sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 26 Feb 2025 14:16:19 +0300
      Finished:     Wed, 26 Feb 2025 14:16:39 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-q5k5h (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-q5k5h:
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
  Type    Reason     Age    From               Message
  ----    ------     ----   ----               -------
  Normal  Scheduled  2m23s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     2m22s  kubelet            Container image "busybox" already present on machine
  Normal  Created    2m22s  kubelet            Created container: pre-install-container
  Normal  Started    2m22s  kubelet            Started container pre-install-container

```

### kubectl describe po post-install-job-wddjj
```
Name:             post-install-job-wddjj
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 26 Feb 2025 14:16:41 +0300
Labels:           batch.kubernetes.io/controller-uid=9d040b07-1d95-492d-9cba-14c8c63c331c
                  batch.kubernetes.io/job-name=post-install-job
                  controller-uid=9d040b07-1d95-492d-9cba-14c8c63c331c
                  job-name=post-install-job
Annotations:      <none>
Status:           Succeeded
IP:               10.244.0.26
IPs:
  IP:           10.244.0.26
Controlled By:  Job/post-install-job
Containers:
  post-install:
    Container ID:  docker://2de313aa82669268311a4f700e95177903314bb17fd8438edcc48f2b03a8be63
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo Post-install hook running; sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 26 Feb 2025 14:16:43 +0300
      Finished:     Wed, 26 Feb 2025 14:17:03 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-646g9 (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-646g9:
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
  Normal  Scheduled  8m4s  default-scheduler  Successfully assigned default/post-install-job-wddjj to minikube
  Normal  Pulling    8m3s  kubelet            Pulling image "busybox"
  Normal  Pulled     8m2s  kubelet            Successfully pulled image "busybox" in 1.417s (1.417s including waiting). Image size: 4269694 bytes.
  Normal  Created    8m2s  kubelet            Created container: post-install
  Normal  Started    8m2s  kubelet            Started container post-install
```

# Helm Chart for Java Application

kubectl get pods,svc
```
NAME                                    READY   STATUS              RESTARTS   AGE
pod/appjava-7f67fb7c47-ggl8d            0/1     ContainerCreating   0          17s
pod/appjava-7f67fb7c47-vn2j2            0/1     ContainerCreating   0          17s
pod/helm-hooks-myapp-6cbc7bd8bc-mz72k   1/1     Running             0          27m
pod/myapp-7fdbcfb478-nr68g              1/1     Running             0          16h
pod/post-install-job-wddjj              0/1     Completed           0          27m
pod/preinstall-hook                     0/1     Completed           0          27m

NAME                       TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/appjava            ClusterIP   10.106.138.50    <none>        4567/TCP         17s
service/helm-hooks-myapp   NodePort    10.109.231.41    <none>        8000:30106/TCP   27m
service/kubernetes         ClusterIP   10.96.0.1        <none>        443/TCP          20h
service/myapp              ClusterIP   10.100.242.107   <none>        80/TCP           16h
```

