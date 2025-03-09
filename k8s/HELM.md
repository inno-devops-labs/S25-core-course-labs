# Helm

## Task 1

```bash
$ helm install app-python app-python
NAME: app-python
LAST DEPLOYED: Thu Feb 27 11:35:03 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export NODE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services app-python)
  export NODE_IP=$(kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
  echo http://$NODE_IP:$NODE_PORT

$ minikube dashboard
🤔  Verifying dashboard health ...
🚀  Launching proxy ...
🤔  Verifying proxy health ...
🎉  Opening http://127.0.0.1:44607/api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard:/proxy/ in your default browser...
```

Here is the screenshot:

![dashboard](/k8s/media/dashboard.png)

```bash
minikube service app-python
```

| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | app-python | http/8081   | <http://192.168.49.2:32640> |

🎉  Opening service default/app-python in default browser...

---

I did an analagous procedure for the second app

```bash
minikube service app-go
```

| NAMESPACE |  NAME  | TARGET PORT |            URL            |
|-----------|--------|-------------|---------------------------|
| default   | app-go | http/8080   | <http://192.168.49.2:32450> |

🎉  Opening service default/app-go in default browser...

Here is the output of pods and services:

```bash
$ kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-go-869748ddbb-c6mnf       1/1     Running   0          7m37s
pod/app-python-5b7d65f767-9gmqh   1/1     Running   0          46m

NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-go       NodePort    10.106.212.50   <none>        8080:32450/TCP   7m38s
service/app-python   NodePort    10.96.167.29    <none>        8081:32640/TCP   46m
service/kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP          16h
```

## Task 2

Here is the output of the requested commands.

```bash

$ kubectl get po 
NAME                          READY   STATUS      RESTARTS   AGE
app-go-869748ddbb-c6mnf       1/1     Running     0          20m
app-python-5b7d65f767-5nrjf   1/1     Running     0          89s
postinstall-hook              0/1     Completed   0          89s
preinstall-hook               0/1     Completed   0          2m1s

$ kubectl describe po preinstall-hook 
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Thu, 27 Feb 2025 12:31:46 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.92
IPs:
  IP:  10.244.0.92
Containers:
  pre-install-container:
    Container ID:  docker://ff6ffeff93ac2ec7d6cf75bc7937a86b32e48e668c98d98f7f5d40c8588b3f9d
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
      Started:      Thu, 27 Feb 2025 12:31:55 +0300
      Finished:     Thu, 27 Feb 2025 12:32:15 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-gpfb5 (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-gpfb5:
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
  Normal  Scheduled  2m8s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulling    2m6s  kubelet            Pulling image "busybox"
  Normal  Pulled     2m    kubelet            Successfully pulled image "busybox" in 5.537s (5.537s including waiting). Image size: 4269678 bytes.
  Normal  Created    119s  kubelet            Created container: pre-install-container
  Normal  Started    119s  kubelet            Started container pre-install-container

$ kubectl describe po postinstall-hook 
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Thu, 27 Feb 2025 12:32:18 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.94
IPs:
  IP:  10.244.0.94
Containers:
  post-install-container:
    Container ID:  docker://6451d09d9ba3ef9796f797bbe10ed720cfbf266fd4e0f379b1dc1c3f6ed3f131
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
      Started:      Thu, 27 Feb 2025 12:32:26 +0300
      Finished:     Thu, 27 Feb 2025 12:32:41 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-x9g4d (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-x9g4d:
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
  Normal  Scheduled  108s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    106s  kubelet            Pulling image "busybox"
  Normal  Pulled     101s  kubelet            Successfully pulled image "busybox" in 2.496s (5.426s including waiting). Image size: 4269678 bytes.
  Normal  Created    100s  kubelet            Created container: post-install-container
  Normal  Started    100s  kubelet            Started container post-install-container

$ kubectl get pods,svc
NAME                              READY   STATUS      RESTARTS   AGE
pod/app-go-869748ddbb-ptwbr       1/1     Running     0          8m27s
pod/app-python-84bb6c8ff4-bxdtg   1/1     Running     0          96s
pod/postinstall-hook              0/1     Completed   0          96s
pod/preinstall-hook               0/1     Completed   0          2m3s

NAME                 TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/app-go       NodePort    10.101.137.156   <none>        8080:31152/TCP   8m27s
service/app-python   NodePort    10.99.25.151     <none>        8081:32452/TCP   97s

```

## Task bonus

First of all, I created a library chart, then I added it as a dependency to `Chart.yaml` of my apps.

```bash
$ helm dependency update app-python
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "stable" chart repository
Update Complete. ⎈Happy Helming!⎈
Saving 1 charts
Deleting outdated charts
$ helm dependency update app-go
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "stable" chart repository
Update Complete. ⎈Happy Helming!⎈
Saving 1 charts
Deleting outdated charts
```

---

Then I ran the following commands:

```bash

$ helm install app-python-library app-python
NAME: app-python-library
LAST DEPLOYED: Thu Feb 27 13:06:11 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export NODE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services app-python-library)
  export NODE_IP=$(kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
  echo http://$NODE_IP:$NODE_PORT

$ helm install app-go-library app-go
NAME: app-go-library
LAST DEPLOYED: Thu Feb 27 13:03:55 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export NODE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services app-go-library)
  export NODE_IP=$(kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
  echo http://$NODE_IP:$NODE_PORT

$ kubectl get pods, svc
error: arguments in resource/name form must have a single resource and name

$ kubectl get pods,svc
NAME                                      READY   STATUS    RESTARTS   AGE
pod/app-go-library-7fbdd6c76d-tfz5s       1/1     Running   0          35s
pod/app-python-library-6bdb9c49d8-k9hxk   1/1     Running   0          3m20s

NAME                         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/app-go-library       NodePort    10.102.107.200   <none>        8080:30502/TCP   36s
service/app-python-library   NodePort    10.101.229.254   <none>        8081:31108/TCP   3m20s
service/kubernetes           ClusterIP   10.96.0.1        <none>        443/TCP          17h

```
