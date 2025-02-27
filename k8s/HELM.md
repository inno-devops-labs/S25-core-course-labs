## Helm report

---

#### Minicube dashboard

![image](https://github.com/UTKANOS-RIBA/S25-core-course-labs/blob/Lab10/k8s/im1.jpg)
![image](https://github.com/UTKANOS-RIBA/S25-core-course-labs/blob/Lab10/k8s/im2.jpg)

---

#### *kubectl get pods, svc* output result
![image](https://github.com/UTKANOS-RIBA/S25-core-course-labs/blob/Lab10/k8s/im3.jpg)

---

#### *kubectl get po* output result
![image](https://github.com/UTKANOS-RIBA/S25-core-course-labs/blob/Lab10/k8s/im5.jpg)

---

#### *kubectl describe po <>* pre/post-install-jobs result

```utkanos@utkanos-VirtualBox:~/S25-core-course-labs/k8s$ kubectl get po
NAME                               READY   STATUS      RESTARTS   AGE
moscow-time-app-86cc47498b-llqzs   1/1     Running     0          31s
moscow-time-app-86cc47498b-nlndb   1/1     Running     0          31s
moscow-time-app-86cc47498b-tqdgr   1/1     Running     0          31s
post-install-hook-cvdp8            0/1     Completed   0          31s
pre-install-hook-n6m4x             0/1     Completed   0          57s
utkanos@utkanos-VirtualBox:~/S25-core-course-labs/k8s$ kubectl describe po pre-install-hook-n6m4x
Name:             pre-install-hook-n6m4x
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Thu, 27 Feb 2025 05:03:49 +0300
Labels:           batch.kubernetes.io/controller-uid=92858143-54ef-45b2-a8f4-4a861836f09d
                  batch.kubernetes.io/job-name=pre-install-hook
                  controller-uid=92858143-54ef-45b2-a8f4-4a861836f09d
                  job-name=pre-install-hook
Annotations:      <none>
Status:           Succeeded
IP:               10.244.0.35
IPs:
  IP:           10.244.0.35
Controlled By:  Job/pre-install-hook
Containers:
  sleep:
    Container ID:  docker://c7f7c240454e28bbeef635429ae55f1403e473118e4ac06d9b097aaa638c9de2
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
      sleep
      20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Thu, 27 Feb 2025 05:03:52 +0300
      Finished:     Thu, 27 Feb 2025 05:04:12 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-52l5p (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-52l5p:
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
  Normal  Scheduled  2m19s  default-scheduler  Successfully assigned default/pre-install-hook-n6m4x to minikube
  Normal  Pulling    2m19s  kubelet            Pulling image "busybox"
  Normal  Pulled     2m16s  kubelet            Successfully pulled image "busybox" in 2.192s (2.192s including waiting). Image size: 4269694 bytes.
  Normal  Created    2m16s  kubelet            Created container: sleep
  Normal  Started    2m16s  kubelet            Started container sleep
utkanos@utkanos-VirtualBox:~/S25-core-course-labs/k8s$ kubectl describe po post-install-hook-cvdp8
Name:             post-install-hook-cvdp8
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Thu, 27 Feb 2025 05:04:15 +0300
Labels:           batch.kubernetes.io/controller-uid=a1187533-0057-44ce-9e01-f8f499608680
                  batch.kubernetes.io/job-name=post-install-hook
                  controller-uid=a1187533-0057-44ce-9e01-f8f499608680
                  job-name=post-install-hook
Annotations:      <none>
Status:           Succeeded
IP:               10.244.0.39
IPs:
  IP:           10.244.0.39
Controlled By:  Job/post-install-hook
Containers:
  sleep:
Container ID:  docker://99c3b1be454aff01c16588818289bc721ca619bf93d7f949736b6d70e5448d6b
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
      sleep
      20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Thu, 27 Feb 2025 05:04:18 +0300
      Finished:     Thu, 27 Feb 2025 05:04:38 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-5h5kw (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-5h5kw:
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
  Normal  Scheduled  2m16s  default-scheduler  Successfully assigned default/post-install-hook-cvdp8 to minikube
  Normal  Pulling    2m15s  kubelet            Pulling image "busybox"
  Normal  Pulled     2m13s  kubelet            Successfully pulled image "busybox" in 2.003s (2.003s including waiting). Image size: 4269694 bytes.
  Normal  Created    2m13s  kubelet            Created container: sleep
  Normal  Started    2m13s  kubelet            Started container sleep```
