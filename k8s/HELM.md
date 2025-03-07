# Helm Deployment Status

## Pods and Services Output

```bash

fory@pop-os:~/devops-labs/S25-core-course-labs/k8s$ kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/python-app-7fd9468b5c-7cqpf   1/1     Running   0          5m39s

NAME                 TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1      <none>        443/TCP   99m
service/python-app   ClusterIP   10.96.206.61   <none>        80/TCP    5m39s

```

## `kubectl get po`

```bash
fory@pop-os:~/devops-labs/S25-core-course-labs/k8s$ kubectl get po
NAME                          READY   STATUS    RESTARTS   AGE
python-app-7fd9468b5c-7cqpf   1/1     Running   0          13m
```

## Preinstall Hook

```bash
fory@pop-os:~/devops-labs/S25-core-course-labs/k8s$ kubectl describe po pre-install-hook
Name:             pre-install-hook-t2qpz
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 26 Feb 2025 18:11:45 +0300
Labels:           batch.kubernetes.io/controller-uid=9d6adda0-dea3-4c70-97b0-f0ce77db221c
                  batch.kubernetes.io/job-name=pre-install-hook
                  controller-uid=9d6adda0-dea3-4c70-97b0-f0ce77db221c
                  job-name=pre-install-hook
Annotations:      <none>
Status:           Succeeded
IP:               10.244.0.13
IPs:
  IP:           10.244.0.13
Controlled By:  Job/pre-install-hook
Containers:
  pre-install:
    Container ID:  docker://5ef6913a49245d34fcb21e319636f99c43489f99cc25fdf746a1cdb7457b97e3
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo 'Pre-install hook running...'; sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 26 Feb 2025 18:11:50 +0300
      Finished:     Wed, 26 Feb 2025 18:12:10 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-bwkrn (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-bwkrn:
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
  Normal  Scheduled  100s  default-scheduler  Successfully assigned default/pre-install-hook-t2qpz to minikube
  Normal  Pulling    100s  kubelet            Pulling image "busybox"
  Normal  Pulled     96s   kubelet            Successfully pulled image "busybox" in 4.016s (4.016s including waiting). Image size: 4269694 bytes.
  Normal  Created    96s   kubelet            Created container: pre-install
  Normal  Started    96s   kubelet            Started container pre-install

```


## Postinstall Hook

```bash
fory@pop-os:~/devops-labs/S25-core-course-labs/k8s$ kubectl describe po post-install-hook
Name:             post-install-hook-fshxs
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 26 Feb 2025 18:12:12 +0300
Labels:           batch.kubernetes.io/controller-uid=88b0a9b8-d996-4ddb-8531-d7507744dc97
                  batch.kubernetes.io/job-name=post-install-hook
                  controller-uid=88b0a9b8-d996-4ddb-8531-d7507744dc97
                  job-name=post-install-hook
Annotations:      <none>
Status:           Succeeded
IP:               10.244.0.14
IPs:
  IP:           10.244.0.14
Controlled By:  Job/post-install-hook
Containers:
  post-install:
    Container ID:  docker://c4eb60212351d0b7733c88d2147569120d24f3f8b5b4213537b8654be0ec7f94
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo 'Post-install hook running...'; sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 26 Feb 2025 18:12:14 +0300
      Finished:     Wed, 26 Feb 2025 18:12:34 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-5x9bz (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-5x9bz:
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
  Normal  Scheduled  2m    default-scheduler  Successfully assigned default/post-install-hook-fshxs to minikube
  Normal  Pulling    2m    kubelet            Pulling image "busybox"
  Normal  Pulled     119s  kubelet            Successfully pulled image "busybox" in 1.36s (1.36s including waiting). Image size: 4269694 bytes.
  Normal  Created    119s  kubelet            Created container: post-install
  Normal  Started    119s  kubelet            Started container post-install
```
