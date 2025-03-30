# Helm

## Task 1

### Output of `kubectl get pods,svc` command:
```
NAME                      READY   STATUS             RESTARTS      AGE
pod/app-9b5c6fd7d-6mctk   0/1     CrashLoopBackOff   6 (56s ago)   15m

NAME                 TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)   AGE
service/app          ClusterIP   10.99.83.94   <none>        80/TCP    15m
service/kubernetes   ClusterIP   10.96.0.1     <none>        443/TCP   140m
```

## Task 2

### helm lint app
```bash
==> Linting app
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed
```

### helm install --dry-run helm-hooks ./app 

```bash
NAME: helm-hooks
LAST DEPLOYED: Sun Mar 30 13:28:07 2025
NAMESPACE: default
STATUS: pending-install
REVISION: 1
HOOKS:
---
# Source: app/templates/post-install-hook.yaml
apiVersion: v1  # Changed from batch/v1
kind: Pod
metadata:
  name: "post-install"
  annotations:
    "helm.sh/hook": post-install
    # "helm.sh/hook-delete-policy": hook-succeeded
spec:
  containers:
  - name: post-install
    image: busybox
    command: ["/bin/sh", "-c", "echo 'Running post-install hook'; sleep 20"]
  restartPolicy: Never
---
# Source: app/templates/pre-install-hook.yaml
apiVersion: v1  # Changed from batch/v1
kind: Pod
metadata:
  name: "pre-install"
  annotations:
    "helm.sh/hook": pre-install
    # "helm.sh/hook-delete-policy": hook-succeeded
spec:
  containers:
  - name: pre-install
    image: busybox
    command: ["/bin/sh", "-c", "echo 'Running pre-install hook'; sleep 20"]
  restartPolicy: Never
---
# Source: app/templates/tests/test-connection.yaml
apiVersion: v1
kind: Pod
metadata:
  name: "helm-hooks-app-test-connection"
  labels:
    helm.sh/chart: app-0.1.0
    app.kubernetes.io/name: app
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
      args: ['helm-hooks-app:80']
  restartPolicy: Never
MANIFEST:
---
# Source: app/templates/serviceaccount.yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: helm-hooks-app
  labels:
    helm.sh/chart: app-0.1.0
    app.kubernetes.io/name: app
    app.kubernetes.io/instance: helm-hooks
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
automountServiceAccountToken: true
---
# Source: app/templates/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: helm-hooks-app
  labels:
    helm.sh/chart: app-0.1.0
    app.kubernetes.io/name: app
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
    app.kubernetes.io/name: app
    app.kubernetes.io/instance: helm-hooks
---
# Source: app/templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: helm-hooks-app
  labels:
    helm.sh/chart: app-0.1.0
    app.kubernetes.io/name: app
    app.kubernetes.io/instance: helm-hooks
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
spec:
  replicas: 1
  selector:
    matchLabels:
      app.kubernetes.io/name: app
      app.kubernetes.io/instance: helm-hooks
  template:
    metadata:
      labels:
        helm.sh/chart: app-0.1.0
        app.kubernetes.io/name: app
        app.kubernetes.io/instance: helm-hooks
        app.kubernetes.io/version: "1.16.0"
        app.kubernetes.io/managed-by: Helm
    spec:
      serviceAccountName: helm-hooks-app
      containers:
        - name: app
          image: "denisnesterov/app:latest"
          imagePullPolicy: IfNotPresent
          ports:
            - name: http
              containerPort: 8000
              protocol: TCP
          livenessProbe:
            httpGet:
              path: /
              port: http
          readinessProbe:
            httpGet:
              path: /
              port: http

NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=app,app.kubernetes.io/instance=helm-hooks" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
```

### helm install helm-hooks ./app  
```bash
NAME: helm-hooks
LAST DEPLOYED: Sun Mar 30 13:28:17 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=app,app.kubernetes.io/instance=helm-hooks" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
```


### kubectl get po
```bash
NAME                              READY   STATUS      RESTARTS       AGE
app-9c45788fd-568d7               1/1     Running     2 (6d4h ago)   14d
helm-hooks-app-685ff5fbb8-d2z2g   1/1     Running     0              77s
post-install                      0/1     Completed   0              77s
pre-install                       0/1     Completed   0              102s
python-app-57cc6ddb99-222vj       1/1     Running     1 (6d4h ago)   7d19h
python-app-57cc6ddb99-7g7xv       1/1     Running     1 (6d4h ago)   7d19h
python-app-57cc6ddb99-sgms8       1/1     Running     1 (6d4h ago)   7d20h
```

### kubectl describe po pre-install

```bash
Name:             pre-install
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sun, 30 Mar 2025 13:28:17 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.66
IPs:
  IP:  10.244.0.66
Containers:
  pre-install:
    Container ID:  docker://2aa08899f7c96b2bd527acda74e84a9743e6eee04004f447c03a854e3c62e7dd
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:37f7b378a29ceb4c551b1b5582e27747b855bbfaa73fa11914fe0df028dc581f
    Port:          <none>
    Host Port:     <none>
    Command:
      /bin/sh
      -c
      echo 'Running pre-install hook'; sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Sun, 30 Mar 2025 13:28:19 +0300
      Finished:     Sun, 30 Mar 2025 13:28:40 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-rbtdt (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-rbtdt:
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
  Normal  Scheduled  3m26s  default-scheduler  Successfully assigned default/pre-install to minikube
  Normal  Pulling    3m26s  kubelet            Pulling image "busybox"
  Normal  Pulled     3m24s  kubelet            Successfully pulled image "busybox" in 2.31s (2.31s including waiting). Image size: 4042190 bytes.
  Normal  Created    3m24s  kubelet            Created container: pre-install
  Normal  Started    3m23s  kubelet            Started container pre-install
```

### kubectl describe po post-install
```bash
Name:             post-install
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sun, 30 Mar 2025 13:28:42 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.68
IPs:
  IP:  10.244.0.68
Containers:
  post-install:
    Container ID:  docker://e099271ab4af1700270cc88096a6a85058f7f249c6b53f20d23a11d67dd85090
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:37f7b378a29ceb4c551b1b5582e27747b855bbfaa73fa11914fe0df028dc581f
    Port:          <none>
    Host Port:     <none>
    Command:
      /bin/sh
      -c
      echo 'Running post-install hook'; sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Sun, 30 Mar 2025 13:28:44 +0300
      Finished:     Sun, 30 Mar 2025 13:29:04 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-wlkqh (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-wlkqh:
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
  Normal  Scheduled  3m58s  default-scheduler  Successfully assigned default/post-install to minikube
  Normal  Pulling    3m58s  kubelet            Pulling image "busybox"
  Normal  Pulled     3m56s  kubelet            Successfully pulled image "busybox" in 1.778s (1.778s including waiting). Image size: 4042190 bytes.
  Normal  Created    3m56s  kubelet            Created container: post-install
  Normal  Started    3m56s  kubelet            Started container post-install
```

### To implement a hook delete policy i added this line
```yaml
"helm.sh/hook-delete-policy": hook-succeeded
```
