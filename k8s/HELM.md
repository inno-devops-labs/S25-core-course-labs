#  Introduction to Helm
## Helm Setup and Chart Creation
### Create helm chart and install app:
```bash
sg@sg-BBR-WAX9:~/DevOps/S25-core-course-labs/k8s$ helm install my-django-app ./my-django-app
NAME: my-django-app
LAST DEPLOYED: Tue Feb 25 21:03:41 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=my-django-app,app.kubernetes.io/instance=my-django-app" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
  ```
### Pods in Minikube Workloads
![alt text](image-1.png)

```bash
sg@sg-BBR-WAX9:~/DevOps/S25-core-course-labs/k8s$ minikube service my-django-app
|-----------|---------------|-------------|---------------------------|
| NAMESPACE |     NAME      | TARGET PORT |            URL            |
|-----------|---------------|-------------|---------------------------|
| default   | my-django-app | http/8082   | http://192.168.49.2:31167 |
|-----------|---------------|-------------|---------------------------|
🎉  Opening service default/my-django-app in default browser...
sg@sg-BBR-WAX9:~/DevOps/S25-core-course-labs/k8s$ kubectl get pods,svc
NAME                                 READY   STATUS    RESTARTS       AGE
pod/my-dart-app-75dcc6cc48-5rm5d     1/1     Running   14 (15m ago)   4h16m
pod/my-dart-app-75dcc6cc48-kt87l     1/1     Running   14 (15m ago)   4h16m
pod/my-dart-app-75dcc6cc48-s4klk     1/1     Running   14 (15m ago)   4h16m
pod/my-django-app-5f795b8589-j5hcc   1/1     Running   0              8m24s
pod/my-django-app-5f795b8589-l8bfg   1/1     Running   0              8m24s
pod/my-django-app-5f795b8589-sr5n4   1/1     Running   0              8m24s
pod/mysql-1740505581-0               1/1     Running   1 (15m ago)    41m

NAME                                TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/kubernetes                  ClusterIP   10.96.0.1        <none>        443/TCP          8h
service/my-dart-app                 NodePort    10.101.222.145   <none>        8081:32742/TCP   4h16m
service/my-django-app               NodePort    10.107.30.221    <none>        8082:31167/TCP   8m24s
service/mysql-1740505581            ClusterIP   10.101.183.169   <none>        3306/TCP         41m
service/mysql-1740505581-headless   ClusterIP   None             <none>        3306/TCP         41m
```
## Helm Chart Hooks

### Troubleshoot Hooks:
```bash
sg@sg-BBR-WAX9:~/DevOps/S25-core-course-labs/k8s$ helm lint my-django-app
==> Linting my-django-app
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed
sg@sg-BBR-WAX9:~/DevOps/S25-core-course-labs/k8s$ helm install --dry-run helm-hooks my-django-app
NAME: helm-hooks
LAST DEPLOYED: Tue Feb 25 21:44:00 2025
NAMESPACE: default
STATUS: pending-install
REVISION: 1
HOOKS:
---
# Source: my-django-app/templates/post-install-hook.yml
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
    command: ['sh', '-c', 'echo The post-install hook is running && sleep 15' ]
  restartPolicy: Never
  terminationGracePeriodSeconds: 0
---
# Source: my-django-app/templates/pre-install-hook.yml
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
    command: ['sh', '-c', 'echo The pre-install hook is running && sleep 20' ]
  restartPolicy: Never
  terminationGracePeriodSeconds: 0
---
# Source: my-django-app/templates/tests/test-connection.yaml
apiVersion: v1
kind: Pod
metadata:
  name: "helm-hooks-my-django-app-test-connection"
  labels:
    helm.sh/chart: my-django-app-0.1.0
    app.kubernetes.io/name: my-django-app
    app.kubernetes.io/instance: helm-hooks
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
  annotations:
    "helm.sh/hook": test
spec:
  containers:
    - name: wget
      image: busybox
      command: ['wget']
      args: ['helm-hooks-my-django-app:8082']
  restartPolicy: Never
MANIFEST:
---
# Source: my-django-app/templates/serviceaccount.yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: helm-hooks-my-django-app
  labels:
    helm.sh/chart: my-django-app-0.1.0
    app.kubernetes.io/name: my-django-app
    app.kubernetes.io/instance: helm-hooks
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
automountServiceAccountToken: true
---
# Source: my-django-app/templates/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: helm-hooks-my-django-app
  labels:
    helm.sh/chart: my-django-app-0.1.0
    app.kubernetes.io/name: my-django-app
    app.kubernetes.io/instance: helm-hooks
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
spec:
  type: NodePort
  ports:
    - port: 8082
      targetPort: http
      protocol: TCP
      name: http
  selector:
    app.kubernetes.io/name: my-django-app
    app.kubernetes.io/instance: helm-hooks
---
# Source: my-django-app/templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: helm-hooks-my-django-app
  labels:
    helm.sh/chart: my-django-app-0.1.0
    app.kubernetes.io/name: my-django-app
    app.kubernetes.io/instance: helm-hooks
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
spec:
  replicas: 3
  selector:
    matchLabels:
      app.kubernetes.io/name: my-django-app
      app.kubernetes.io/instance: helm-hooks
  template:
    metadata:
      labels:
        helm.sh/chart: my-django-app-0.1.0
        app.kubernetes.io/name: my-django-app
        app.kubernetes.io/instance: helm-hooks
        app.kubernetes.io/version: "1.16.0"
        app.kubernetes.io/managed-by: Helm
    spec:
      serviceAccountName: helm-hooks-my-django-app
      containers:
        - name: my-django-app
          image: "g1l1a/my-django-app:v2.4"
          imagePullPolicy: IfNotPresent
          ports:
            - name: http
              containerPort: 8082
              protocol: TCP

NOTES:
1. Get the application URL by running these commands:
  export NODE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services helm-hooks-my-django-app)
  export NODE_IP=$(kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
  echo http://$NODE_IP:$NODE_PORT
sg@sg-BBR-WAX9:~/DevOps/S25-core-course-labs/k8s$ kubectl get po
NAME                             READY   STATUS    RESTARTS       AGE
my-dart-app-75dcc6cc48-5rm5d     1/1     Running   14 (32m ago)   4h33m
my-dart-app-75dcc6cc48-kt87l     1/1     Running   14 (32m ago)   4h33m
my-dart-app-75dcc6cc48-s4klk     1/1     Running   14 (32m ago)   4h33m
my-django-app-5f795b8589-j5hcc   1/1     Running   0              24m
my-django-app-5f795b8589-l8bfg   1/1     Running   0              24m
my-django-app-5f795b8589-sr5n4   1/1     Running   0              24m
mysql-1740505581-0               1/1     Running   1 (32m ago)    58m
```
### Hook with deletion policy
```bash
sg@sg-BBR-WAX9:~/DevOps/S25-core-course-labs/k8s$ kubectl get po
NAME                             READY   STATUS    RESTARTS       AGE
my-dart-app-75dcc6cc48-5rm5d     1/1     Running   14 (32m ago)   4h33m
my-dart-app-75dcc6cc48-kt87l     1/1     Running   14 (32m ago)   4h33m
my-dart-app-75dcc6cc48-s4klk     1/1     Running   14 (32m ago)   4h33m
my-django-app-5f795b8589-j5hcc   1/1     Running   0              24m
my-django-app-5f795b8589-l8bfg   1/1     Running   0              24m
my-django-app-5f795b8589-sr5n4   1/1     Running   0              24m
mysql-1740505581-0               1/1     Running   1 (32m ago)    58m
```

### Hook without deletion policy
```bash
sg@sg-BBR-WAX9:~/DevOps/S25-core-course-labs/k8s$ helm install my-django-app ./my-django-app
NAME: my-django-app
LAST DEPLOYED: Tue Feb 25 21:49:03 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export NODE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services my-django-app)
  export NODE_IP=$(kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
  echo http://$NODE_IP:$NODE_PORT
sg@sg-BBR-WAX9:~/DevOps/S25-core-course-labs/k8s$ kubectl get po
NAME                             READY   STATUS      RESTARTS       AGE
my-dart-app-75dcc6cc48-5rm5d     1/1     Running     14 (37m ago)   4h38m
my-dart-app-75dcc6cc48-kt87l     1/1     Running     14 (37m ago)   4h38m
my-dart-app-75dcc6cc48-s4klk     1/1     Running     14 (37m ago)   4h38m
my-django-app-5f795b8589-86rvv   1/1     Running     0              30s
my-django-app-5f795b8589-c2v8n   1/1     Running     0              30s
my-django-app-5f795b8589-gfdr7   1/1     Running     0              30s
mysql-1740505581-0               1/1     Running     1 (37m ago)    63m
postinstall-hook                 0/1     Completed   0              30s
preinstall-hook                  0/1     Completed   0              58s
```
## Po and Describe postinstall and preinstall hooks
```bash
sg@sg-BBR-WAX9:~/DevOps/S25-core-course-labs/k8s$ kubectl describe po postinstall-hook
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 25 Feb 2025 21:49:31 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.57
IPs:
  IP:  10.244.0.57
Containers:
  post-install-container:
    Container ID:  docker://955d8add65e20f97c98ba8cb3702ca12d96ed4e27079d3bf9ca03b5126303657
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
      Started:      Tue, 25 Feb 2025 21:49:33 +0300
      Finished:     Tue, 25 Feb 2025 21:49:48 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-cjh59 (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-cjh59:
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
  Normal  Scheduled  6m31s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    6m31s  kubelet            Pulling image "busybox"
  Normal  Pulled     6m29s  kubelet            Successfully pulled image "busybox" in 2.113s (2.113s including waiting). Image size: 4269694 bytes.
  Normal  Created    6m29s  kubelet            Created container: post-install-container
  Normal  Started    6m29s  kubelet            Started container post-install-container
sg@sg-BBR-WAX9:~/DevOps/S25-core-course-labs/k8s$ kubectl describe po preinstall-hook
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 25 Feb 2025 21:49:03 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.53
IPs:
  IP:  10.244.0.53
Containers:
  pre-install-container:
    Container ID:  docker://c152b150fa2f079f491214069418f6b82abda83c94f8ec94b1e16f4b7e675c9a
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
      Started:      Tue, 25 Feb 2025 21:49:09 +0300
      Finished:     Tue, 25 Feb 2025 21:49:29 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-sbggc (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-sbggc:
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
  Normal  Scheduled  7m10s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulling    7m11s  kubelet            Pulling image "busybox"
  Normal  Pulled     7m5s   kubelet            Successfully pulled image "busybox" in 5.445s (5.445s including waiting). Image size: 4269694 bytes.
  Normal  Created    7m5s   kubelet            Created container: pre-install-container
  Normal  Started    7m5s   kubelet            Started container pre-install-container
```

## Bonus task: Helm Library Chart
### Helm Chart for dart application
```bash
sg@sg-BBR-WAX9:~/DevOps/S25-core-course-labs/k8s$ helm install my-dart-app ./my-dart-app
NAME: my-dart-app
LAST DEPLOYED: Tue Feb 25 22:20:58 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export NODE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services my-dart-app)
  export NODE_IP=$(kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
  echo http://$NODE_IP:$NODE_PORT
```

### Helm Library Chart
```bash
sg@sg-BBR-WAX9:~/DevOps/S25-core-course-labs/k8s$ helm dependency update my-django-app
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "bitnami" chart repository
Update Complete. ⎈Happy Helming!⎈
Saving 1 charts
Deleting outdated charts
sg@sg-BBR-WAX9:~/DevOps/S25-core-course-labs/k8s$ helm dependency update my-dart-
app
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "bitnami" chart repository
Update Complete. ⎈Happy Helming!⎈
Saving 1 charts
Deleting outdated charts
```
### All pods and services
```bash
sg@sg-BBR-WAX9:~/DevOps/S25-core-course-labs/k8s$ kubectl get pods,svc
NAME                                 READY   STATUS      RESTARTS      AGE
pod/my-dart-app-6ff6678b89-29lrw     1/1     Running     0             23m
pod/my-dart-app-6ff6678b89-f4sxw     1/1     Running     0             23m
pod/my-dart-app-6ff6678b89-g6rn4     1/1     Running     0             23m
pod/my-django-app-5f795b8589-86rvv   1/1     Running     0             54m
pod/my-django-app-5f795b8589-c2v8n   1/1     Running     0             54m
pod/my-django-app-5f795b8589-gfdr7   1/1     Running     0             54m
pod/mysql-1740505581-0               1/1     Running     1 (91m ago)   117m
pod/postinstall-hook                 0/1     Completed   0             54m
pod/preinstall-hook                  0/1     Completed   0             54m

NAME                                TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/kubernetes                  ClusterIP   10.96.0.1        <none>        443/TCP          10h
service/my-dart-app                 NodePort    10.111.104.190   <none>        8081:30781/TCP   23m
service/my-django-app               NodePort    10.102.77.191    <none>        8082:31459/TCP   54m
service/mysql-1740505581            ClusterIP   10.101.183.169   <none>        3306/TCP         117m
service/mysql-1740505581-headless   ClusterIP   None             <none>        3306/TCP         117m
```