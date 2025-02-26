# Helm

## Python
```angular2html
 helm install py-app python-app/
NAME: py-app
LAST DEPLOYED: Wed Feb 26 22:13:28 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=python-app,app.kubernetes.io/instance=py-app" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT

```

### Service
```angular2html
 minikube service python-app
|-----------|------------|-------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | python-app |          80 | http://192.168.49.2:30907 |
|-----------|------------|-------------|---------------------------|
🏃  Starting tunnel for service python-app.
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | python-app |             | http://127.0.0.1:35661 |
|-----------|------------|-------------|------------------------|
🎉  Opening service default/python-app in default browser...
👉  http://127.0.0.1:35661
❗  Because you are using a Docker driver on linux, the terminal needs to be open to run it.

```

### Command `kubectl get pods,svc`

```angular2html
dasha@LAPTOP-382BEF3K:~/devops/devops_labs/k8s$ kubectl get pods,svc
NAME                                     READY   STATUS    RESTARTS   AGE
pod/py-app-python-app-585c94c576-7gkhj   1/1     Running   0          5s
pod/py-app-python-app-585c94c576-ncxgm   1/1     Running   0          5s
pod/py-app-python-app-585c94c576-znwlk   1/1     Running   0          5s
pod/python-app-7b48846ccd-pg2pj          1/1     Running   0          35m

NAME                        TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
service/kubernetes          ClusterIP   10.96.0.1      <none>        443/TCP        97m
service/py-app-python-app   ClusterIP   10.98.117.4    <none>        80/TCP         5s
service/python-app          NodePort    10.98.115.40   <none>        80:30907/TCP   35m

```

## Troubleshoot Hooks

```angular2html
 helm lint python-app/
==> Linting python-app/
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed

```

```angular2html
 helm install --dry-run helm-hooks python-app
NAME: helm-hooks
LAST DEPLOYED: Wed Feb 26 22:29:21 2025
NAMESPACE: default
STATUS: pending-install
REVISION: 1
HOOKS:
---
# Source: python-app/templates/post-install-hooks.yml
apiVersion: v1
kind: Pod
metadata:
   name: postinstall-hook
   annotations:
       "helm.sh/hook": "post-install"
       "helm.sh/hook-delete-policy": "hook-succeeded"
spec:
  containers:
  - name: post-install-container
    image: busybox
    imagePullPolicy: Always
    command: ['sh', '-c', 'echo The post-install hook is running && sleep 15' ]
  restartPolicy: Never
  terminationGracePeriodSeconds: 0
---
# Source: python-app/templates/pre-install-hooks.yml
apiVersion: v1
kind: Pod
metadata:
   name: preinstall-hook
   annotations:
       "helm.sh/hook": "pre-install"
       "helm.sh/hook-delete-policy": "hook-succeeded"
spec:
  containers:
  - name: pre-install-container
    image: busybox
    imagePullPolicy: IfNotPresent
    command: ['sh', '-c', 'echo The pre-install hook is running && sleep 20' ]
  restartPolicy: Never
  terminationGracePeriodSeconds: 0
---
# Source: python-app/templates/tests/test-connection.yaml
apiVersion: v1
kind: Pod
metadata:
  name: "helm-hooks-python-app-test-connection"
  labels:
    helm.sh/chart: python-app-0.1.0
    app.kubernetes.io/name: python-app
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
      args: ['helm-hooks-python-app:80']
  restartPolicy: Never
MANIFEST:
---
# Source: python-app/templates/serviceaccount.yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: helm-hooks-python-app
  labels:
    helm.sh/chart: python-app-0.1.0
    app.kubernetes.io/name: python-app
    app.kubernetes.io/instance: helm-hooks
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
automountServiceAccountToken: true
---
# Source: python-app/templates/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: helm-hooks-python-app
  labels:
    helm.sh/chart: python-app-0.1.0
    app.kubernetes.io/name: python-app
    app.kubernetes.io/instance: helm-hooks
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
spec:
  type: ClusterIP
  ports:
    - port: 80
      targetPort: http
      protocol: TCP
      name: http
  selector:
    app.kubernetes.io/name: python-app
    app.kubernetes.io/instance: helm-hooks
---
# Source: python-app/templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: helm-hooks-python-app
  labels:
    helm.sh/chart: python-app-0.1.0
    app.kubernetes.io/name: python-app
    app.kubernetes.io/instance: helm-hooks
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
spec:
  replicas: 3
  selector:
    matchLabels:
      app.kubernetes.io/name: python-app
      app.kubernetes.io/instance: helm-hooks
  template:
    metadata:
      labels:
        helm.sh/chart: python-app-0.1.0
        app.kubernetes.io/name: python-app
        app.kubernetes.io/instance: helm-hooks
        app.kubernetes.io/version: "1.16.0"
        app.kubernetes.io/managed-by: Helm
    spec:
      serviceAccountName: helm-hooks-python-app
      containers:
        - name: python-app
          image: "dtolmach/python-app-monitor:latest"
          imagePullPolicy: IfNotPresent
          ports:
            - name: http
              containerPort: 80
              protocol: TCP

NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=python-app,app.kubernetes.io/instance=helm-hooks" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT

```

```angular2html
kubectl get po
NAME                                 READY   STATUS      RESTARTS   AGE
post-install-job-drh66               0/1     Completed   0          7m5s
preinstall-hook                      0/1     Completed   0          2m17s
py-app-python-app-585c94c576-7gkhj   1/1     Running     0          14m
py-app-python-app-585c94c576-ncxgm   1/1     Running     0          14m
py-app-python-app-585c94c576-znwlk   1/1     Running     0          14m
python-app-7b48846ccd-pg2pj          1/1     Running     0          50m

```

```angular2html
kubectl describe po preinstall-hook
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 26 Feb 2025 22:28:33 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
                  helm.sh/hook-delete-policy: hook-succeeded
Status:           Succeeded
IP:               10.244.0.42
IPs:
  IP:  10.244.0.42
Containers:
  pre-install-container:
    Container ID:  docker://22cba6004739f29d38c8f6842704a8b7d17728376671060b77e53bec7e9f97fc
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
      Started:      Wed, 26 Feb 2025 22:28:34 +0300
      Finished:     Wed, 26 Feb 2025 22:28:54 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-c5hgs (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False
  Initialized                 True
  Ready                       False
  ContainersReady             False
  PodScheduled                True
Volumes:
  kube-api-access-c5hgs:
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
  Normal  Scheduled  3m46s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     3m45s  kubelet            Container image "busybox" already present on machine
  Normal  Created    3m45s  kubelet            Created container: pre-install-container
  Normal  Started    3m45s  kubelet            Started container pre-install-container

```

```angular2html
kubectl describe po post-install-job-drh66 
Name:             post-install-job-drh66
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 26 Feb 2025 22:23:45 +0300
Labels:           batch.kubernetes.io/controller-uid=a41ae6cc-ab83-4ca2-9cc6-f3bca076b05b
                  batch.kubernetes.io/job-name=post-install-job
                  controller-uid=a41ae6cc-ab83-4ca2-9cc6-f3bca076b05b
                  job-name=post-install-job
Annotations:      <none>
Status:           Succeeded
IP:               10.244.0.37
IPs:
  IP:           10.244.0.37
Controlled By:  Job/post-install-job
Containers:
  post-install:
    Container ID:  docker://7bd455187b5dd1cde5e92331848418c64f1cf2814733f9d2080d8bfeb416f5eb
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
      Started:      Wed, 26 Feb 2025 22:23:51 +0300
      Finished:     Wed, 26 Feb 2025 22:24:12 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-gc2kq (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False
  Initialized                 True
  Ready                       False
  ContainersReady             False
  PodScheduled                True
Volumes:
  kube-api-access-gc2kq:
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
  Normal  Scheduled  9m11s  default-scheduler  Successfully assigned default/post-install-job-drh66 to minikube
  Normal  Pulling    9m9s   kubelet            Pulling image "busybox"
  Normal  Pulled     9m6s   kubelet            Successfully pulled image "busybox" in 2.62s (2.62s including waiting). Image size: 4269694 bytes.
  Normal  Created    9m6s   kubelet            Created container: post-install
  Normal  Started    9m4s   kubelet            Started container post-install
dasha@LAPTOP-382BEF3K:~/devops/devops_labs/k8s$

```

## Go app

```angular2html
 helm install go-app go-app
NAME: go-app
LAST DEPLOYED: Wed Feb 26 22:41:32 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=go-app,app.kubernetes.io/instance=go-app" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
dasha@LAPTOP-382BEF3K:~/devops/devops_labs/k8s$

```

### Command `kubectl get pods,svc`

```angular2html
$ kubectl get pods,svc
NAME                              READY   STATUS      RESTARTS   AGE
pod/go-app-668c5f9bf7-8wt9p       1/1     Running     0          67s
pod/go-app-668c5f9bf7-cbdgf       1/1     Running     0          67s
pod/go-app-668c5f9bf7-v25hx       1/1     Running     0          67s
pod/post-install-job-drh66        0/1     Completed   0          18m
pod/preinstall-hook               0/1     Completed   0          14m
pod/python-app-7b48846ccd-pg2pj   1/1     Running     0          62m

NAME                 TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
service/go-app       ClusterIP   10.108.132.228   <none>        80/TCP         67s
service/kubernetes   ClusterIP   10.96.0.1        <none>        443/TCP        124m
service/python-app   NodePort    10.98.115.40     <none>        80:30907/TCP   61m

```

