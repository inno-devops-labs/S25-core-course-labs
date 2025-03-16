# Helm

```bash
> kubectl get pods,svc
NAME                             READY   STATUS    RESTARTS   AGE
pod/app-python-b64ff6cdf-pn2ks   1/1     Running   0          57m

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python   LoadBalancer   10.109.151.45   <pending>     8080:31592/TCP   57m
service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          6d18h
```

## Helm Chart hooks

```bash
> kubectl get po
NAME                                     READY   STATUS      RESTARTS   AGE
helm-hooks-app-python-7b856f4666-bhxzn   1/1     Running     0          41s
postinstall-hook                         0/1     Completed   0          41s
preinstall-hook                          0/1     Completed   0          75s
```

```bash
> kubectl describe po postinstall-hook
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.59.100
Start Time:       Sun, 09 Mar 2025 19:02:44 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.23
IPs:
  IP:  10.244.0.23
Containers:
  post-install-container:
    Container ID:  docker://86fe8520a0333ba65e68717cc63215c60c4ae694cc41e7d459a9a55785317a15
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Command:
      sh
      -c
      echo The post-install hook is running && sleep 15
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Sun, 09 Mar 2025 19:02:50 +0300
      Finished:     Sun, 09 Mar 2025 19:03:07 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-zlblr (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False
  Initialized                 True
  Ready                       False
  ContainersReady             False
  PodScheduled                True
Volumes:
  kube-api-access-zlblr:
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
  Normal  Scheduled  69s   default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    66s   kubelet            Pulling image "busybox"
  Normal  Pulled     64s   kubelet            Successfully pulled image "busybox" in 2.017s (2.017s including waiting). Image size: 4269694 bytes.
  Normal  Created    64s   kubelet            Created container: post-install-container
  Normal  Started    63s   kubelet            Started container post-install-container
```

```bash
> kubectl describe po preinstall-hook
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.59.100
Start Time:       Sun, 09 Mar 2025 19:02:10 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.22
IPs:
  IP:  10.244.0.22
Containers:
  pre-install-container:
    Container ID:  docker://1353b25ccaa7e340acf5c89ec46c298a5faad7cb5fe69ff6d1401c98abe802cd
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The pre-install hook is running && sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Sun, 09 Mar 2025 19:02:20 +0300
      Finished:     Sun, 09 Mar 2025 19:02:41 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-7lcpz (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False
  Initialized                 True
  Ready                       False
  ContainersReady             False
  PodScheduled                True
Volumes:
  kube-api-access-7lcpz:
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
  Normal  Scheduled  110s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulling    109s  kubelet            Pulling image "busybox"
  Normal  Pulled     102s  kubelet            Successfully pulled image "busybox" in 6.604s (6.604s including waiting). Image size: 4269694 bytes.
  Normal  Created    101s  kubelet            Created container: pre-install-container
  Normal  Started    100s  kubelet            Started container pre-install-container
```
