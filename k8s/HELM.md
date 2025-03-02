NAME                                 READY   STATUS    RESTARTS   AGE
pod/flask-app-app-6b978d9cb7-m84dr   1/1     Running   0          12m

NAME                 TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
service/flask-app    NodePort    10.103.163.197   <none>        80:30766/TCP   29s
service/kubernetes   ClusterIP   10.96.0.1        <none>        443/TCP        32s

kubectl get po

NAME                            READY   STATUS      RESTARTS   AGE
helm-hooks-app-d5cc8655-f9cdq   1/1     Running     0          102s
postinstall-hook-gbh2z          0/1     Completed   0          102s
preinstall-hook-t98rm           0/1     Completed   0          2m8s

kubectl describe po <preinstall_hook_name>

Name:             preinstall-hook-t98rm
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sun, 02 Mar 2025 22:58:44 +0300
Labels:           batch.kubernetes.io/controller-uid=375ae7fb-7a54-4de3-82fe-5be0b6fbffa0
                  batch.kubernetes.io/job-name=preinstall-hook
                  controller-uid=375ae7fb-7a54-4de3-82fe-5be0b6fbffa0
                  job-name=preinstall-hook
Annotations:      <none>
Status:           Succeeded
IP:               10.244.0.23
IPs:
  IP:           10.244.0.23
Controlled By:  Job/preinstall-hook
Containers:
  preinstall-hook:
    Container ID:  docker://0781e1f26862b141054fe523225ea3bbf923172cb8b0748602a62e680ff352b2
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
      Started:      Sun, 02 Mar 2025 22:58:47 +0300
      Finished:     Sun, 02 Mar 2025 22:59:07 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-pzpbh (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-pzpbh:
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
  Normal  Scheduled  2m37s  default-scheduler  Successfully assigned default/preinstall-hook-t98rm to minikube
  Normal  Pulling    2m36s  kubelet            Pulling image "busybox"
  Normal  Pulled     2m34s  kubelet            Successfully pulled image "busybox" in 2.14s (2.14s including waiting). Image size: 4269678 bytes.
  Normal  Created    2m34s  kubelet            Created container: preinstall-hook
  Normal  Started    2m34s  kubelet            Started container preinstall-hook

kubectl describe po <postinstall_hook_name>

Name:             postinstall-hook-gbh2z
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sun, 02 Mar 2025 22:59:10 +0300
Labels:           batch.kubernetes.io/controller-uid=a42b3912-13ca-43fa-90f9-8b8741fcde33
                  batch.kubernetes.io/job-name=postinstall-hook
                  controller-uid=a42b3912-13ca-43fa-90f9-8b8741fcde33
                  job-name=postinstall-hook
Annotations:      <none>
Status:           Succeeded
IP:               10.244.0.25
IPs:
  IP:           10.244.0.25
Controlled By:  Job/postinstall-hook
Containers:
  postinstall-hook:
    Container ID:  docker://ad74fec2865c855c3ccae26bd17db17c14905e8c867abf65ff037259c92c4132
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
      Started:      Sun, 02 Mar 2025 22:59:15 +0300
      Finished:     Sun, 02 Mar 2025 22:59:35 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-gthb6 (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-gthb6:
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
  Normal  Scheduled  2m55s  default-scheduler  Successfully assigned default/postinstall-hook-gbh2z to minikube
  Normal  Pulling    2m54s  kubelet            Pulling image "busybox"
  Normal  Pulled     2m50s  kubelet            Successfully pulled image "busybox" in 1.548s (3.734s including waiting). Image size: 4269678 bytes.
  Normal  Created    2m50s  kubelet            Created container: postinstall-hook
  Normal  Started    2m50s  kubelet            Started container postinstall-hook

