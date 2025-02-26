# Helm

Install Helm, verify the Workloads page in the Minikube dashboard.

<img width="1468" alt="Снимок экрана 2025-02-27 в 00 41 40" src="https://github.com/user-attachments/assets/e1387691-8abf-4d92-97f0-3d6c6cd0b754" />

## Deploy moscow-time app using Helm

Create helm chart for python app:

```bash
helm create moscow-time
```

Change `values.yaml` and install helm chart:

```bash
ebob@laptop k8s % helm install moscow-time ./moscow-time
NAME: moscow-time
LAST DEPLOYED: Sun Feb 23 03:58:30 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
```

```bash
ebob@laptop ~ % kubectl get pods,svc
NAME                               READY   STATUS    RESTARTS   AGE
pod/moscow-time-7bcf4d744f-4hndm   1/1     Running   0          13h
pod/moscow-time-7bcf4d744f-84pq6   1/1     Running   0          13h
pod/moscow-time-7bcf4d744f-lwbg9   1/1     Running   0          13h

NAME                  TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
service/kubernetes    ClusterIP   10.96.0.1      <none>        443/TCP   15h
service/moscow-time   ClusterIP   10.110.30.20   <none>        80/TCP    13h
```

```bash
ebob@laptop ~ % minikube service --all
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
|-----------|-------------|-------------|--------------|
| NAMESPACE |    NAME     | TARGET PORT |     URL      |
|-----------|-------------|-------------|--------------|
| default   | moscow-time |             | No node port |
|-----------|-------------|-------------|--------------|
😿  service default/moscow-time has no node port
❗  Services [default/kubernetes default/moscow-time] have type "ClusterIP" not meant to be exposed, however for local development minikube allows you to access this !
🏃  Starting tunnel for service kubernetes.
🏃  Starting tunnel for service moscow-time.
|-----------|-------------|-------------|------------------------|
| NAMESPACE |    NAME     | TARGET PORT |          URL           |
|-----------|-------------|-------------|------------------------|
| default   | kubernetes  |             | http://127.0.0.1:52535 |
| default   | moscow-time |             | http://127.0.0.1:52536 |
|-----------|-------------|-------------|------------------------|
🎉  Opening service default/kubernetes in default browser...
🎉  Opening service default/moscow-time in default browser...
❗  Because you are using a Docker driver on darwin, the terminal needs to be open to run it.
```

## Helm Chart Hooks

### `helm lint`

```bash
ebob@laptop k8s % helm lint moscow-time
==> Linting moscow-time
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed
```

### `helm install --dry-run helm-hooks`

```bash
ebob@laptop k8s % helm install --dry-run helm-hooks moscow-time
NAME: helm-hooks
LAST DEPLOYED: Sun Feb 23 18:23:42 2025
NAMESPACE: default
STATUS: pending-install
REVISION: 1
HOOKS:
---
# Source: moscow-time/templates/post-install-hook.yaml
apiVersion: v1
kind: Pod
metadata:
  name: helm-hooks-moscow-time-post-install
  annotations:
    "helm.sh/hook": post-install
    "helm.sh/hook-weight": "5"
    #"helm.sh/hook-delete-policy": hook-succeeded
spec:
  restartPolicy: Never
  containers:
  - name: post-install-job
    image: busybox
    command: ['sh', '-c', 'echo "Starting post-install hook"; sleep 20; echo "Post-install hook completed"']
---
# Source: moscow-time/templates/pre-install-hook.yaml
apiVersion: v1
kind: Pod
metadata:
  name: helm-hooks-moscow-time-pre-install
  annotations:
    "helm.sh/hook": pre-install
    "helm.sh/hook-weight": "-5"
    #"helm.sh/hook-delete-policy": hook-succeeded
spec:
  restartPolicy: Never
  containers:
  - name: pre-install-job
    image: busybox
    command: ['sh', '-c', 'echo "Starting pre-install hook"; sleep 20; echo "Pre-install hook completed"']
---
# Source: moscow-time/templates/tests/test-connection.yaml
apiVersion: v1
kind: Pod
metadata:
  name: "helm-hooks-moscow-time-test-connection"
  labels:
    helm.sh/chart: moscow-time-0.1.0
    app.kubernetes.io/name: moscow-time
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
      args: ['helm-hooks-moscow-time:80']
  restartPolicy: Never
MANIFEST:
---
# Source: moscow-time/templates/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: helm-hooks-moscow-time
  labels:
    helm.sh/chart: moscow-time-0.1.0
    app.kubernetes.io/name: moscow-time
    app.kubernetes.io/instance: helm-hooks
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
spec:
  type: ClusterIP
  ports:
    - port: 80
      targetPort: 8080
      protocol: TCP
      name: http
  selector:
    app.kubernetes.io/name: moscow-time
    app.kubernetes.io/instance: helm-hooks
---
# Source: moscow-time/templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: helm-hooks-moscow-time
  labels:
    helm.sh/chart: moscow-time-0.1.0
    app.kubernetes.io/name: moscow-time
    app.kubernetes.io/instance: helm-hooks
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
spec:
  replicas: 3
  selector:
    matchLabels:
      app.kubernetes.io/name: moscow-time
      app.kubernetes.io/instance: helm-hooks
  template:
    metadata:
      labels:
        app.kubernetes.io/name: moscow-time
        app.kubernetes.io/instance: helm-hooks
    spec:
      containers:
        - name: moscow-time
          image: "ebob/moscow-time:v1.1"
          imagePullPolicy: IfNotPresent
          ports:
            - name: http
              containerPort: 8080
              protocol: TCP
          resources:
            limits:
              cpu: 500m
              memory: 128Mi
            requests:
              cpu: 250m
              memory: 64Mi
---
# Source: moscow-time/templates/ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: helm-hooks-moscow-time
  labels:
    helm.sh/chart: moscow-time-0.1.0
    app.kubernetes.io/name: moscow-time
    app.kubernetes.io/instance: helm-hooks
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx
  rules:
    - host: "moscow-time.local"
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: helm-hooks-moscow-time
                port:
                  number: 80
```

### `kubectl get po`

```bash
ebob@laptop ~ % kubectl get po
NAME                           READY   STATUS      RESTARTS   AGE
moscow-time-7bcf4d744f-fhbmt   1/1     Running     0          3m51s
moscow-time-7bcf4d744f-j7hqx   1/1     Running     0          3m51s
moscow-time-7bcf4d744f-lmzxq   1/1     Running     0          3m51s
moscow-time-post-install       0/1     Completed   0          3m51s
moscow-time-pre-install        0/1     Completed   0          4m18s
```

### `kubectl describe po moscow-time-pre-install`

```bash
ebob@laptop ~ % kubectl describe po moscow-time-pre-install
Name:             moscow-time-pre-install
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sun, 23 Feb 2025 18:16:54 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
                  helm.sh/hook-weight: -5
Status:           Succeeded
IP:               10.244.0.18
IPs:
  IP:  10.244.0.18
Containers:
  pre-install-job:
    Container ID:  docker://a9eb3677f57c50a03d5a4878da65dcf345cc382460e9e0a62d5abd44f837765e
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo "Starting pre-install hook"; sleep 20; echo "Pre-install hook completed"
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Sun, 23 Feb 2025 18:16:59 +0300
      Finished:     Sun, 23 Feb 2025 18:17:19 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-5vjhm (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False
  Initialized                 True
  Ready                       False
  ContainersReady             False
  PodScheduled                True
Volumes:
  kube-api-access-5vjhm:
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
  Normal  Scheduled  5m6s  default-scheduler  Successfully assigned default/moscow-time-pre-install to minikube
  Normal  Pulling    5m6s  kubelet            Pulling image "busybox"
  Normal  Pulled     5m1s  kubelet            Successfully pulled image "busybox" in 4.799s (4.799s including waiting). Image size: 4042190 bytes.
  Normal  Created    5m1s  kubelet            Created container: pre-install-job
  Normal  Started    5m1s  kubelet            Started container pre-install-job
```

### `kubectl describe po moscow-time-post-install`

```bash
ebob@laptop ~ % kubectl describe po moscow-time-post-install
Name:             moscow-time-post-install
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sun, 23 Feb 2025 18:17:21 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
                  helm.sh/hook-weight: 5
Status:           Succeeded
IP:               10.244.0.22
IPs:
  IP:  10.244.0.22
Containers:
  post-install-job:
    Container ID:  docker://5a02bdf5adb5d33e4e4f2baea2ea8444cbc0f704ec58162eef23e0cc5874aa45
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo "Starting post-install hook"; sleep 20; echo "Post-install hook completed"
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Sun, 23 Feb 2025 18:17:24 +0300
      Finished:     Sun, 23 Feb 2025 18:17:44 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-jgt76 (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False
  Initialized                 True
  Ready                       False
  ContainersReady             False
  PodScheduled                True
Volumes:
  kube-api-access-jgt76:
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
  Normal  Scheduled  5m26s  default-scheduler  Successfully assigned default/moscow-time-post-install to minikube
  Normal  Pulling    5m25s  kubelet            Pulling image "busybox"
  Normal  Pulled     5m23s  kubelet            Successfully pulled image "busybox" in 1.49s (1.49s including waiting). Image size: 4042190 bytes.
  Normal  Created    5m23s  kubelet            Created container: post-install-job
  Normal  Started    5m23s  kubelet            Started container post-install-job
```

`kubectl get pods`

```bash
kubectl get pods
NAME                           READY   STATUS      RESTARTS   AGE
moscow-time-7bcf4d744f-fhbmt   1/1     Running     0          46h
moscow-time-7bcf4d744f-j7hqx   1/1     Running     0          46h
moscow-time-7bcf4d744f-lmzxq   1/1     Running     0          46h
moscow-time-post-install       0/1     Completed   0          46h
moscow-time-pre-install        0/1     Completed   0          46h
```

### Hook Delete Policy

Add this to `hook.yaml`:

```bash
"helm.sh/hook-delete-policy": hook-succeeded
```

## Helm Library Chart

Create lib directory:

```bash
helm create common-lib
```

```bash
cd moscow-time
helm dependency build
```

```bash
helm install moscow-time . --set labels.environment=production
```

Deploy second app:

```bash
kubectl get pods
NAME                           READY   STATUS    RESTARTS   AGE
moscow-time-74498bff5b-6ctjb   1/1     Running   0          108s
moscow-time-74498bff5b-jrgz6   1/1     Running   0          108s
moscow-time-74498bff5b-wdg6s   1/1     Running   0          108s
omsk-time-9474b67c6-qjpns      1/1     Running   0          3m14s
omsk-time-9474b67c6-rnw5s      1/1     Running   0          3m14s
omsk-time-9474b67c6-vnjp8      1/1     Running   0          3m14s

kubectl get deployment moscow-time -o yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  annotations:
    deployment.kubernetes.io/revision: "1"
    meta.helm.sh/release-name: moscow-time
    meta.helm.sh/release-namespace: default
  creationTimestamp: "2025-02-25T14:41:49Z"
  generation: 1
  labels:
    app.kubernetes.io/instance: moscow-time
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/name: moscow-time
    app.kubernetes.io/version: "1.1"
    helm.sh/chart: moscow-time-0.1.0
  name: moscow-time
  namespace: default
  resourceVersion: "112911"
  uid: 8f4e3b68-224b-4d38-81eb-400a6c9bf8d9
spec:
  progressDeadlineSeconds: 600
  replicas: 3
  revisionHistoryLimit: 10
  selector:
    matchLabels:
      app.kubernetes.io/instance: moscow-time
      app.kubernetes.io/name: moscow-time
  strategy:
    rollingUpdate:
      maxSurge: 25%
      maxUnavailable: 25%
    type: RollingUpdate
  template:
    metadata:
      creationTimestamp: null
      labels:
        app.kubernetes.io/instance: moscow-time
        app.kubernetes.io/name: moscow-time
    spec:
      containers:
      - image: ebob/moscow-time:v1.1
        imagePullPolicy: IfNotPresent
        name: moscow-time
        ports:
        - containerPort: 80
          name: http
          protocol: TCP
        resources: {}
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
      dnsPolicy: ClusterFirst
      restartPolicy: Always
      schedulerName: default-scheduler
      securityContext: {}
      terminationGracePeriodSeconds: 30
status:
  availableReplicas: 3
  conditions:
  - lastTransitionTime: "2025-02-25T14:41:52Z"
    lastUpdateTime: "2025-02-25T14:41:52Z"
    message: Deployment has minimum availability.
    reason: MinimumReplicasAvailable
    status: "True"
    type: Available
  - lastTransitionTime: "2025-02-25T14:41:49Z"
    lastUpdateTime: "2025-02-25T14:41:52Z"
    message: ReplicaSet "moscow-time-74498bff5b" has successfully progressed.
    reason: NewReplicaSetAvailable
    status: "True"
    type: Progressing
  observedGeneration: 1
  readyReplicas: 3
  replicas: 3
  updatedReplicas: 3
```
