```bash
minikube kubectl get pods,svc
```

```bash
NAME                              READY   STATUS    RESTARTS   AGE
pod/python-app-78c89c85c9-d5cdc   1/1     Running   0          6m4s

NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP   6m41s
service/python-app   ClusterIP   10.109.86.228   <none>        80/TCP    6m4s
```

### helm-hooks

```bash
minikube kubectl get po
```

```bash
NAME                                    READY   STATUS      RESTARTS   AGE
helm-hooks-python-app-7b5c667bb-47vhn   1/1     Running     0          73s
postinstall-hook                        0/1     Completed   0          73s
preinstall-hook                         0/1     Completed   0          102s
```

```bash
minikube kubectl describe po preinstall-hook
```

```bash
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sun, 02 Mar 2025 18:30:30 +0000
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.3
IPs:
  IP:  10.244.0.3
Containers:
  pre-install-container:
    Container ID:  docker://dc65f4948777bdada7b0d62dd1fa158450e5099a036dfc1215932cebc8981145
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
      Started:      Sun, 02 Mar 2025 18:30:36 +0000
      Finished:     Sun, 02 Mar 2025 18:30:57 +0000
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-jksjt (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-jksjt:
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
  Normal  Scheduled  4m6s   default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulling    4m5s   kubelet            Pulling image "busybox"
  Normal  Pulled     4m     kubelet            Successfully pulled image "busybox" in 5.676s (5.676s including waiting). Image size: 4269694 bytes.
  Normal  Created    4m     kubelet            Created container: pre-install-container
  Normal  Started    3m59s  kubelet            Started container pre-install-container
```

```bash
minikube kubectl describe po postinstall-hook
```

```bash
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sun, 02 Mar 2025 18:30:59 +0000
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.5
IPs:
  IP:  10.244.0.5
Containers:
  post-install-container:
    Container ID:  docker://b8724e828ddc402012894fa54395b0b2ca4a5f8772444381df76ad3ecbffa32d
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The post-install hook is running && sleep 15
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Sun, 02 Mar 2025 18:31:14 +0000
      Finished:     Sun, 02 Mar 2025 18:31:29 +0000
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-w4ncp (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-w4ncp:
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
  Normal  Scheduled  4m23s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    4m21s  kubelet            Pulling image "busybox"
  Normal  Pulled     4m8s   kubelet            Successfully pulled image "busybox" in 1.733s (12.383s including waiting). Image size: 4269694 bytes.
  Normal  Created    4m8s   kubelet            Created container: post-install-container
  Normal  Started    4m8s   kubelet            Started container post-install-container
```