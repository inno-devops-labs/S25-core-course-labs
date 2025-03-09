# Helm report

## Without hooks

```shell
tedor49@tedor49:~/S25-core-course-labs/k8s$ minikube kubectl -- get pods,svc
NAME                                         READY   STATUS              RESTARTS   AGE
pod/webapp-python-msk-time-8f4cf445c-ndn9k   0/1     ContainerCreating   0          24s

NAME                             TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE
service/kubernetes               ClusterIP   10.96.0.1      <none>        443/TCP    39s
service/webapp-python-msk-time   ClusterIP   10.106.82.92   <none>        8000/TCP   25s
```

## With hooks

```shell
tedor49@tedor49:~/S25-core-course-labs/k8s$ minikube kubectl -- get po
NAME                                         READY   STATUS      RESTARTS   AGE
helm-hooks-python-msk-time-549454c49-v68nb   1/1     Running     0          91s
postinstall-hook                             0/1     Completed   0          91s
preinstall-hook                              0/1     Completed   0          2m3s

```

```shell
tedor49@tedor49:~/S25-core-course-labs/k8s$ minikube kubectl -- describe po preinstall-hook
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.58.2
Start Time:       Sun, 02 Mar 2025 21:43:56 +0500
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.3
IPs:
  IP:  10.244.0.3
Containers:
  pre-install-container:
    Container ID:  docker://101a0578193ef4b9c14c2b0d52a4932bda9675aa6fab5940dc6ebbddf225477c
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
      Started:      Sun, 02 Mar 2025 21:44:06 +0500
      Finished:     Sun, 02 Mar 2025 21:44:26 +0500
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-64thl (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-64thl:
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
  Normal  Scheduled  2m22s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulling    2m21s  kubelet            Pulling image "busybox"
  Normal  Pulled     2m12s  kubelet            Successfully pulled image "busybox" in 8.789s (8.789s including waiting). Image size: 4269694 bytes.
  Normal  Created    2m12s  kubelet            Created container pre-install-container
  Normal  Started    2m12s  kubelet            Started container pre-install-container

```

```shell
tedor49@tedor49:~/S25-core-course-labs/k8s$ minikube kubectl -- describe po postinstall-hook
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.58.2
Start Time:       Sun, 02 Mar 2025 21:44:28 +0500
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.5
IPs:
  IP:  10.244.0.5
Containers:
  post-install-container:
    Container ID:  docker://2f67f1c32f9744a7f9c46b979b65aa4ba2e46633bab4d9cc688c65375d59e0ae
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
      Started:      Sun, 02 Mar 2025 21:44:45 +0500
      Finished:     Sun, 02 Mar 2025 21:45:00 +0500
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-8wzb5 (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-8wzb5:
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
  Normal  Scheduled  2m16s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    2m15s  kubelet            Pulling image "busybox"
  Normal  Pulled     119s   kubelet            Successfully pulled image "busybox" in 2.033s (16.333s including waiting). Image size: 4269694 bytes.
  Normal  Created    119s   kubelet            Created container post-install-container
  Normal  Started    119s   kubelet            Started container post-install-container

```



