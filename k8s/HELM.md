## HELM

### Task 1

The output of `kubectl get pods,svc`:
```
kubectl get pods,svc
NAME                                          READY   STATUS    RESTARTS      AGE
pod/moscow-time-deployment-6bcbb8d58c-7nw7n   1/1     Running   1 (28m ago)   4h56m
pod/moscow-time-deployment-6bcbb8d58c-jcsp7   1/1     Running   1 (28m ago)   4h56m
pod/moscow-time-deployment-6bcbb8d58c-pqcnv   1/1     Running   1 (28m ago)   4h56m
pod/my-release-moscow-time-7d9878f785-4pxr2   1/1     Running   1 (28m ago)   30m
pod/my-release-moscow-time-7d9878f785-qccj9   1/1     Running   1 (28m ago)   30m
pod/my-release-moscow-time-7d9878f785-t4tdt   1/1     Running   1 (28m ago)   30m

NAME                             TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes               ClusterIP   10.96.0.1       <none>        443/TCP          2d19h
service/moscow-time-service      NodePort    10.103.54.240   <none>        8000:30768/TCP   2d17h
service/my-release-moscow-time   NodePort    10.102.96.96    <none>        8000:32058/TCP   30m
```

The output of `minikube service moscow-time`:
```
minikube service moscow-time-service
|-----------|---------------------|-------------|---------------------------|
| NAMESPACE |        NAME         | TARGET PORT |            URL            |
|-----------|---------------------|-------------|---------------------------|
| default   | moscow-time-service |        8000 | http://192.168.49.2:30768 |
|-----------|---------------------|-------------|---------------------------|
🎉  Opening service default/moscow-time-service in default browser...

```

The workloads page of minikube dashboards.
![dashboard](/k8s/media/minikube-dashboard.png)

### Task 2
The output of `kubectl get po` command:
```
kubectl get po

NAME                                      READY   STATUS      RESTARTS      AGE
helm-hooks-moscow-time-5bb6b97b5b-8bw6l   1/1     Running     0             57s
helm-hooks-moscow-time-5bb6b97b5b-mr9l8   1/1     Running     0             57s
helm-hooks-moscow-time-5bb6b97b5b-ztgkm   1/1     Running     0             57s
moscow-time-deployment-6bcbb8d58c-7nw7n   1/1     Running     1 (53m ago)   5h22m
moscow-time-deployment-6bcbb8d58c-jcsp7   1/1     Running     1 (53m ago)   5h22m
moscow-time-deployment-6bcbb8d58c-pqcnv   1/1     Running     1 (53m ago)   5h22m
my-release-moscow-time-7d9878f785-4pxr2   1/1     Running     1 (53m ago)   55m
my-release-moscow-time-7d9878f785-qccj9   1/1     Running     1 (53m ago)   55m
my-release-moscow-time-7d9878f785-t4tdt   1/1     Running     1 (53m ago)   55m
postinstall-hook                          0/1     Completed   0             57s
preinstall-hook                           0/1     Completed   0             80s
```

The output of `kubectl describe po preinstall-hook` command:
```
kubectl describe po preinstall-hook

Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sat, 01 Mar 2025 17:27:50 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.40
IPs:
  IP:  10.244.0.40
Containers:
  pre-install-container:
    Container ID:  docker://59ff17bed37843c5ca9728e81b7166e2c4f4f197e7f98995106da9a0d320f18e
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
      Started:      Sat, 01 Mar 2025 17:27:51 +0300
      Finished:     Sat, 01 Mar 2025 17:28:11 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-fndnr (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-fndnr:
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
  Normal  Scheduled  2m26s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     2m25s  kubelet            Container image "busybox" already present on machine
  Normal  Created    2m25s  kubelet            Created container: pre-install-container
  Normal  Started    2m25s  kubelet            Started container pre-install-container
```

The output of `kubectl describe po postinstall-hook` command:
```
 kubectl describe po postinstall-hook

Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sat, 01 Mar 2025 17:28:13 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.44
IPs:
  IP:  10.244.0.44
Containers:
  post-install-container:
    Container ID:  docker://9497d405604994a457635ae626324f779121e50ff220eed3d5e1b3a3baa40645
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The post-install hook is running && sleep 15
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Sat, 01 Mar 2025 17:28:15 +0300
      Finished:     Sat, 01 Mar 2025 17:28:30 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-rhbdz (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-rhbdz:
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
  Normal  Scheduled  3m19s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    3m19s  kubelet            Pulling image "busybox"
  Normal  Pulled     3m17s  kubelet            Successfully pulled image "busybox" in 1.454s (1.454s including waiting). Image size: 4269694 bytes.
  Normal  Created    3m17s  kubelet            Created container: post-install-container
  Normal  Started    3m17s  kubelet            Started container post-install-container
```

The output of `kubectl get pods,svc` command after delete-policy is added:
```
NAME                                          READY   STATUS    RESTARTS      AGE
pod/helm-hooks-moscow-time-5bb6b97b5b-lz4d6   1/1     Running   0             27s
pod/helm-hooks-moscow-time-5bb6b97b5b-vgkph   1/1     Running   0             27s
pod/helm-hooks-moscow-time-5bb6b97b5b-xmksx   1/1     Running   0             27s
pod/moscow-time-deployment-6bcbb8d58c-7nw7n   1/1     Running   1 (74m ago)   5h43m
pod/moscow-time-deployment-6bcbb8d58c-jcsp7   1/1     Running   1 (74m ago)   5h43m
pod/moscow-time-deployment-6bcbb8d58c-pqcnv   1/1     Running   1 (74m ago)   5h43m
pod/my-release-moscow-time-7d9878f785-4pxr2   1/1     Running   1 (74m ago)   76m
pod/my-release-moscow-time-7d9878f785-qccj9   1/1     Running   1 (74m ago)   76m
pod/my-release-moscow-time-7d9878f785-t4tdt   1/1     Running   1 (74m ago)   76m

NAME                             TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/helm-hooks-moscow-time   NodePort    10.108.161.105   <none>        8000:31910/TCP   27s
service/kubernetes               ClusterIP   10.96.0.1        <none>        443/TCP          2d20h
service/moscow-time-service      NodePort    10.103.54.240    <none>        8000:30768/TCP   2d18h
service/my-release-moscow-time   NodePort    10.102.96.96     <none>        8000:32058/TCP   76m
```