## Task 1


```bash
$ kubectl get pods,svc
NAME                                     READY   STATUS    RESTARTS        AGE
pod/app-python-deploy-6d8d477d4f-544dc   1/1     Running   0 (3m44s ago)   4m36s
pod/your-app-c4b6bd4fd-pln7f             1/1     Running   0 (28s ago)     89s

NAME                        TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
service/app-python-deploy   NodePort    10.107.113.5   <none>        80:32557/TCP   4m20s
service/kubernetes          ClusterIP   10.96.0.1      <none>        443/TCP        5m22s
service/your-app            ClusterIP   10.105.92.64   <none>        80/TCP         89s
```

## Task 2
## step 4
```bash
$ kubectl get po
NAME                                 READY   STATUS      RESTARTS      AGE
app-python-deploy-74f9584459-6zlsr   1/1     Running     1 (10m ago)   20h
app-python-deploy-74f9584459-k7f6j   1/1     Running     1 (10m ago)   20h
app-python-deploy-74f9584459-w9tp7   1/1     Running     1 (10m ago)   20h
post-install-job-trsgx               0/1     Completed   0             40s
pre-install-job-txvwf                0/1     Completed   0             65s
your-app-c4b6bd4fd-cjcqx             0/1     Running     1 (10s ago)   40s
```

```bash
$ kubectl describe po pre-install-job
Name:             pre-install-job-txvwf
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Fri, 28 Feb 2025 07:10:01 +0000
Labels:           batch.kubernetes.io/controller-uid=7aa22332-b498-45f0-9a1c-5f2e1795073d
                  batch.kubernetes.io/job-name=pre-install-job
                  controller-uid=7aa22332-b498-45f0-9a1c-5f2e1795073d
                  job-name=pre-install-job
Annotations:      <none>
Status:           Succeeded
IP:               10.244.0.15
IPs:
  IP:           10.244.0.15
Controlled By:  Job/pre-install-job
Containers:
  pre-install-container:
    Container ID:  docker://d110abeb371ce0f403bcc42734f912e2cf89a95f7e319b53355b667f0309e919
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo Pre-install job running... && sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Fri, 28 Feb 2025 07:10:03 +0000
      Finished:     Fri, 28 Feb 2025 07:10:23 +0000
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-7qcw8 (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-7qcw8:
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
  Normal  Scheduled  93s   default-scheduler  Successfully assigned default/pre-install-job-txvwf to minikube
  Normal  Pulling    93s   kubelet            Pulling image "busybox"
  Normal  Pulled     91s   kubelet            Successfully pulled image "busybox" in 2.145s (2.145s including waiting). Image size: 4269678 bytes.
  Normal  Created    91s   kubelet            Created container pre-install-container
  Normal  Started    91s   kubelet            Started container pre-install-container
```

```bash
$ kubectl describe po post-install-job
Name:             post-install-job-trsgx
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Fri, 28 Feb 2025 07:10:26 +0000
Labels:           batch.kubernetes.io/controller-uid=a32659e1-b7c0-4a42-a600-b6757fdfd4cc
                  batch.kubernetes.io/job-name=post-install-job
                  controller-uid=a32659e1-b7c0-4a42-a600-b6757fdfd4cc
                  job-name=post-install-job
Annotations:      <none>
Status:           Succeeded
IP:               10.244.0.17
IPs:
  IP:           10.244.0.17
Controlled By:  Job/post-install-job
Containers:
  post-install-container:
    Container ID:  docker://62724325248a21ce23d64b801dda61aa6f6f95b33d2cd907a6b20e6721c38a06
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo Post-install job running... && sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Fri, 28 Feb 2025 07:10:28 +0000
      Finished:     Fri, 28 Feb 2025 07:10:48 +0000
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-s5gwh (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-s5gwh:
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
  Normal  Scheduled  2m20s  default-scheduler  Successfully assigned default/post-install-job-trsgx to minikube
  Normal  Pulling    2m19s  kubelet            Pulling image "busybox"
  Normal  Pulled     2m18s  kubelet            Successfully pulled image "busybox" in 894ms (894ms including waiting). Image size: 4269678 bytes.
  Normal  Created    2m18s  kubelet            Created container post-install-container
  Normal  Started    2m18s  kubelet            Started container post-install-container
```