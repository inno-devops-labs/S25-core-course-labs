# Helm Deployment

## Task 1: Helm Setup and Chart Creation

Output of `kubectl get pods,svc`:

```
NAME                                               READY   STATUS    RESTARTS   AGE
pod/moscow-time-api-56d97f7c6d-29slv               1/1     Running   0          41m
pod/moscow-time-api-56d97f7c6d-tkl2t               1/1     Running   0          41m
pod/moscow-time-api-56d97f7c6d-tkn88               1/1     Running   0          41m
pod/moscow-time-moscow-time-app-794cfc6b74-fnrxg   1/1     Running   0          16s

NAME                                  TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                         AGE
service/kubernetes                    ClusterIP   10.96.0.1        <none>        443/TCP                         73m
service/moscow-time-api               NodePort    10.110.251.95    <none>        8001:31894/TCP,8000:31925/TCP   41m
service/moscow-time-moscow-time-app   NodePort    10.111.138.238   <none>        8001:32550/TCP,8000:31153/TCP   16s
```

The Moscow Time application is accessible via:
- Application endpoint: http://192.168.49.2:32550
- Metrics endpoint: http://192.168.49.2:31153

## Task 2: Helm Chart Hooks

We implemented both pre-install and post-install hooks for our Helm chart. Both hooks simply sleep for 20 seconds and include hook delete policies to automatically remove them after successful execution.

### Output of `kubectl get po`:
```
NAME                                                      READY   STATUS      RESTARTS   AGE
helm-hooks-example-moscow-time-app-dc5946c98-5ztsx        1/1     Running     0          65s
helm-hooks-example-moscow-time-app-post-install-example   0/1     Completed   0          41s
helm-hooks-example-moscow-time-app-pre-install-example    0/1     Completed   0          89s
helm-hooks-moscow-time-app-5d4fcfc74f-6jpd9               1/1     Running     0          2m54s
moscow-time-api-56d97f7c6d-29slv                          1/1     Running     0          46m
moscow-time-api-56d97f7c6d-tkl2t                          1/1     Running     0          46m
moscow-time-api-56d97f7c6d-tkn88                          1/1     Running     0          46m
moscow-time-moscow-time-app-794cfc6b74-fnrxg              1/1     Running     0          5m34s
```

### Output of `kubectl describe po helm-hooks-example-moscow-time-app-pre-install-example`:
```
Name:             helm-hooks-example-moscow-time-app-pre-install-example
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sat, 01 Mar 2025 19:21:11 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
                  helm.sh/hook-weight: 0
Status:           Succeeded
IP:               10.244.0.21
IPs:
  IP:  10.244.0.21
Containers:
  pre-install-job:
    Container ID:  docker://6e7db81bebe4fd8f2839fd7140f71fd9b6e85a15b691f4c8ab9df2d9987d42f2
    Image:         busybox:latest
    Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
      /bin/sh
      -c
      echo Pre-install hook started; sleep 20; echo Pre-install hook completed
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Sat, 01 Mar 2025 19:21:13 +0300
      Finished:     Sat, 01 Mar 2025 19:21:33 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-xnls2 (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-xnls2:
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
  Normal  Scheduled  93s   default-scheduler  Successfully assigned default/helm-hooks-example-moscow-time-app-pre-install-example to minikube
  Normal  Pulling    93s   kubelet            Pulling image "busybox:latest"
  Normal  Pulled     91s   kubelet            Successfully pulled image "busybox:latest" in 1.575s (1.575s including waiting). Image size: 4269694 bytes.
  Normal  Created    91s   kubelet            Created container: pre-install-job
  Normal  Started    91s   kubelet            Started container pre-install-job
```

### Output of `kubectl describe po helm-hooks-example-moscow-time-app-post-install-example`:
```
Name:             helm-hooks-example-moscow-time-app-post-install-example
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sat, 01 Mar 2025 19:21:59 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
                  helm.sh/hook-weight: 0
Status:           Succeeded
IP:               10.244.0.24
IPs:
  IP:  10.244.0.24
Containers:
  post-install-job:
    Container ID:  docker://cd03a375fd23aacd4c6569b29f6d69fc3fbe951f3a3dbb5c5acd4049f85974d1
    Image:         busybox:latest
    Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
      /bin/sh
      -c
      echo Post-install hook started; sleep 20; echo Post-install hook completed
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Sat, 01 Mar 2025 19:22:02 +0300
      Finished:     Sat, 01 Mar 2025 19:22:22 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-6v85c (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-6v85c:
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
  Normal  Scheduled  50s   default-scheduler  Successfully assigned default/helm-hooks-example-moscow-time-app-post-install-example to minikube
  Normal  Pulling    49s   kubelet            Pulling image "busybox:latest"
  Normal  Pulled     47s   kubelet            Successfully pulled image "busybox:latest" in 1.681s (1.681s including waiting). Image size: 4269694 bytes.
  Normal  Created    47s   kubelet            Created container: post-install-job
  Normal  Started    47s   kubelet            Started container post-install-job
```

### Implementation of Hook Delete Policy

We implemented the hook delete policy in our pre-install.yaml and post-install.yaml files with the annotation:
```yaml
"helm.sh/hook-delete-policy": hook-succeeded
```

This ensures that the hook pods are automatically deleted after they've successfully completed their execution, keeping our cluster clean.