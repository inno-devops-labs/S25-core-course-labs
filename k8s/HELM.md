# Helm Setup and Chart Creation

```bash
kubectl get pods,svc
```

*Output of the command:*

```bash
NAME                                         READY   STATUS    RESTARTS   AGE
pod/helm-release-python-app-8c568b7f-pt4vf   1/1     Running   0          16s

NAME                              TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/helm-release-python-app   ClusterIP   10.101.30.243   <none>        8000/TCP   16s
service/kubernetes                ClusterIP   10.96.0.1       <none>        443/TCP    4d3h
```

# Helm Chart Hooks

```bash
kubectl get po
```

*Output of the command:*

```bash
NAME                                     READY   STATUS      RESTARTS   AGE
helm-hooks-python-app-6b5fb9fb86-88s75   1/1     Running     0          116s
helm-release-python-app-8c568b7f-pt4vf   1/1     Running     0          16m
app-python-post-install-zbddx            0/1     Completed   0          16m
app-python-pre-install-zvhg6             0/1     Completed   0          16m
```

```bash
kubectl describe po app-python-pre-install-zvhg6
```

*Output of the command:*

```bash
Name:             app-python-pre-install-zvhg6
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 26 Feb 2025 20:34:17 +0300
Labels:           batch.kubernetes.io/controller-uid=6e01c750-2f2b-4de0-bce4-1788360c7c29
                  batch.kubernetes.io/job-name=app-python-pre-install
                  controller-uid=6e01c750-2f2b-4de0-bce4-1788360c7c29
                  job-name=app-python-pre-install
Annotations:      <none>
Status:           Succeeded
IP:               10.244.0.63
IPs:
  IP:           10.244.0.63
Controlled By:  Job/app-python-pre-install
Containers:
  pre-install-job:
    Container ID:  docker://e102655ae105e766af86a772f87d2c4818694aaac1b346fccd13f08e856862be
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
      /bin/sh
      -c
      echo Pre-install job running
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 26 Feb 2025 20:34:19 +0300
      Finished:     Wed, 26 Feb 2025 20:34:19 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-r7ms2 (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-r7ms2:
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
  Normal  Scheduled  17m   default-scheduler  Successfully assigned default/app-python-pre-install-zvhg6 to minikube
  Normal  Pulling    17m   kubelet            Pulling image "busybox"
  Normal  Pulled     17m   kubelet            Successfully pulled image "busybox" in 1.661s (1.661s including waiting). Image size: 4269694 bytes.
  Normal  Created    17m   kubelet            Created container: pre-install-job
  Normal  Started    17m   kubelet            Started container pre-install-job
```

```bash
kubectl describe po app-python-post-install-zbddx
```

*Output of the command:*

```bash
Name:             app-python-post-install-zbddx
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 26 Feb 2025 20:34:22 +0300
Labels:           batch.kubernetes.io/controller-uid=36814b9e-e7a2-46a5-a967-fc12d27a1e1f
                  batch.kubernetes.io/job-name=app-python-post-install
                  controller-uid=36814b9e-e7a2-46a5-a967-fc12d27a1e1f
                  job-name=app-python-post-install
Annotations:      <none>
Status:           Succeeded
IP:               10.244.0.67
IPs:
  IP:           10.244.0.67
Controlled By:  Job/app-python-post-install
Containers:
  post-install-job:
    Container ID:  docker://ffa289c85adab440cdf39f33e1a71c00e242e72a374818bcb118590843d2291d
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
      /bin/sh
      -c
      echo Post-install job completed
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 26 Feb 2025 20:34:24 +0300
      Finished:     Wed, 26 Feb 2025 20:34:24 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-ndlqb (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-ndlqb:
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
  Normal  Scheduled  16m   default-scheduler  Successfully assigned default/app-python-post-install-zbddx to minikube
  Normal  Pulling    16m   kubelet            Pulling image "busybox"
  Normal  Pulled     16m   kubelet            Successfully pulled image "busybox" in 1.595s (1.595s including waiting). Image size: 4269694 bytes.
  Normal  Created    16m   kubelet            Created container: post-install-job
  Normal  Started    16m   kubelet            Started container post-install-job
```
