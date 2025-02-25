# HELM

## Overview

This document will provide an overview of Helm setup and hooks

## Helm Setup

After creating the app the app and installing it

```bash
$ helm install web-app ./web-app/
NAME: web-app
LAST DEPLOYED: Tue Feb 25 16:26:40 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=web-app,app.kubernetes.io/instance=web-app" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
```

We can access the app by following running the commands provided or by running:

```bash
$ minikube service web-app
|-----------|---------|-------------|--------------|
| NAMESPACE |  NAME   | TARGET PORT |     URL      |
|-----------|---------|-------------|--------------|
| default   | web-app |             | No node port |
|-----------|---------|-------------|--------------|
😿  service default/web-app has no node port
❗  Services [default/web-app] have type "ClusterIP" not meant to be exposed, however for local development minikube allows you to access this !
🏃  Starting tunnel for service web-app.
|-----------|---------|-------------|------------------------|
| NAMESPACE |  NAME   | TARGET PORT |          URL           |
|-----------|---------|-------------|------------------------|
| default   | web-app |             | http://127.0.0.1:41607 |
|-----------|---------|-------------|------------------------|
🎉  Opening service default/web-app in default browser...
❗  Because you are using a Docker driver on linux, the terminal needs to be open to run it.
```

**Pods and Services:**

```bash
$ kubectl get pods,svc
NAME                           READY   STATUS    RESTARTS   AGE
pod/web-app-645d86898b-dttvq   1/1     Running   0          2m58s

NAME                 TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
service/kubernetes   ClusterIP   10.96.0.1        <none>        443/TCP    23h
service/web-app      ClusterIP   10.101.253.100   <none>        5000/TCP   2m58s
```

## Helm Hooks

We will create two [hooks](https://helm.sh/docs/topics/charts_hooks/#the-available-hooks):

- `pre-install` hook
- `post-install` hook

We add them to the `templates` directory.

- **Pods:**

  ```bash
  $ kubectl get po
  NAME                       READY   STATUS      RESTARTS   AGE
  postinstall-hook           0/1     Completed   0          4m22s
  preinstall-hook            0/1     Completed   0          4m43s
  web-app-645d86898b-rgwxv   1/1     Running     0          4m22s
  ```

- **pre-install Pod:**

  ```bash
  $ kubectl describe po preinstall-hook
  Name:             preinstall-hook
  Namespace:        default
  Priority:         0
  Service Account:  default
  Node:             minikube/192.168.49.2
  Start Time:       Tue, 25 Feb 2025 17:14:05 +0300
  Labels:           <none>
  Annotations:      helm.sh/hook: pre-install
  Status:           Succeeded
  IP:               10.244.0.57
  IPs:
    IP:  10.244.0.57
  Containers:
    pre-install-container:
      Container ID:  docker://796b8444423c0e1b390cb0b71d6b4834785566dfd382a160fb624aa2e3e23ce7
      Image:         busybox
      Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
      Port:          <none>
      Host Port:     <none>
      Command:
        sh
        -c
        echo The pre-install hook is running && sleep 5
      State:          Terminated
        Reason:       Completed
        Exit Code:    0
        Started:      Tue, 25 Feb 2025 17:14:10 +0300
        Finished:     Tue, 25 Feb 2025 17:14:15 +0300
      Ready:          False
      Restart Count:  0
      Environment:    <none>
      Mounts:
        /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-kvbww (ro)
  Conditions:
    Type                        Status
    PodReadyToStartContainers   False 
    Initialized                 True 
    Ready                       False 
    ContainersReady             False 
    PodScheduled                True 
  Volumes:
    kube-api-access-kvbww:
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
    Normal  Scheduled  47s   default-scheduler  Successfully assigned default/preinstall-hook to minikube
    Normal  Pulling    47s   kubelet            Pulling image "busybox"
    Normal  Pulled     42s   kubelet            Successfully pulled image "busybox" in 4.47s (4.47s including waiting). Image size: 4269694 bytes.
    Normal  Created    42s   kubelet            Created container: pre-install-container
    Normal  Started    42s   kubelet            Started container pre-install-container
  ```

- **post-install Pod:**

  ```bash
  $ kubectl describe po postinstall-hook
  Name:             postinstall-hook
  Namespace:        default
  Priority:         0
  Service Account:  default
  Node:             minikube/192.168.49.2
  Start Time:       Tue, 25 Feb 2025 17:14:17 +0300
  Labels:           <none>
  Annotations:      helm.sh/hook: post-install
  Status:           Succeeded
  IP:               10.244.0.59
  IPs:
    IP:  10.244.0.59
  Containers:
    post-install-container:
      Container ID:  docker://d1a0a14249a30397771e0a1fff04ac7f2ce62c7e5ab74b7e75db56ca6a2ffef7
      Image:         busybox
      Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
      Port:          <none>
      Host Port:     <none>
      Command:
        sh
        -c
        echo The post-install hook is running && sleep 5
      State:          Terminated
        Reason:       Completed
        Exit Code:    0
        Started:      Tue, 25 Feb 2025 17:14:21 +0300
        Finished:     Tue, 25 Feb 2025 17:14:26 +0300
      Ready:          False
      Restart Count:  0
      Environment:    <none>
      Mounts:
        /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-ktv6p (ro)
  Conditions:
    Type                        Status
    PodReadyToStartContainers   False 
    Initialized                 True 
    Ready                       False 
    ContainersReady             False 
    PodScheduled                True 
  Volumes:
    kube-api-access-ktv6p:
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
    Normal  Scheduled  2m8s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
    Normal  Pulling    2m8s  kubelet            Pulling image "busybox"
    Normal  Pulled     2m5s  kubelet            Successfully pulled image "busybox" in 3.384s (3.384s including waiting). Image size: 4269694 bytes.
    Normal  Created    2m5s  kubelet            Created container: post-install-container
    Normal  Started    2m5s  kubelet            Started container post-install-container
  ```

## Hooks delete policy

This feature can be added to the annotations part in the yaml file
Reference: [Hook deletion policies](https://helm.sh/docs/topics/charts_hooks/#hook-deletion-policies)

After adding the policy and installing the helm chart, if we check the pods we see only our app

```bash
$ kubectl get po
NAME                       READY   STATUS    RESTARTS   AGE
web-app-645d86898b-fvcrm   1/1     Running   0          58s
```
