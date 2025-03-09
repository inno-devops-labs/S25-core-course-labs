# Introduction to Helm

## Task 1: Helm Setup and Chart Creation

### Output

```bash
  > minikube service app-python-helm

  | NAMESPACE |      NAME       | TARGET PORT |          URL           |
  |-----------|-----------------|-------------|------------------------|
  | default   | app-python-helm |             | http://127.0.0.1:50612 |
  |-----------|-----------------|-------------|------------------------|
  🎉  Opening service default/app-python-helm in default browser...
```

```bash
  > kubectl get pods,svc
  
  NAME                                   READY   STATUS    RESTARTS   AGE
  pod/app-python-helm-5d6c47db5d-97pwt   1/1     Running   0          104s

  NAME                      TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
  service/app-python-helm   ClusterIP   10.106.240.107   <none>        80/TCP    104s
  service/kubernetes        ClusterIP   10.96.0.1        <none>        443/TCP   2d17h
```

## Task 2: Helm Chart Hooks

### Output

```bash
  > kubectl get po  

  NAME                                         READY   STATUS      RESTARTS   AGE
  app-python-helm-5d6c47db5d-66kbg             1/1     Running     0          8m58s
  helm-hooks-app-python-helm-6b964dfd8-tbwfr   1/1     Running     0          4m15s
  helm-hooks-app-python-helm-postinstall       0/1     Completed   0          4m15s
  helm-hooks-app-python-helm-preinstall        0/1     Completed   0          4m39s
```

```bash
  > kubectl describe po helm-hooks-app-python-helm-preinstall 
  
  Name:             helm-hooks-app-python-helm-preinstall
  Namespace:        default
  Priority:         0
  Service Account:  default
  Node:             minikube/192.168.49.2
  Start Time:       Sat, 01 Mar 2025 22:09:55 +0300
  Labels:           <none>
  Annotations:      helm.sh/hook: pre-install
                    helm.sh/hook-delete-policy: before-hook-creation
  Status:           Succeeded
  IP:               10.244.0.45
  IPs:
    IP:  10.244.0.45
  Containers:
    preinstall:
      Container ID:  docker://47ca4a1480166a80b0c7c1ab471dab7b4c655eca60b6fd80b75e3941483fd72e
      Image:         busybox
      Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
      Port:          <none>
      Host Port:     <none>
      Command:
        sh
        -c
        sleep 20
      State:          Terminated
        Reason:       Completed
        Exit Code:    0
        Started:      Sat, 01 Mar 2025 22:09:57 +0300
        Finished:     Sat, 01 Mar 2025 22:10:18 +0300
      Ready:          False
      Restart Count:  0
      Environment:    <none>
      Mounts:
        /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-xsqp2 (ro)
  Conditions:
    Type                        Status
    PodReadyToStartContainers   False
    Initialized                 True
    Ready                       False
    ContainersReady             False
    PodScheduled                True
  Volumes:
    kube-api-access-xsqp2:
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
    Normal  Scheduled  8m7s  default-scheduler  Successfully assigned default/helm-hooks-app-python-helm-preinstall to minikube
    Normal  Pulling    8m8s  kubelet            Pulling image "busybox"
    Normal  Pulled     8m6s  kubelet            Successfully pulled image "busybox" in 1.886s (1.886s including waiting). Image size: 4269694 bytes.
    Normal  Created    8m6s  kubelet            Created container: preinstall
    Normal  Started    8m6s  kubelet            Started container preinstall
```

```bash
  > kubectl describe po helm-hooks-app-python-helm-postinstall

  Name:             helm-hooks-app-python-helm-postinstall
  Namespace:        default
  Priority:         0
  Service Account:  default
  Node:             minikube/192.168.49.2
  Start Time:       Sat, 01 Mar 2025 22:10:19 +0300
  Labels:           <none>
  Annotations:      helm.sh/hook: post-install
                    helm.sh/hook-delete-policy: before-hook-creation
  Status:           Succeeded
  IP:               10.244.0.47
  IPs:
    IP:  10.244.0.47
  Containers:
    post-install:
      Container ID:  docker://9e25e077e3fc02d3cd341058907ddc7162b5a6f7789c18007d36c6f9106b073a
      Image:         busybox
      Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
      Port:          <none>
      Host Port:     <none>
      Command:
        sh
        -c
        sleep 20
      State:          Terminated
        Reason:       Completed
        Exit Code:    0
        Started:      Sat, 01 Mar 2025 22:10:22 +0300
        Finished:     Sat, 01 Mar 2025 22:10:42 +0300
      Ready:          False
      Restart Count:  0
      Environment:    <none>
      Mounts:
        /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-dd2fq (ro)
  Conditions:
    Type                        Status
    PodReadyToStartContainers   False
    Initialized                 True
    Ready                       False
    ContainersReady             False
    PodScheduled                True
  Volumes:
    kube-api-access-dd2fq:
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
    Normal  Scheduled  5m22s  default-scheduler  Successfully assigned default/helm-hooks-app-python-helm-postinstall to minikube
    Normal  Pulling    5m21s  kubelet            Pulling image "busybox"
    Normal  Pulled     5m19s  kubelet            Successfully pulled image "busybox" in 1.636s (1.636s including waiting). Image size: 4269694 bytes.
    Normal  Created    5m19s  kubelet            Created container: post-install
    Normal  Started    5m19s  kubelet            Started container post-install
```
