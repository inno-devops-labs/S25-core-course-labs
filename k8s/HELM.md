# Helm Deployment Documentation

## Hook Execution Details

```bash
> kubectl describe pod time-moscow-pre-install-hook
Name:             time-moscow-pre-install-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             colima/192.168.5.1
Start Time:       Wed, 26 Feb 2025 20:09:14 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
                  helm.sh/hook-delete-policy: before-hook-creation
                  helm.sh/hook-weight: -5
Status:           Succeeded
IP:               10.42.0.29
IPs:
  IP:  10.42.0.29
Containers:
  pre-install-job:
    Container ID:  docker://f63cc1cb1b8211f8590dd436537c2aa30ce7b39d8831e7a5bba298440f7f9e12
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo Pre-install hook is running && sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 26 Feb 2025 20:09:16 +0300
      Finished:     Wed, 26 Feb 2025 20:09:36 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-7zxrb (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-7zxrb:
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
  Normal  Scheduled  28s   default-scheduler  Successfully assigned default/time-moscow-pre-install-hook to colima
  Normal  Pulling    29s   kubelet            Pulling image "busybox"
  Normal  Pulled     27s   kubelet            Successfully pulled image "busybox" in 1.981s (1.982s including waiting). Image size: 4042190 bytes.
  Normal  Created    27s   kubelet            Created container pre-install-job
  Normal  Started    27s   kubelet            Started container pre-install-job
> kubectl get pods | grep hook                     
time-moscow-hooks-test-pre-install-hook               0/1     Completed   0             7m46s
time-moscow-post-install-hook                         1/1     Running     0             23s
time-moscow-pre-install-hook                          0/1     Completed   0             47s
> kubectl describe pod time-moscow-post-install-hook
Name:             time-moscow-post-install-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             colima/192.168.5.1
Start Time:       Wed, 26 Feb 2025 20:09:38 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
                  helm.sh/hook-delete-policy: before-hook-creation
                  helm.sh/hook-weight: 5
Status:           Succeeded
IP:               10.42.0.30
IPs:
  IP:  10.42.0.30
Containers:
  post-install-job:
    Container ID:  docker://0517f766351f35be77546afacb50645773f331f31dbc7cf19a378e56f9abd626
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo Post-install hook is running && sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 26 Feb 2025 20:09:40 +0300
      Finished:     Wed, 26 Feb 2025 20:10:00 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-bxq87 (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-bxq87:
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
  Normal  Scheduled  30s   default-scheduler  Successfully assigned default/time-moscow-post-install-hook to colima
  Normal  Pulling    30s   kubelet            Pulling image "busybox"
  Normal  Pulled     29s   kubelet            Successfully pulled image "busybox" in 1.898s (1.898s including waiting). Image size: 4042190 bytes.
  Normal  Created    29s   kubelet            Created container post-install-job
  Normal  Started    29s   kubelet            Started container post-install-job
```

kubectl status:

```bash
>> kubectl get pods,svc
NAME                                                      READY   STATUS    RESTARTS      AGE
pod/propositional-logic-app-deployment-64cfffc74b-5x6dd   1/1     Running   1 (63m ago)   79m
pod/propositional-logic-app-deployment-64cfffc74b-twvz2   1/1     Running   1 (63m ago)   79m
pod/propositional-logic-app-deployment-64cfffc74b-zkmpc   1/1     Running   1 (63m ago)   79m
pod/time-moscow-6d5fbc5f79-726pr                          1/1     Running   0             2m4s
pod/time-moscow-6d5fbc5f79-8whq5                          1/1     Running   0             2m4s
pod/time-moscow-6d5fbc5f79-j8zv6                          1/1     Running   0             2m4s
pod/time-moscow-post-install-hook                         0/1     Completed   0           76s
pod/time-moscow-pre-install-hook                          0/1     Completed   0           100s

NAME                                      TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes                        ClusterIP      10.43.0.1       <none>        443/TCP          118m
service/propositional-logic-app-service   LoadBalancer   10.43.195.163   <pending>     8000:32447/TCP   79m
service/time-moscow                       ClusterIP      10.43.126.72    <none>        8000/TCP         2m4s
service/time-moscow-hooks                 ClusterIP      10.43.49.76     <none>        8000/TCP         6m48s
```
