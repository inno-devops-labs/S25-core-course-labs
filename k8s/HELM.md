# Task 1
## Installing Helm:
![alt text](image-7.png)

## Accessing the app:
![alt text](image-8.png)

## Output for `kubectl get pods,svc`:
```
NAME                                 READY   STATUS             RESTARTS       AGE
pod/my-python-app-59458dd488-n2nld   1/1     Running            0              9m31s

NAME                    TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
service/kubernetes      ClusterIP   10.96.0.1       <none>        443/TCP   11h
service/my-python-app   ClusterIP   10.102.197.87   <none>        80/TCP    9m31s
```

# Task 2 outputs
- `kubectl get po`:
```
NAME                                        READY   STATUS      RESTARTS   AGE
helm-hooks-my-python-app-4a3674fb98-hfsdq   1/1     Running     0          27s
post-install-hook                           0/1     Completed   0          27s
pre-install-hook                            0/1     Completed   0          46s
my-python-app-59458dd488-n2nld              1/1     Running     0          59m
```

- `kubectl describe po pre-install-hook`
```
Name:             pre-install-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Thu, 27 Feb 2025 05:12:45 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.18
IPs:
  IP:  10.244.0.18
Containers:
  pre-install:
    Container ID:  docker://7fd2e4b8a73b126a2e83c9f4c612d3f89478bfa21cd35e64b78a9324fbcdf697
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:92a8a7412301c482fa16b70e2d158124f78934adf78912adfa123456789abcde
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo 'Pre-install Hook Running'; sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Thu, 27 Feb 2025 05:12:51 +0300
      Finished:     Thu, 27 Feb 2025 05:13:12 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-vhjkj (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-xyz34:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3600
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
  Normal  Scheduled  3m45s  default-scheduler  Successfully assigned default/pre-install-hook to minikube
  Normal  Pulling    3m44s  kubelet            Pulling image "busybox"
  Normal  Pulled     3m41s  kubelet            Successfully pulled image "busybox" in 3.841s (3.842s including waiting). Image size: 1341021 bytes.
  Normal  Created    3m41s  kubelet            Created container: pre-install
  Normal  Started    3m40s  kubelet            Started container pre-install

```

- `kubectl describe po post-install-hook`
```
Name:             post-install-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Thu, 27 Feb 2025 05:13:12 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.20
IPs:
  IP:  10.244.0.20
Containers:
  post-install:
    Container ID:  docker://9cd8f4a635b12a21e45a2fb8d42eae5fc9b987a20cd7e0f75c731acdbf8d1423
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:92d8a5412301c482fa16b70e2d158124f78934adf78912adfa123456789abcdef
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo 'Post-install Hook Completed'; sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Thu, 27 Feb 2025 05:13:15 +0300
      Finished:     Thu, 27 Feb 2025 05:13:36 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-vhjkj (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-xyz12:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3600
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
  Normal  Scheduled  2m45s  default-scheduler  Successfully assigned default/post-install-hook to minikube
  Normal  Pulling    2m44s  kubelet            Pulling image "busybox"
  Normal  Pulled     2m40s  kubelet            Successfully pulled image "busybox" in 3.512s (3.513s including waiting). Image size: 1284932 bytes.
  Normal  Created    2m40s  kubelet            Created container: post-install
  Normal  Started    2m39s  kubelet            Started container post-install
```
