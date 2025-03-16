# Task 1

```bash
❯ kubectl get pods,svc
NAME                            READY   STATUS    RESTARTS   AGE
pod/your-app-69df88b497-8dl46   1/1     Running   0          2m46s

NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP   75m
service/your-app     ClusterIP   10.109.119.47   <none>        80/TCP    10m
```

![](./dashboard.jpg)


# Task 2

```bash
❯ kubectl get po
NAME                        READY   STATUS      RESTARTS   AGE
post-install-hook-hqvmc     0/1     Completed   0          2m35s
pre-install-hook-b9mlf      0/1     Completed   0          2m46s
your-app-69df88b497-jmk6l   1/1     Running     0          2m35s

❯ kubectl describe po pre-install-hook

Name:             pre-install-hook-b9mlf
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 26 Feb 2025 17:34:21 +0300
Labels:           batch.kubernetes.io/controller-uid=2347d39b-90c1-46cc-8140-35870266271d
                  batch.kubernetes.io/job-name=pre-install-hook
                  controller-uid=2347d39b-90c1-46cc-8140-35870266271d
                  job-name=pre-install-hook
Annotations:      <none>
Status:           Succeeded
IP:               10.244.0.30
IPs:
  IP:           10.244.0.30
Controlled By:  Job/pre-install-hook
Containers:
  pre-install-container:
    Container ID:  docker://29162a6189ce3cf2a54a3d8281333980972da5725d63c350d918c7144440569d
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo 'Pre-install hook running...'; sleep 5
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 26 Feb 2025 17:34:25 +0300
      Finished:     Wed, 26 Feb 2025 17:34:30 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-xvnrb (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False
  Initialized                 True
  Ready                       False
  ContainersReady             False
  PodScheduled                True
Volumes:
  kube-api-access-xvnrb:
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
  Normal  Scheduled  105s  default-scheduler  Successfully assigned default/pre-install-hook-b9mlf to minikube
  Normal  Pulling    105s  kubelet            Pulling image "busybox"
  Normal  Pulled     101s  kubelet            Successfully pulled image "busybox" in 3.152s (3.152s including waiting). Image size: 4269678 bytes.
  Normal  Created    101s  kubelet            Created container: pre-install-container
  Normal  Started    101s  kubelet            Started container pre-install-container

❯ kubectl describe po post-install-hook

Name:             post-install-hook-hqvmc
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 26 Feb 2025 17:34:32 +0300
Labels:           batch.kubernetes.io/controller-uid=62303194-abf3-4f04-bfe4-37c8d3cdebc2
                  batch.kubernetes.io/job-name=post-install-hook
                  controller-uid=62303194-abf3-4f04-bfe4-37c8d3cdebc2
                  job-name=post-install-hook
Annotations:      <none>
Status:           Succeeded
IP:               10.244.0.32
IPs:
  IP:           10.244.0.32
Controlled By:  Job/post-install-hook
Containers:
  post-install-container:
    Container ID:  docker://89d298a1ae45b5d01437d7c55c4247aaf8296eb73bb8c81b3f620e22513e6700
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
      Started:      Wed, 26 Feb 2025 17:34:36 +0300
      Finished:     Wed, 26 Feb 2025 17:34:57 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-74phf (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False
  Initialized                 True
  Ready                       False
  ContainersReady             False
  PodScheduled                True
Volumes:
  kube-api-access-74phf:
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
  Normal  Scheduled  108s  default-scheduler  Successfully assigned default/post-install-hook-hqvmc to minikube
  Normal  Pulling    109s  kubelet            Pulling image "busybox"
  Normal  Pulled     105s  kubelet            Successfully pulled image "busybox" in 3.847s (3.847s including waiting). Image size: 4269678 bytes.
  Normal  Created    105s  kubelet            Created container: post-install-container
  Normal  Started    104s  kubelet            Started container post-install-container
  ```

After adding hook remove policy:
```bash
❯ kubectl get pods,svc
NAME                            READY   STATUS    RESTARTS   AGE
pod/your-app-69df88b497-cfqjw   1/1     Running   0          48s

NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP   102m
service/your-app     ClusterIP   10.105.68.215   <none>        80/TCP    48s
```
