# Helm Overview

## Running helm

How it is set up:

```text
PS C:\Users\egora\PycharmProjects\S25-core-course-labs\k8s> helm install flask-release ./flask-app
LAST DEPLOYED: Mon Feb 24 21:02:04 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=flask-app,app.kubernetes.io/instance=flask-release" -o jsonpath="{.items[0].metadata.name}")   
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
PS C:\Users\egora\PycharmProjects\S25-core-course-labs\k8s> helm list
NAME            NAMESPACE       REVISION        UPDATED                                 STATUS          CHART           APP VERSION
flask-release   default         1               2025-02-24 21:02:04.7285337 +0300 MSK   deployed        flask-app-0.1.0 1.16.0
```

```text
PS C:\Users\egora\PycharmProjects\S25-core-course-labs> kubectl get pods,svc
NAME                                           READY   STATUS    RESTARTS   AGE
pod/flask-release-flask-app-6b58c55478-2gghl   1/1     Running   0          2m1s
pod/flask-release-flask-app-6b58c55478-gc9kt   1/1     Running   0          2m1s
pod/flask-release-flask-app-6b58c55478-gsskl   1/1     Running   0          2m1s

NAME                              TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
service/flask-release-flask-app   ClusterIP   10.97.150.171   <none>        80/TCP    2m1s
service/kubernetes                ClusterIP   10.96.0.1       <none>        443/TCP   7m13s
```

```text
PS C:\Users\egora\PycharmProjects\S25-core-course-labs\k8s> minikube service flask-release-flask-app --url
* service default/flask-release-flask-app has no node port
! Services [default/flask-release-flask-app] have type "ClusterIP" not meant to be exposed, however for local development minikube allows you to access this !
http://127.0.0.1:60976
! Because you are using a Docker driver on windows, the terminal needs to be open to run it.
```

```text
PS C:\Users\egora\PycharmProjects\S25-core-course-labs> minikube service flask-release-flask-app
|-----------|-------------------------|-------------|--------------|
| NAMESPACE |          NAME           | TARGET PORT |     URL      |
|-----------|-------------------------|-------------|--------------|
| default   | flask-release-flask-app |             | No node port |
|-----------|-------------------------|-------------|--------------|
* service default/flask-release-flask-app has no node port
! Services [default/flask-release-flask-app] have type "ClusterIP" not meant to be exposed, however for local development minikube allows you to access this !
* Starting tunnel for service flask-release-flask-app.
|-----------|-------------------------|-------------|------------------------|
| NAMESPACE |          NAME           | TARGET PORT |          URL           |
|-----------|-------------------------|-------------|------------------------|
| default   | flask-release-flask-app |             | http://127.0.0.1:61376 |
|-----------|-------------------------|-------------|------------------------|
* Opening service default/flask-release-flask-app in default browser...
! Because you are using a Docker driver on windows, the terminal needs to be open to run it.
```

[Screenshot of running app](screenshots/helm/app_python_running.png)

[Workloads](screenshots/helm/workloads.png)

## Helm Hooks

```text
PS C:\Users\egora\PycharmProjects\S25-core-course-labs\k8s> helm lint ./flask-app
==> Linting ./flask-app
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed
```

```text
PS C:\Users\egora\PycharmProjects\S25-core-course-labs\k8s> helm install --dry-run helm-hooks ./flask-app
NAME: helm-hooks
LAST DEPLOYED: Tue Feb 25 10:19:33 2025
NAMESPACE: default
STATUS: pending-install
REVISION: 1
HOOKS:
---
# Source: flask-app/templates/post-install-hook.yaml
apiVersion: v1
kind: Pod
metadata:
  name: postinstall-hook
  annotations:
    "helm.sh/hook": "post-install"
spec:
  containers:
    - name: post-install-container
      image: busybox
      imagePullPolicy: Always
      command: ['sh', '-c', 'echo The post-install hook is running && sleep 15']
  restartPolicy: Never
---
# Source: flask-app/templates/pre-install-hook.yaml
apiVersion: v1
kind: Pod
metadata:
  name: preinstall-hook
  annotations:
    "helm.sh/hook": "pre-install"
spec:
  containers:
    - name: pre-install-container
      image: busybox
      imagePullPolicy: IfNotPresent
      command: ['sh', '-c', 'echo The pre-install hook is running && sleep 20']
  restartPolicy: Never
---

... (too long)
```

```text
PS C:\Users\egora\PycharmProjects\S25-core-course-labs\k8s> kubectl get po
NAME                                       READY   STATUS      RESTARTS   AGE
flask-release-flask-app-6b58c55478-26mqr   1/1     Running     0          31s
flask-release-flask-app-6b58c55478-mj8j6   1/1     Running     0          32s
flask-release-flask-app-6b58c55478-qzfcl   1/1     Running     0          31s
postinstall-hook                           0/1     Completed   0          31s
preinstall-hook                            0/1     Completed   0          58s
```

Preinstall hook:

```text
PS C:\Users\egora\PycharmProjects\S25-core-course-labs\k8s> kubectl describe po preinstall-hook
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 25 Feb 2025 18:22:28 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.6
IPs:
  IP:  10.244.0.6
Containers:
  pre-install-container:
    Container ID:  docker://7842d496c0cc9acade1ac34beda21a2a3f4923575ab7947ff81e09244bc02235
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
      Started:      Tue, 25 Feb 2025 18:22:32 +0300
      Finished:     Tue, 25 Feb 2025 18:22:52 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-s45zg (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False
  Initialized                 True
  Ready                       False
  ContainersReady             False
  PodScheduled                True
Volumes:
  kube-api-access-s45zg:
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
  Normal  Scheduled  103s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulling    103s  kubelet            Pulling image "busybox"
  Normal  Pulled     99s   kubelet            Successfully pulled image "busybox" in 3.602s (3.602s including waiting). Image size: 4269694 bytes.
  Normal  Created    99s   kubelet            Created container: pre-install-container
  Normal  Started    99s   kubelet            Started container pre-install-container
```

Postinstall hook:

```text
PS C:\Users\egora\PycharmProjects\S25-core-course-labs\k8s> kubectl describe po postinstall-hook
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 25 Feb 2025 18:22:55 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.9
IPs:
  IP:  10.244.0.9
Containers:
  post-install-container:
    Container ID:  docker://58d1a174529cfbb6070acc704980956e46b3de1e56bcd3f9b41227b1202ec231
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
      Started:      Tue, 25 Feb 2025 18:23:04 +0300
      Finished:     Tue, 25 Feb 2025 18:23:19 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-4jjss (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False
  Initialized                 True
  Ready                       False
  ContainersReady             False
  PodScheduled                True
Volumes:
  kube-api-access-4jjss:
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
  Normal  Scheduled  2m20s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    2m20s  kubelet            Pulling image "busybox"
  Normal  Pulled     2m11s  kubelet            Successfully pulled image "busybox" in 1.41s (8.681s including waiting). Image size: 4269694 bytes.
  Normal  Created    2m11s  kubelet            Created container: post-install-container
  Normal  Started    2m11s  kubelet            Started container post-install-container
```

With delete policy:

```text
PS C:\Users\egora\PycharmProjects\S25-core-course-labs\k8s> kubectl get pods,svc
NAME                                           READY   STATUS    RESTARTS   AGE
pod/flask-release-flask-app-6b58c55478-5sd2t   1/1     Running   0          19m
pod/flask-release-flask-app-6b58c55478-dbq6s   1/1     Running   0          19m
pod/flask-release-flask-app-6b58c55478-ww29n   1/1     Running   0          19m

NAME                              TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
service/flask-release-flask-app   ClusterIP   10.99.139.226   <none>        80/TCP    19m
service/kubernetes                ClusterIP   10.96.0.1       <none>        443/TCP   47m
```

## Bonus

### Helm for Kotlin Ktor app

```text
PS C:\Users\egora\PycharmProjects\S25-core-course-labs\k8s> helm install ktor-release ./ktor-app
NAME: ktor-release
LAST DEPLOYED: Tue Feb 25 22:37:38 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=ktor-app,app.kubernetes.io/instance=ktor-release" -o jsonpath="{.items[0].metadata.name}")      
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
NAME                                           READY   STATUS    RESTARTS        AGE
pod/flask-release-flask-app-6b58c55478-5sd2t   1/1     Running   1 (2m40s ago)   3h48m
pod/flask-release-flask-app-6b58c55478-dbq6s   1/1     Running   1 (2m40s ago)   3h48m
pod/flask-release-flask-app-6b58c55478-ww29n   1/1     Running   1 (2m40s ago)   3h48m
pod/ktor-release-ktor-app-57c4c59f4-kp5dc      1/1     Running   0               25s
pod/ktor-release-ktor-app-57c4c59f4-rjv4v      1/1     Running   0               25s

NAME                              TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
service/flask-release-flask-app   ClusterIP   10.99.139.226    <none>        80/TCP    3h48m
service/ktor-release-ktor-app     ClusterIP   10.106.147.197   <none>        80/TCP    25s
```

```text
PS C:\Users\egora\PycharmProjects\S25-core-course-labs\k8s> kubectl get pods,svc
NAME                                        READY   STATUS    RESTARTS   AGE
pod/ktor-release-ktor-app-57c4c59f4-kp5dc   1/1     Running   0          98s
pod/ktor-release-ktor-app-57c4c59f4-rjv4v   1/1     Running   0          98s

NAME                            TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
service/ktor-release-ktor-app   ClusterIP   10.106.147.197   <none>        80/TCP    98s
service/kubernetes              ClusterIP   10.96.0.1        <none>        443/TCP   4h17m
```

### Library Chart usage

Everything is defined in the [./library-charts/common](./library-charts/common)

```text
PS C:\Users\egora\PycharmProjects\S25-core-course-labs\k8s> helm dependency update ./flask-app
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "stable" chart repository
Update Complete. ⎈Happy Helming!⎈
Saving 1 charts
Deleting outdated charts
PS C:\Users\egora\PycharmProjects\S25-core-course-labs\k8s> helm dependency update ./ktor-app
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "stable" chart repository
Update Complete. ⎈Happy Helming!⎈
Deleting outdated charts
NAME: flask-release
LAST DEPLOYED: Tue Feb 25 22:57:46 2025
NAMESPACE: default
REVISION: 1
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=flask-app,app.kubernetes.io/instance=flask-release" -o jsonpath="{.items[0].metadata.name}")    
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
PS C:\Users\egora\PycharmProjects\S25-core-course-labs\k8s> helm install ktor-release ./ktor-app
NAME: ktor-release
LAST DEPLOYED: Tue Feb 25 23:01:05 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=ktor-app,app.kubernetes.io/instance=ktor-release" -o jsonpath="{.items[0].metadata.name}")      
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
```

```text
PS C:\Users\egora\PycharmProjects\S25-core-course-labs\k8s> kubectl get pods,svc
NAME                                          READY   STATUS    RESTARTS   AGE
pod/flask-release-flask-app-9fccd5cf9-b8s85   1/1     Running   0          3m2s
pod/flask-release-flask-app-9fccd5cf9-tqq8f   1/1     Running   0          3m2s
pod/flask-release-flask-app-9fccd5cf9-zz2tg   1/1     Running   0          3m2s
pod/ktor-release-ktor-app-6b47b95dfb-t5dvb    0/1     Running   0          7s
pod/ktor-release-ktor-app-6b47b95dfb-tfwcq    0/1     Running   0          7s

NAME                              TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
service/flask-release-flask-app   ClusterIP   10.101.235.213   <none>        80/TCP    3m2s
service/ktor-release-ktor-app     ClusterIP   10.109.227.144   <none>        80/TCP    7s
service/kubernetes                ClusterIP   10.96.0.1        <none>        443/TCP   4h39m
```
