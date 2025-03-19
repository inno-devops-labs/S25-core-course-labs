<h1>HELM.md</h1>
The outputs of the HELM commands


`kubectl get pods,svc`
```
NAME                                         READY   STATUS    RESTARTS        AGE
pod/python-msk-789787bb98-5nfh7              1/1     Running   0               5m19s
pod/python-msk-deployment-868c89fdfd-csrf2   1/1     Running   1 (8m21s ago)   8m49s
pod/python-msk-deployment-868c89fdfd-kmpkj   1/1     Running   1 (8m21s ago)   8m49s
pod/python-msk-deployment-868c89fdfd-srrmn   1/1     Running   1 (8m21s ago)   8m49s
NAME                         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
service/kubernetes           ClusterIP   10.96.0.1        <none>        443/TCP        4d7h
service/python-msk           ClusterIP   10.97.171.40     <none>        80/TCP         5m19s
service/python-msk-service   NodePort    10.103.189.134   <none>        80:31551/TCP   2d14h
```

`kubectl get po`
```
NAME                                     READY   STATUS      RESTARTS      AGE
nginx-statefulset-0                      1/1     Running     0             78s
postinstall-hook                         0/1     Completed   0             78s
preinstall-hook                          0/1     Completed   0             103s
python-msk-deployment-868c89fdfd-csrf2   1/1     Running     2 (16m ago)   2d17h
python-msk-deployment-868c89fdfd-kmpkj   1/1     Running     2 (16m ago)   2d17h
python-msk-deployment-868c89fdfd-srrmn   1/1     Running     2 (16m ago)   2d17h
```

Pre-install Hook Pod (preinstall-hook)
```
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 04 Mar 2025 12:43:39 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.75
IPs:
  IP:  10.244.0.75
Containers:
  pre-install-container:
    Container ID:  docker://f835f3d41958769ee94be305df54c4a4313988e67d6db61798651294ea967cf3
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
      Started:      Tue, 04 Mar 2025 12:43:41 +0300
      Finished:     Tue, 04 Mar 2025 12:44:01 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-vqqz9 (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-vqqz9:
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
  Normal  Scheduled  2m16s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     2m15s  kubelet            Container image "busybox" already present on machine
  Normal  Created    2m14s  kubelet            Created container: pre-install-container
  Normal  Started    2m14s  kubelet            Started container pre-install-container
```

Post-install Hook Pod (postinstall-hook)
```
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 04 Mar 2025 12:44:04 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.76
IPs:
  IP:  10.244.0.76
Containers:
  post-install-container:
    Container ID:  docker://8cb63a911fff6a9386d592f45960876531befcd877c3ba97bc87ae31d2e84322
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
      Started:      Tue, 04 Mar 2025 12:44:09 +0300
      Finished:     Tue, 04 Mar 2025 12:44:24 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-mxjcg (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-mxjcg:
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
  Normal  Scheduled  118s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    116s  kubelet            Pulling image "busybox"
  Normal  Pulled     113s  kubelet            Successfully pulled image "busybox" in 3.565s (3.566s including waiting). Image size: 4269694 bytes.
  Normal  Created    113s  kubelet            Created container: post-install-container
  Normal  Started    113s  kubelet            Started container post-install-container
```