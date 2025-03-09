# Helm Setup and Chart Creation

## Applying Helm
```bash
➜ k8s git:(lab-10) ✗ helm install app-python-release app-python 

NAME: app-python-release
LAST DEPLOYED: Tue Feb 25 10:26:09 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export NODE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services app-python-release)
  export NODE_IP=$(kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
  echo http://$NODE_IP:$NODE_PORT
```

## Accessing service

```bash
➜ k8s git:(lab-10) ✗ minikube service app-python-release
|-----------|--------------------|-------------|---------------------------|
| NAMESPACE |        NAME        | TARGET PORT |            URL            |
|-----------|--------------------|-------------|---------------------------|
| default   | app-python-release | http/8000   | http://192.168.49.2:32537 |
|-----------|--------------------|-------------|---------------------------|
🏃  Starting tunnel for service app-python-release.
|-----------|--------------------|-------------|------------------------|
| NAMESPACE |        NAME        | TARGET PORT |          URL           |
|-----------|--------------------|-------------|------------------------|
| default   | app-python-release |             | http://127.0.0.1:62044 |
|-----------|--------------------|-------------|------------------------|
🎉  Opening service default/app-python-release in default browser...
❗  Because you are using a Docker driver on darwin, the terminal needs to be open to run it.

```

```bash
➜ k8s git:(lab-10) ✗ kubectl get pods,svc
NAME                                      READY   STATUS    RESTARTS   AGE
pod/app-python-release-7865995874-br4kl   1/1     Running   0          3m28s

NAME                         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python-release   NodePort    10.105.15.120   <none>        8000:32537/TCP   3m29s
service/kubernetes           ClusterIP   10.96.0.1       <none>        443/TCP          13h
```

## Helm Chart Hooks

### Linting

```bash
➜ k8s git:(lab-10) ✗ helm lint app-python

==> Linting app-python
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed
```

### Installing

```bash
➜ k8s git:(lab-10) ✗ helm install helm-hooks app-python

NAME: helm-hooks
LAST DEPLOYED: Tue Feb 25 21:35:58 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export NODE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services helm-hooks-app-python)
  export NODE_IP=$(kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
  echo http://$NODE_IP:$NODE_PORT
```

### Get info

```bash
➜ k8s git:(lab-10) ✗ kubectl get po
NAME                                     READY   STATUS      RESTARTS   AGE
app-python-release-7865995874-br4kl      1/1     Running     0          11h
helm-hooks-app-python-68dcbb988c-s87vz   1/1     Running     0          7m54s
helm-hooks-post-install-vn52f            0/1     Completed   0          7m54s
helm-hooks-pre-install-qb7nn             0/1     Completed   0          8m19s
```

### Post install hook info

```bash
➜ k8s git:(lab-10) ✗ kubectl describe po helm-hooks-pre-install-qb7nn 
Name:             helm-hooks-pre-install-qb7nn
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 25 Feb 2025 21:35:58 +0300
Labels:           batch.kubernetes.io/controller-uid=ddf4481c-acf3-4a2c-8f0e-51c1e60284d0
                  batch.kubernetes.io/job-name=helm-hooks-pre-install
                  controller-uid=ddf4481c-acf3-4a2c-8f0e-51c1e60284d0
                  job-name=helm-hooks-pre-install
Annotations:      <none>
Status:           Succeeded
IP:               10.244.0.35
IPs:
  IP:           10.244.0.35
Controlled By:  Job/helm-hooks-pre-install
Containers:
  pre-install:
    Container ID:  docker://7889b8ef73f93db31aaec900b85ebfb0605bd4704cc9eb0e0da72b65db4d945b
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo Pre-install hook running; sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Tue, 25 Feb 2025 21:36:01 +0300
      Finished:     Tue, 25 Feb 2025 21:36:21 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-lgp9v (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-lgp9v:
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
  Normal  Scheduled  11m   default-scheduler  Successfully assigned default/helm-hooks-pre-install-qb7nn to minikube
  Normal  Pulling    11m   kubelet            Pulling image "busybox"
  Normal  Pulled     11m   kubelet            Successfully pulled image "busybox" in 1.737s (1.737s including waiting)
  Normal  Created    11m   kubelet            Created container pre-install
  Normal  Started    11m   kubelet            Started container pre-install
```

### Pre install hook info

```bash
.venv➜  k8s git:(lab-10) ✗ kubectl describe po helm-hooks-post-install-vn52f 
Name:             helm-hooks-post-install-vn52f
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 25 Feb 2025 21:36:23 +0300
Labels:           batch.kubernetes.io/controller-uid=a8324ad6-34b8-4207-abf6-a68dbdad42d2
                  batch.kubernetes.io/job-name=helm-hooks-post-install
                  controller-uid=a8324ad6-34b8-4207-abf6-a68dbdad42d2
                  job-name=helm-hooks-post-install
Annotations:      <none>
Status:           Succeeded
IP:               10.244.0.36
IPs:
  IP:           10.244.0.36
Controlled By:  Job/helm-hooks-post-install
Containers:
  post-install:
    Container ID:  docker://a11ff348c694feb53b26b3ee1ca1bd1df058d03aee9b94cd17040ab4d4fec669
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo Post-install hook running; sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Tue, 25 Feb 2025 21:36:25 +0300
      Finished:     Tue, 25 Feb 2025 21:36:45 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-2zphx (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-2zphx:
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
  Normal  Scheduled  9m16s  default-scheduler  Successfully assigned default/helm-hooks-post-install-vn52f to minikube
  Normal  Pulling    9m16s  kubelet            Pulling image "busybox"
  Normal  Pulled     9m15s  kubelet            Successfully pulled image "busybox" in 1.652s (1.652s including waiting)
  Normal  Created    9m15s  kubelet            Created container post-install
  Normal  Started    9m15s  kubelet            Started container post-install
```