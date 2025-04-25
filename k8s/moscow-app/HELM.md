## get pods

```bash
tjann@fedora:~$ kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS      AGE
pod/moscow-app-57dc557498-bwc5x   1/1     Running   2 (23m ago)   149m

NAME                 TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE
service/kubernetes   ClusterIP   10.96.0.1      <none>        443/TCP    4h39m
service/moscow-app   ClusterIP   10.110.38.20   <none>        5005/TCP   148m
tjann@fedora:~$ 
```

## kubectl get po

```bash
tjann@fedora:~/DevOps-Course/k8s/moscow-app$ kubectl get po
NAME               READY   STATUS      RESTARTS   AGE
postinstall-hook   0/1     Completed   0          69s
preinstall-hook    0/1     Completed   0          91s
tjann@fedora:~/DevOps-Course/k8s/moscow-app$ 
```


## Preinstall Description

```bash
tjann@fedora:~/DevOps-Course/k8s/moscow-app$ kubectl describe po preinstall-hook 
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Fri, 25 Apr 2025 04:42:43 -0400
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.27
IPs:
  IP:  10.244.0.27
Containers:
  pre-install-container:
    Container ID:  docker://b1bb43104aecf81aa276a30ef60274c9c4563942c62fa29bf97ebe98b0e4ac00
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:37f7b378a29ceb4c551b1b5582e27747b855bbfaa73fa11914fe0df028dc581f
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The pre-install hook is running && sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Fri, 25 Apr 2025 04:42:43 -0400
      Finished:     Fri, 25 Apr 2025 04:43:04 -0400
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-hsqp7 (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-hsqp7:
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
  Normal  Scheduled  2m53s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     2m54s  kubelet            Container image "busybox" already present on machine
  Normal  Created    2m54s  kubelet            Created container: pre-install-container
  Normal  Started    2m53s  kubelet            Started container pre-install-container
```

## Postinstall Description

```bash
tjann@fedora:~/DevOps-Course/k8s/moscow-app$ kubectl describe po postinstall-hook 
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Fri, 25 Apr 2025 04:43:05 -0400
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.28
IPs:
  IP:  10.244.0.28
Containers:
  post-install-container:
    Container ID:  docker://6bb1abd40bafb28b7fd53969736174ba745b412ab85d0fbf10bb4dc4549af13a
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:37f7b378a29ceb4c551b1b5582e27747b855bbfaa73fa11914fe0df028dc581f
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The post-install hook is running && sleep 15
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Fri, 25 Apr 2025 04:43:08 -0400
      Finished:     Fri, 25 Apr 2025 04:43:23 -0400
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-x4d28 (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-x4d28:
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
  Normal  Scheduled  3m15s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    3m15s  kubelet            Pulling image "busybox"
  Normal  Pulled     3m13s  kubelet            Successfully pulled image "busybox" in 2.04s (2.04s including waiting). Image size: 4277910 bytes.
  Normal  Created    3m13s  kubelet            Created container: post-install-container
  Normal  Started    3m13s  kubelet            Started container post-install-container
```

## kubectl get pods,svc

```bash
tjann@fedora:~/DevOps-Course/k8s/moscow-app$ kubectl get pods,svc
NAME                   READY   STATUS      RESTARTS   AGE
pod/postinstall-hook   0/1     Completed   0          6m16s
pod/preinstall-hook    0/1     Completed   0          6m38s

NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   23h
```

