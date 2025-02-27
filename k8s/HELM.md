## Task 1
- Task 1.4 Screenshots:
1. ![alt text](image-8.png)
2. ![alt text](image-9.png)
- Task 1.5 Screenshot:
1. ![alt text](image-10.png)
- Task 1.6 Screenshot:
1. ![alt text](image-11.png)

## Task 2
- Task 2.4 Screenshots & Outputs:
1. ![alt text](image-12.png)
2. Preinstall hook: 
```bash
Name:             pre-install-hook-4hgzh
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Thu, 27 Feb 2025 06:09:59 +0300
Labels:           batch.kubernetes.io/controller-uid=af367a4d-423e-405c-b9bd-7b6b2e904350
                batch.kubernetes.io/job-name=pre-install-hook
                controller-uid=af367a4d-423e-405c-b9bd-7b6b2e904350
                job-name=pre-install-hook
Annotations:      <none>
Status:           Succeeded
IP:               10.244.0.5
IPs:
IP:           10.244.0.5
Controlled By:  Job/pre-install-hook
Containers:
pre-install-hook:
    Container ID:  docker://6e1e3606e2f41583f1a9772d111995cbb716abd48f18b5c6cd8491e99facc9f5
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
    sh
    -c
    echo Pre-Install Hook && sleep 20
    State:          Terminated
    Reason:       Completed
    Exit Code:    0
    Started:      Thu, 27 Feb 2025 06:10:11 +0300
    Finished:     Thu, 27 Feb 2025 06:10:31 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
    /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-v9qwq (ro)
Conditions:
Type                        Status
PodReadyToStartContainers   False 
Initialized                 True 
Ready                       False 
ContainersReady             False 
PodScheduled                True 
Volumes:
kube-api-access-v9qwq:
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
Normal  Scheduled  3m58s  default-scheduler  Successfully assigned default/pre-install-hook-4hgzh to minikube
Normal  Pulling    3m54s  kubelet            Pulling image "busybox"
Normal  Pulled     3m48s  kubelet            Successfully pulled image "busybox" in 6.453s (6.453s including waiting). Image size: 4269694 bytes.
Normal  Created    3m47s  kubelet            Created container: pre-install-hook
Normal  Started    3m46s  kubelet            Started container pre-install-hook
```
3. Postinstall hook: 
```bash
Name:             post-install-hook-2vgt6
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Thu, 27 Feb 2025 06:10:38 +0300
Labels:           batch.kubernetes.io/controller-uid=8b517141-eec5-4ac1-9ac3-6861a9484a17
                batch.kubernetes.io/job-name=post-install-hook
                controller-uid=8b517141-eec5-4ac1-9ac3-6861a9484a17
                job-name=post-install-hook
Annotations:      <none>
Status:           Succeeded
IP:               10.244.0.6
IPs:
IP:           10.244.0.6
Controlled By:  Job/post-install-hook
Containers:
post-install-hook:
    Container ID:  docker://012ab0b19576ed4f5061a5634f7b4a92754df29c3af9fcf8420d57ab89e64b43
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
    sh
    -c
    echo Post-Install Hook && sleep 20
    State:          Terminated
    Reason:       Completed
    Exit Code:    0
    Started:      Thu, 27 Feb 2025 06:10:45 +0300
    Finished:     Thu, 27 Feb 2025 06:11:06 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
    /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-sjwdp (ro)
Conditions:
Type                        Status
PodReadyToStartContainers   False 
Initialized                 True 
Ready                       False 
ContainersReady             False 
PodScheduled                True 
Volumes:
kube-api-access-sjwdp:
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
Normal  Scheduled  3m44s  default-scheduler  Successfully assigned default/post-install-hook-2vgt6 to minikube
Normal  Pulling    3m40s  kubelet            Pulling image "busybox"
Normal  Pulled     3m38s  kubelet            Successfully pulled image "busybox" in 2.603s (2.603s including waiting). Image size: 4269694 bytes.
Normal  Created    3m37s  kubelet            Created container: post-install-hook
Normal  Started    3m36s  kubelet            Started container post-install-hook
```
- Task 1.6 (After addition of hooks):
1. ![alt text](image-13.png)
