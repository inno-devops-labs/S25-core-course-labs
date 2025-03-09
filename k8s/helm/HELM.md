# Task 1

```
emildavlityarov@emapfff k8s % minikube service app-python
W1108 00:34:35.943831 24264 main.go:291] Unable to resolve the current Docker CLI context "default": context "default": context not found: open C:\Users\MSI-PC\.docker\contexts\meta\37a8eec1ce19687d132fe29051dca629d164e2c4958ba141d5f4133a33f0688f\meta.json: The system cannot find the path specified.
|-----------|------------|-------------|---------------------------|
| NAMESPACE | NAME | TARGET PORT | URL |
|-----------|------------|-------------|---------------------------|
| default | app-python | http/5000 | http://192.168.49.2:30358 |
|-----------|------------|-------------|---------------------------|

- Starting tunnel for service app-python.
  |-----------|------------|-------------|------------------------|
  | NAMESPACE | NAME | TARGET PORT | URL |
  |-----------|------------|-------------|------------------------|
  | default | app-python | | http://127.0.0.1:64527 |
  |-----------|------------|-------------|------------------------|
- Opening service default/app-python in default browser...
  ! Because you are using a Docker driver on windows, the terminal needs to be open to run it.
```

```
emildavlityarov@emapfff k8s % kubectl get pods,svc
NAME                             READY   STATUS    RESTARTS   AGE
pod/app-python-9d57c4d94-4cpwj   1/1     Running   0          5m37s
pod/app-python-9d57c4d94-68db5   1/1     Running   0          5m37s

NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python   NodePort    10.104.65.184   <none>        5000:30358/TCP   5m37s
service/kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP          117m
```

# Task 2

```
emildavlityarov@emapfff k8s % kubectl describe po postinstall-python-hook
Name:             postinstall-python-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 08 Nov 2023 01:04:08 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.8
IPs:
  IP:  10.244.0.8
Containers:
  post-install-container:
    Container ID:  docker://5b4655e6a58277968e2d1ead62478355d7047ba548e5f0f469e6cea3d678d1a2
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:3fbc632167424a6d997e74f52b878d7cc478225cffac6bc977eedfe51c7f4e79
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The post-install hook is running && sleep 1
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 08 Nov 2023 01:04:09 +0300
      Finished:     Wed, 08 Nov 2023 01:04:10 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-nhc26 (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-nhc26:
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
  Normal  Scheduled  50s   default-scheduler  Successfully assigned default/postinstall-python-hook to minikube
  Normal  Pulled     49s   kubelet            Container image "busybox" already present on machine
  Normal  Created    49s   kubelet            Created container post-install-container
  Normal  Started    49s   kubelet            Started container post-install-container
```

```
emildavlityarov@emapfff k8s % kubectl describe po preinstall-python-hook
Name:             preinstall-python-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 08 Nov 2023 01:04:04 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.6
IPs:
  IP:  10.244.0.6
Containers:
  pre-install-container:
    Container ID:  docker://91c69e4a9f2a4a5a508110f951a52d0e749a009695d6cf01d0c4bf03ca33be9d
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:3fbc632167424a6d997e74f52b878d7cc478225cffac6bc977eedfe51c7f4e79
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The pre-install hook is running && sleep 1
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 08 Nov 2023 01:04:05 +0300
      Finished:     Wed, 08 Nov 2023 01:04:06 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-dlffb (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-dlffb:
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
  Normal  Scheduled  83s   default-scheduler  Successfully assigned default/preinstall-python-hook to minikube
  Normal  Pulled     82s   kubelet            Container image "busybox" already present on machine
  Normal  Created    82s   kubelet            Created container pre-install-container
  Normal  Started    82s   kubelet            Started container pre-install-container
```

```
emildavlityarov@emapfff k8s % kubectl get pods,svc
NAME                             READY   STATUS      RESTARTS   AGE
pod/app-python-9d57c4d94-ct7zf   1/1     Running     0          3m48s
pod/postinstall-python-hook      0/1     Completed   0          3m48s
pod/preinstall-python-hook       0/1     Completed   0          3m52s

NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)          AGE
service/app-python   NodePort    10.98.74.0   <none>        5000:30597/TCP   3m48s
service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP          6m15s
```

# Bonus task

```
emildavlityarov@emapfff k8s %  kubectl describe po app-kotlin
Name:             app-kotlin-55c9755fff-5vqz5
Namespace:        default
Priority:         0
Service Account:  app-kotlin
Node:             minikube/192.168.49.2
Start Time:       Wed, 08 Nov 2023 02:01:54 +0300
Labels:           TEST=check-custom-label
                  app.kubernetes.io/instance=app-kotlin
                  app.kubernetes.io/managed-by=Helm
                  app.kubernetes.io/name=app-kotlin
                  app.kubernetes.io/version=1.16.0
                  helm.sh/chart=app-kotlin-0.1.0
                  pod-template-hash=55c9755fff
Annotations:      <none>
Status:           Running
IP:               10.244.0.13
IPs:
  IP:           10.244.0.13
Controlled By:  ReplicaSet/app-kotlin-55c9755fff
Containers:
  app-kotlin:
    Container ID:   docker://69e6780e2351288bc4b076407333c6f95bf6e19ae8a0b17d07feab86631dca8b
    Image:          emapfff/app_kotlin:latest
    Image ID:       docker-pullable://emapfff/app_kotlin@sha256:8818fe4076611494d2685f71a347f60bbb164ff1942e19f5a4a1a4c441ea3cdc
    Port:           8080/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Wed, 08 Nov 2023 02:01:55 +0300
    Ready:          True
    Restart Count:  0
    Liveness:       http-get http://:8080/ delay=0s timeout=1s period=10s #success=1 #failure=3
    Readiness:      http-get http://:8080/ delay=0s timeout=1s period=10s #success=1 #failure=3
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-zngkl (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             True
  ContainersReady   True
  PodScheduled      True
Volumes:
  kube-api-access-zngkl:
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
  Type     Reason     Age   From               Message
  ----     ------     ----  ----               -------
  Normal   Scheduled  4s    default-scheduler  Successfully assigned default/app-kotlin-55c9755fff-5vqz5 to minikube
  Normal   Pulled     3s    kubelet            Container image "emapfff/app_kotlin:latest" already present on machine
  Normal   Created    3s    kubelet            Created container app-kotlin
  Normal   Started    3s    kubelet            Started container app-kotlin
  Warning  Unhealthy  2s    kubelet            Readiness probe failed: Get "http://10.244.0.13:8080/": dial tcp 10.244.0.13:8080: connect: connection refused

```
