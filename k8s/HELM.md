# HELM

Python app chart:

```bash
$ helm install chart-app-python chart-app-python/
NAME: chart-app-python
LAST DEPLOYED: Tue Feb 25 18:51:18 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=chart-app-python,app.kubernetes.io/instance=chart-app-python" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
```

And go app:

```bash
$ helm install chart-app-go chart-app-go/
NAME: chart-app-go
LAST DEPLOYED: Tue Feb 25 19:02:10 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=chart-app-go,app.kubernetes.io/instance=chart-app-go" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
```

```bash
$ kubectl get pods,svc

NAME                                   READY   STATUS    RESTARTS   AGE
pod/app-go-549b987b68-88wwm            1/1     Running   0          18h
pod/app-go-549b987b68-lqzbf            1/1     Running   0          18h
pod/app-go-549b987b68-sbxtb            1/1     Running   0          18h
pod/app-python-68774cd7dd-6hpl6        1/1     Running   0          18h
pod/app-python-68774cd7dd-mcjrv        1/1     Running   0          18h
pod/app-python-68774cd7dd-rnjll        1/1     Running   0          18h
pod/chart-app-go-7bc874d74-jbh8g       1/1     Running   0          3m16s
pod/chart-app-python-95cd64998-tb8cd   1/1     Running   0          14m
pod/chart-app-python-95cd64998-tzg48   1/1     Running   0          14m

NAME                       TYPE           CLUSTER-IP       EXTERNAL-IP      PORT(S)          AGE
service/app-go             LoadBalancer   10.107.156.246   10.107.156.246   8080:32573/TCP   18h
service/app-python         LoadBalancer   10.99.102.22     10.99.102.22     8080:31745/TCP   18h
service/chart-app-go       ClusterIP      10.109.106.9     <none>           8080/TCP         3m16s
service/chart-app-python   ClusterIP      10.101.249.248   <none>           8080/TCP         14m
service/kubernetes         ClusterIP      10.96.0.1        <none>           443/TCP          18h

```

## Helm hooks

```bash
$ kubectl get po
NAME                                               READY   STATUS      RESTARTS   AGE
hooks-nodelete-chart-app-python-5fcf4db878-6kgz7   1/1     Running     0          36s
hooks-nodelete-chart-app-python-5fcf4db878-frsv7   1/1     Running     0          36s
postinstall-hook                                   0/1     Completed   0          36s
preinstall-hook                                    0/1     Completed   0          58s
```

```bash
$ kubectl describe po preinstall-hook
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 26 Feb 2025 01:59:57 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.82
IPs:
  IP:  10.244.0.82
Containers:
  pre-install-container:
    Container ID:  docker://4d8a53c54b9920a2a5680c0c0b3de28932ce2021ea6c9800da2bf6a837191310
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
      Started:      Wed, 26 Feb 2025 01:59:58 +0300
      Finished:     Wed, 26 Feb 2025 02:00:18 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-2422r (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False
  Initialized                 True
  Ready                       False
  ContainersReady             False
  PodScheduled                True
Volumes:
  kube-api-access-2422r:
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
  Normal  Scheduled  3m1s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     3m    kubelet            Container image "busybox" already present on machine
  Normal  Created    3m    kubelet            Created container: pre-install-container
  Normal  Started    3m    kubelet            Started container pre-install-container
```

```bash
$ kubectl describe po postinstall-hook
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 26 Feb 2025 02:00:19 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.85
IPs:
  IP:  10.244.0.85
Containers:
  post-install-container:
    Container ID:  docker://e4e575d72ee1d197f1087badf234a26dc81485e34b9b1aed6a41c4e7da0d8fa0
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
      Started:      Wed, 26 Feb 2025 02:00:24 +0300
      Finished:     Wed, 26 Feb 2025 02:00:39 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-gnmxb (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False
  Initialized                 True
  Ready                       False
  ContainersReady             False
  PodScheduled                True
Volumes:
  kube-api-access-gnmxb:
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
  Normal  Scheduled  3m13s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    3m13s  kubelet            Pulling image "busybox"
  Normal  Pulled     3m9s   kubelet            Successfully pulled image "busybox" in 3.934s (3.934s including waiting). Image size: 4269694 bytes.
  Normal  Created    3m9s   kubelet            Created container: post-install-container
  Normal  Started    3m9s   kubelet            Started container post-install-container
```

Also, delete policy was implemented.

## Bonus, library chart with labels

```bash
$ helm dependency update chart-app-python/
Saving 1 charts
Deleting outdated charts
```

```bash
$ helm dependency update chart-app-go/
Saving 1 charts
Deleting outdated charts
```

```bash
$ helm install app-python-with-lablib chart-app-python/
NAME: app-python-with-lablib
LAST DEPLOYED: Thu Feb 27 00:16:58 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=chart-app-python,app.kubernetes.io/instance=app-python-with-lablib" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
```

```bash
$ helm install app-go-with-lablib chart-app-go/
NAME: app-go-with-lablib
LAST DEPLOYED: Thu Feb 27 00:23:04 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=chart-app-go,app.kubernetes.io/instance=app-go-with-lablib" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
```

So they all do work:

```bash
$ kubectl get pods,svc
NAME                                                           READY   STATUS    RESTARTS   AGE
pod/app-go-with-lablib-chart-app-go-6b466c95b8-hrrvc           1/1     Running   0          2m57s
pod/app-python-with-lablib-chart-app-python-5d7dd66f96-l7h72   1/1     Running   0          9m3s
pod/app-python-with-lablib-chart-app-python-5d7dd66f96-qtk5d   1/1     Running   0          9m3s

NAME                                              TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/app-go-with-lablib-chart-app-go           ClusterIP   10.101.154.73   <none>        8080/TCP   2m57s
service/app-python-with-lablib-chart-app-python   ClusterIP   10.109.14.80    <none>        8080/TCP   9m3s
service/kubernetes                                ClusterIP   10.96.0.1       <none>        443/TCP    9m40s

```
