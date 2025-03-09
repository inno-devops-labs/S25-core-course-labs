# Helm Setup and Chart Creation

## Installation

```bash 
curl -fsSL https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
```

- Verify Installation:

```bash
helm version
```

## Generate a Helm chart

```bash
egor@egor-100-HP:~/PycharmProjects/S25-core-course-labs/k8s$ helm install app-python ./app-python
NAME: app-python
LAST DEPLOYED: Tue Feb 26 23:30:47 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=app-python,app.kubernetes.io/instance=app-python" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:5000 to use your application"
```

```bash
egor@egor-100-HP:~/PycharmProjects/S25-core-course-labs/k8s$ kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-7fac46b478-nak8g   1/1     Running   0          1m43s

NAME                         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python           NodePort    10.106.277.547  <none>        5000/TCP         1m43s
service/kubernetes           ClusterIP   10.96.0.1       <none>        443/TCP          11h10m
```

```bash
egor@egor-100-HP:~/PycharmProjects/S25-core-course-labs/k8s$ minikube service --all
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | app-python |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/app-python has no node port
❗  Services [default/kubernetes default/app-python] have type "ClusterIP" not meant to be exposed, however for local development minikube allows you to access this !
🏃  Starting tunnel for service kubernetes.
🏃  Starting tunnel for service app-python.
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | kubernetes |             | http://127.0.0.1:44763 |
| default   | app-python |             | http://127.0.0.1:44308 |
|-----------|------------|-------------|------------------------|
🎉  Opening service default/kubernetes in default browser...
🎉  Opening service default/app-python in default browser...
❗  Because you are using a Docker driver on linux, the terminal needs to be open to run it.
```

## Helm Chart Hooks

```bash
egor@egor-100-HP:~/PycharmProjects/S25-core-course-labs/k8s$ kubectl get po
fory@pop-os:~/devops-labs/S25-core-course-labs/k8s$ kubectl get po
NAME                          READY   STATUS    RESTARTS   AGE
app-python-7fac46b478-nak8g   1/1     Running   0          7m
```

## Pre-install Hook

```bash
egor@egor-100-HP:~/PycharmProjects/S25-core-course-labs/k8s$ kubectl describe po pre-install-hook
Name:             pre-install-hook-fgs7t
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 27 Feb 2025 01:03:12 +0300
Labels:           batch.kubernetes.io/controller-uid=a54d497d-5dd2-49d6-8d72-07fc9922b397
                  batch.kubernetes.io/job-name=pre-install-hook
                  controller-uid=a54d497d-5dd2-49d6-8d72-07fc9922b397
                  job-name=pre-install-hook
Annotations:      <none>
Status:           Succeeded
IP:               10.244.0.27
IPs:
  IP:           10.244.0.27
Controlled By:  Job/pre-install-hook
Containers:
  pre-install:
    Container ID:  docker://bb9e5dc927c33b9dadc00a1cf3019c9bfc91e3aceda053f51eea4bd19d8fde0c
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo 'Pre-install hook running...'; sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 27 Feb 2025 01:03:16 +0300
      Finished:     Wed, 27 Feb 2025 01:05:06 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-z3had (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-z3had:
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
  Normal  Scheduled  110s  default-scheduler  Successfully assigned default/pre-install-hook-fgs7t to minikube
  Normal  Pulling    110s  kubelet            Pulling image "busybox"
  Normal  Pulled     106s   kubelet           Successfully pulled image "busybox" in 3.539s (3.539s including waiting). Image size: 4269694 bytes.
  Normal  Created    106s   kubelet           Created container: pre-install
  Normal  Started    106s   kubelet           Started container pre-install
```

## Post-install Hook

```bash
egor@egor-100-HP:~/PycharmProjects/S25-core-course-labs/k8s$ kubectl describe po post-install-hook
Name:             post-install-hook-ds8fs
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 27 Feb 2025 01:07:35 +0300
Labels:           batch.kubernetes.io/controller-uid=6f2b89f3-91c3-4ab4-9c6d-cf12343f891b
                  batch.kubernetes.io/job-name=install-hook
                  controller-uid=6f2b89f3-91c3-4ab4-9c6d-cf12343f891b
                  job-name=post-install-hook
Annotations:      <none>
Status:           Succeeded
IP:               10.244.0.28
IPs:
  IP:           10.244.0.28
Controlled By:  Job/post-install-hook
Containers:
  post-install:
    Container ID:  docker://f9b6e7634a12d2a1327b9a6745d3a47b1d612e7d5fd96a815b7d9e83c74e55e3
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
      Started:      Wed, 27 Feb 2025 01:07:38 +0300
      Finished:     Wed, 27 Feb 2025 01:09:54 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-5jlf3 (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-5jlf3:
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
  Normal  Scheduled  2m16s default-scheduler  Successfully assigned default/post-install-hook-ds8fs to minikube
  Normal  Pulling    2m16s kubelet            Pulling image "busybox"
  Normal  Pulled     2m14s kubelet            Successfully pulled image "busybox" in 1.56s (1.56s including waiting). Image size: 4269694 bytes.
  Normal  Created    2m14s kubelet            Created container: post-install
  Normal  Started    2m14s kubelet            Started container post-install
```

