# Helm

## Helm Setup and Chart Creation

### Output of `kubectl get pods,svc`

```sh
NAME                          READY   STATUS    RESTARTS   AGE
pod/my-app-6df96d5fc4-nsnbm   1/1     Running   0          3m35s

NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP    101m
service/my-app       ClusterIP   10.107.200.20   <none>        5000/TCP   3m35s
```

## Helm Chart Hooks

### Output of `kubectl get po`

```sh
NAME                      READY   STATUS      RESTARTS   AGE
my-app-6df96d5fc4-ktxrt   1/1     Running     0          28s
post-install-jmq4c        0/1     Completed   0          28s
pre-install-wmb99         0/1     Completed   0          32s
```

### Output of `kubectl describe po post-install-jmq4c`

```sh
Name:             post-install-jmq4c
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 26 Feb 2025 23:04:00 +0300
Labels:           batch.kubernetes.io/controller-uid=327f3f24-95eb-49d8-b3fc-1d8c1c745fae
                  batch.kubernetes.io/job-name=post-install
                  controller-uid=327f3f24-95eb-49d8-b3fc-1d8c1c745fae
                  job-name=post-install
Annotations:      <none>
Status:           Succeeded
IP:               10.244.0.25
IPs:
  IP:           10.244.0.25
Controlled By:  Job/post-install
Containers:
  post-install-job:
    Container ID:  docker://a80f6936b93b4751271145657c518a8151106dade44f28c9442278728d5a99cd
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
      Started:      Wed, 26 Feb 2025 23:04:03 +0300
      Finished:     Wed, 26 Feb 2025 23:04:03 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-tbkqt (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False
  Initialized                 True
  Ready                       False
  ContainersReady             False
  PodScheduled                True
Volumes:
  kube-api-access-tbkqt:
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
  Normal  Scheduled  48s   default-scheduler  Successfully assigned default/post-install-jmq4c to minikube
  Normal  Pulling    48s   kubelet            Pulling image "busybox"
  Normal  Pulled     45s   kubelet            Successfully pulled image "busybox" in 1.553s (2.997s including waiting). Image size: 4269694 bytes.
  Normal  Created    45s   kubelet            Created container: post-install-job
  Normal  Started    45s   kubelet            Started container post-install-job
```

### Output of `kubectl describe po pre-install-wmb99`

```sh
Name:             pre-install-wmb99
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 26 Feb 2025 23:03:56 +0300
Labels:           batch.kubernetes.io/controller-uid=4e0f9235-360d-4649-9ce7-97a50741635c
                  batch.kubernetes.io/job-name=pre-install
                  controller-uid=4e0f9235-360d-4649-9ce7-97a50741635c
                  job-name=pre-install
Annotations:      <none>
Status:           Succeeded
IP:               10.244.0.23
IPs:
  IP:           10.244.0.23
Controlled By:  Job/pre-install
Containers:
  pre-install-job:
    Container ID:  docker://e23aa3317026a092d58e793ad5569119eca3be235e44872f130e214cc7c01505
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
      Started:      Wed, 26 Feb 2025 23:03:59 +0300
      Finished:     Wed, 26 Feb 2025 23:03:59 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-8g8rl (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False
  Initialized                 True
  Ready                       False
  ContainersReady             False
  PodScheduled                True
Volumes:
  kube-api-access-8g8rl:
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
  Normal  Scheduled  85s   default-scheduler  Successfully assigned default/pre-install-wmb99 to minikube
  Normal  Pulling    84s   kubelet            Pulling image "busybox"
  Normal  Pulled     82s   kubelet            Successfully pulled image "busybox" in 1.914s (1.914s including waiting). Image size: 4269694 bytes.
  Normal  Created    82s   kubelet            Created container: pre-install-job
  Normal  Started    82s   kubelet            Started container pre-install-job
```