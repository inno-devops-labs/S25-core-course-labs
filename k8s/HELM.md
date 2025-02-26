# Helm deployment

Installation after configuring

```bash
helm install app-python ./app-python/
```

```text
$ kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-786db76667-zd2kr   1/1     Running   0          2m15s

NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
service/app-python   ClusterIP   10.101.34.139   <none>        80/TCP    2m15s
service/kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP   121m
```

## Hooks

After implementing pre install and post install hooks and installing the chart

```text
$ kubectl get po
NAME                          READY   STATUS      RESTARTS   AGE
app-python-786db76667-5tnsr   1/1     Running     0          2m48s
postinstall-hook              0/1     Completed   0          2m48s
preinstall-hook               0/1     Completed   0          3m9s
```

```text
$ kubectl describe po  preinstall-hook
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 26 Feb 2025 23:59:05 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.35
IPs:
  IP:  10.244.0.35
Containers:
  pre-install-container:
    Container ID:  docker://7b65ab0afc7603eeb81bbb1b273bee7b7cfff63d1d95b4a8dd46291884d002bf
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The pre-install hook is running && sleep 19
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 26 Feb 2025 23:59:05 +0300
      Finished:     Wed, 26 Feb 2025 23:59:24 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-tthbh (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-tthbh:
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
  Normal  Scheduled  4m55s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     4m55s  kubelet            Container image "busybox" already present on machine
  Normal  Created    4m55s  kubelet            Created container: pre-install-container
  Normal  Started    4m55s  kubelet            Started container pre-install-container
```

```text
$ kubectl describe po  postinstall-hook
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 26 Feb 2025 23:59:26 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.37
IPs:
  IP:  10.244.0.37
Containers:
  post-install-container:
    Container ID:  docker://e6643686b8fc3957c90f8f3602b1fb61d41fa253b16201562fd1dd4cceb476fe
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The post-install hook is running && sleep 16
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 26 Feb 2025 23:59:30 +0300
      Finished:     Wed, 26 Feb 2025 23:59:46 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-fphs9 (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-fphs9:
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
  Normal  Scheduled  5m4s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    5m3s  kubelet            Pulling image "busybox"
  Normal  Pulled     5m    kubelet            Successfully pulled image "busybox" in 3.101s (3.101s including waiting). Image size: 4269694 bytes.
  Normal  Created    5m    kubelet            Created container: post-install-container
  Normal  Started    5m    kubelet            Started container post-install-container
```
