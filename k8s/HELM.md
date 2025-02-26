# Helm

## Task 1: Helm Setup and Chart Creation

```sh
$ helm repo add stable https://charts.helm.sh/stable
"stable" has been added to your repositories

$ helm repo update
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "stable" chart repository
Update Complete. ⎈Happy Helming!⎈

$ helm create app-python-helm
Creating app-python-helm
```

```sh
$ helm install app-python-helm ./app-python-helm
NAME: app-python-helm
LAST DEPLOYED: Wed Feb 26 10:21:49 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=app-python-helm,app.kubernetes.io/instance=app-python-helm" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
```

### Kubernetes dashboard
![Dashboard](images/Screenshot%20from%202025-02-26%2010-33-12.png)


### Output of kubectl get pods,svc

```sh
$ kubectl get pods,svc
NAME                                   READY   STATUS    RESTARTS        AGE
pod/app-python-5467f97795-crvvz        1/1     Running   1 (9m17s ago)   11h
pod/app-python-5467f97795-qvmt8        1/1     Running   1 (9m17s ago)   11h
pod/app-python-5467f97795-r7rlx        1/1     Running   1 (9m17s ago)   11h
pod/app-python-helm-54b6555dbf-d4pbl   1/1     Running   0               54s

NAME                      TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python        LoadBalancer   10.98.201.163   <pending>     5000:30646/TCP   11h
service/app-python-helm   ClusterIP      10.100.55.250   <none>        5000/TCP         54s
service/kubernetes        ClusterIP      10.96.0.1       <none>        443/TCP          12h
```

### app-python-helm service

```sh
$ minikube service app-python-helm
|-----------|-----------------|-------------|--------------|
| NAMESPACE |      NAME       | TARGET PORT |     URL      |
|-----------|-----------------|-------------|--------------|
| default   | app-python-helm |             | No node port |
|-----------|-----------------|-------------|--------------|
😿  service default/app-python-helm has no node port
❗  Services [default/app-python-helm] have type "ClusterIP" not meant to be exposed, however for local development minikube allows you to access this !
🏃  Starting tunnel for service app-python-helm.
|-----------|-----------------|-------------|------------------------|
| NAMESPACE |      NAME       | TARGET PORT |          URL           |
|-----------|-----------------|-------------|------------------------|
| default   | app-python-helm |             | http://127.0.0.1:34339 |
|-----------|-----------------|-------------|------------------------|
🎉  Opening service default/app-python-helm in default browser...
❗  Because you are using a Docker driver on linux, the terminal needs to be open to run it.
```


## Task 2: Helm Chart Hooks

### Linting:

```sh
runner@Runner:~/projects/S25-core-course-labs/k8s$ helm lint app-python-helm
==> Linting app-python-helm
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed
```



### Task 2 outputs

#### kubectl get po
```sh
$ kubectl get po
NAME                                          READY   STATUS      RESTARTS       AGE
app-python-5467f97795-crvvz                   1/1     Running     1 (103m ago)   13h
app-python-5467f97795-qvmt8                   1/1     Running     1 (103m ago)   13h
app-python-5467f97795-r7rlx                   1/1     Running     1 (103m ago)   13h
app-python-helm-54b6555dbf-d4pbl              1/1     Running     0              95m
helm-hooks-app-python-helm-7dfd5889c9-rxcc6   1/1     Running     0              2m33s
postinstall-hook                              0/1     Completed   0              2m33s
preinstall-hook                               0/1     Completed   0              3m3s
```


#### kubectl describe po preinstall-hook
```sh
$ kubectl describe po preinstall-hook
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 26 Feb 2025 11:53:50 +0000
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.31
IPs:
  IP:  10.244.0.31
Containers:
  pre-install-container:
    Container ID:  docker://d53cbc516c36d0923ac377396a2f2a0d2694f52e592800ec72a704c240421509
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
      Started:      Wed, 26 Feb 2025 11:53:57 +0000
      Finished:     Wed, 26 Feb 2025 11:54:17 +0000
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-dnq7v (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-dnq7v:
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
  Normal  Scheduled  4m36s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulling    4m35s  kubelet            Pulling image "busybox"
  Normal  Pulled     4m29s  kubelet            Successfully pulled image "busybox" in 5.609s (5.609s including waiting). Image size: 4269694 bytes.
  Normal  Created    4m29s  kubelet            Created container: pre-install-container
  Normal  Started    4m29s  kubelet            Started container pre-install-container
runner@Runner:~/projects/S25-core-course-labs/k8s$ 
```


# Postinstall

```sh
$ kubectl describe po postinstall-hook
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 26 Feb 2025 11:54:19 +0000
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.33
IPs:
  IP:  10.244.0.33
Containers:
  post-install-container:
    Container ID:  docker://f0c4e8dadec82db7e866f4551bc85a4719f1ecec114112d32b96ec7486ddaa4a
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
      Started:      Wed, 26 Feb 2025 11:54:25 +0000
      Finished:     Wed, 26 Feb 2025 11:54:40 +0000
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-fl76c (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-fl76c:
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
  Normal  Scheduled  5m     default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    5m     kubelet            Pulling image "busybox"
  Normal  Pulled     4m55s  kubelet            Successfully pulled image "busybox" in 2.327s (4.571s including waiting). Image size: 4269694 bytes.
  Normal  Created    4m55s  kubelet            Created container: post-install-container
  Normal  Started    4m55s  kubelet            Started container post-install-container
```

### Hook Delete Policy
We need to add this string to preinstall and postinstall hooks:

```sh
"helm.sh/hook-delete-policy": "hook-succeeded"
```
