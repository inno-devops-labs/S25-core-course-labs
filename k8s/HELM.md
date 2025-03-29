# Helm

### Create namespace
At first, I created namespace, where I will deploy my chart.
```bash
(venv) ➜  k8s git:(lab-10) ✗ k create namespace lab-10
namespace/lab-10 created
```

### Install chart
Then I installed chart using `helm install`
```bash
(venv) ➜  k8s git:(lab-10) ✗ helm install py-app py-app -n lab-10
NAME: py-app
LAST DEPLOYED: Mon Feb 24 22:29:47 2025
NAMESPACE: lab-10
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
export POD_NAME=$(kubectl get pods --namespace lab-10 -l "app.kubernetes.io/name=py-app,app.kubernetes.io/instance=py-app" -o jsonpath="{.items[0].metadata.name}")
export CONTAINER_PORT=$(kubectl get pod --namespace lab-10 $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
echo "Visit http://127.0.0.1:8080 to use your application"
kubectl --namespace lab-10 port-forward $POD_NAME 8080:$CONTAINER_PORT
```

### Access application
Then using provided instructions from helm for port-forwarding, we can get reach our app:
```bash
(venv) ➜  k8s git:(lab-10) ✗ 
export POD_NAME=$(kubectl get pods --namespace lab-10 -l "app.kubernetes.io/name=py-app,app.kubernetes.io/instance=py-app" -o jsonpath="{.items[0].metadata.name}")
export CONTAINER_PORT=$(kubectl get pod --namespace lab-10 $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
echo "Visit http://127.0.0.1:8080 to use your application"
kubectl --namespace lab-10 port-forward $POD_NAME 8080:$CONTAINER_PORT

Visit http://127.0.0.1:8080 to use your application
Forwarding from 127.0.0.1:8080 -> 8000
Forwarding from [::1]:8080 -> 8000
```

```bash
➜  ~ curl http://localhost:8000/time
{"time":"2025-02-24T22:35:16.586690+03:00"}%
```

### Pods and services
List of pods and services
```bash
(venv) ➜  k8s git:(lab-10) ✗ k get pods,svc -n lab-10
NAME                         READY   STATUS    RESTARTS   AGE
pod/py-app-6df7b8846-wpdz7   1/1     Running   0          6m4s

NAME             TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)    AGE
service/py-app   ClusterIP   10.96.110.3   <none>        8000/TCP   6m4s
```


## Hooks
Lint gives:
```bash
(venv) ➜  k8s git:(lab-10) ✗ helm lint py-app -n lab-10
==> Linting py-app
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed
```

Install with dry-run:
```bash
(venv) ➜  k8s git:(lab-10) ✗ helm install --dry-run helm-hooks py-app -n lab-10
NAME: helm-hooks
LAST DEPLOYED: Mon Feb 24 22:38:33 2025
NAMESPACE: lab-10
STATUS: pending-install
REVISION: 1
HOOKS:
---
# Source: py-app/templates/post-install-hook.yaml
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
# Source: py-app/templates/pre-install-hook.yaml
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
# Source: py-app/templates/tests/test-connection.yaml
apiVersion: v1
kind: Pod
metadata:
  name: "helm-hooks-py-app-test-connection"
  labels:
    helm.sh/chart: py-app-0.1.0
    app.kubernetes.io/name: py-app
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
      args: ['helm-hooks-py-app:8000']
  restartPolicy: Never
MANIFEST:
---
# Source: py-app/templates/serviceaccount.yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: helm-hooks-py-app
  labels:
    helm.sh/chart: py-app-0.1.0
    app.kubernetes.io/name: py-app
    app.kubernetes.io/instance: helm-hooks
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
automountServiceAccountToken: true
---
# Source: py-app/templates/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: helm-hooks-py-app
  labels:
    helm.sh/chart: py-app-0.1.0
    app.kubernetes.io/name: py-app
    app.kubernetes.io/instance: helm-hooks
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
spec:
  type: ClusterIP
  ports:
    - port: 8000
      targetPort: http
      protocol: TCP
      name: http
  selector:
    app.kubernetes.io/name: py-app
    app.kubernetes.io/instance: helm-hooks
---
# Source: py-app/templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: helm-hooks-py-app
  labels:
    helm.sh/chart: py-app-0.1.0
    app.kubernetes.io/name: py-app
    app.kubernetes.io/instance: helm-hooks
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
spec:
  replicas: 1
  selector:
    matchLabels:
      app.kubernetes.io/name: py-app
      app.kubernetes.io/instance: helm-hooks
  template:
    metadata:
      labels:
        helm.sh/chart: py-app-0.1.0
        app.kubernetes.io/name: py-app
        app.kubernetes.io/instance: helm-hooks
        app.kubernetes.io/version: "1.16.0"
        app.kubernetes.io/managed-by: Helm
    spec:
      serviceAccountName: helm-hooks-py-app
      securityContext:
        {}
      containers:
        - name: py-app
          securityContext:
            {}
          image: "wensiet/devops-py-app:release"
          imagePullPolicy: IfNotPresent
          ports:
            - name: http
              containerPort: 8000
              protocol: TCP
          livenessProbe:
            null
          readinessProbe:
            null
          resources:
            limits:
              cpu: 100m
              memory: 128Mi
            requests:
              cpu: 100m
              memory: 128Mi

NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace lab-10 -l "app.kubernetes.io/name=py-app,app.kubernetes.io/instance=helm-hooks" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace lab-10 $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace lab-10 port-forward $POD_NAME 8080:$CONTAINER_PORT
```

To get working hooks we need to install chart without `--dry-run` flag, after executing command we get:

```bash
(venv) ➜  k8s git:(lab-10) ✗ k get po -n lab-10 
NAME                                 READY   STATUS      RESTARTS   AGE
helm-hooks-py-app-688575dcfd-lkkqh   1/1     Running     0          2m24s
postinstall-hook                     0/1     Completed   0          2m24s
preinstall-hook                      0/1     Completed   0          2m46s
```

Description for pre-install hook

```bash
(venv) ➜  k8s git:(lab-10) ✗ kubectl describe po preinstall-hook -n lab-10
Name:             preinstall-hook
Namespace:        lab-10
Priority:         0
Service Account:  default
Node:             devops-lab-9-control-plane/172.21.0.2
Start Time:       Mon, 24 Feb 2025 22:41:17 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.23
IPs:
  IP:  10.244.0.23
Containers:
  pre-install-container:
    Container ID:  containerd://b2e72c03448ed74d3a592e73699df19188f0f18f43a11e731237ff1ddfe6c58a
    Image:         busybox
    Image ID:      docker.io/library/busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The pre-install hook is running && sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Mon, 24 Feb 2025 22:41:18 +0300
      Finished:     Mon, 24 Feb 2025 22:41:38 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-m22tl (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-m22tl:
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
  Normal  Scheduled  4m20s  default-scheduler  Successfully assigned lab-10/preinstall-hook to devops-lab-9-control-plane
  Normal  Pulled     4m19s  kubelet            Container image "busybox" already present on machine
  Normal  Created    4m19s  kubelet            Created container pre-install-container
  Normal  Started    4m19s  kubelet            Started container pre-install-container
```

Description for post-install hook

```bash
(venv) ➜  k8s git:(lab-10) ✗ kubectl describe po postinstall-hook -n lab-10 
Name:             postinstall-hook
Namespace:        lab-10
Priority:         0
Service Account:  default
Node:             devops-lab-9-control-plane/172.21.0.2
Start Time:       Mon, 24 Feb 2025 22:41:39 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.25
IPs:
  IP:  10.244.0.25
Containers:
  post-install-container:
    Container ID:  containerd://e5dc3a0b0b73eb3d9923b214041c748584ea9b429e9554e08b210e2c4eae227f
    Image:         busybox
    Image ID:      docker.io/library/busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The post-install hook is running && sleep 15
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Mon, 24 Feb 2025 22:41:43 +0300
      Finished:     Mon, 24 Feb 2025 22:41:58 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-w8lwz (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-w8lwz:
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
  Normal  Scheduled  2m56s  default-scheduler  Successfully assigned lab-10/postinstall-hook to devops-lab-9-control-plane
  Normal  Pulling    2m55s  kubelet            Pulling image "busybox"
  Normal  Pulled     2m52s  kubelet            Successfully pulled image "busybox" in 2.896s (2.896s including waiting). Image size: 1855648 bytes.
  Normal  Created    2m52s  kubelet            Created container post-install-container
  Normal  Started    2m52s  kubelet            Started container post-install-container
```

Explanation: actually, there is just basic info about k8s pod resource, there is info
about the node, where the pod was scheduled, it age, container, image tag, lifetime and
also events, which k8s proceeded to launch it.

## Deletion policy
For deletion policy, there is just annotation `hook-delete-policy`:

```yaml
"helm.sh/hook-delete-policy": "before-hook-creation,hook-succeeded"
```

After applying it we see that hook's pods are deleted:

```bash
(venv) ➜  k8s git:(lab-10) ✗ helm install helm-hooks py-app -n lab-10
NAME: helm-hooks
LAST DEPLOYED: Mon Feb 24 22:51:25 2025
NAMESPACE: lab-10
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace lab-10 -l "app.kubernetes.io/name=py-app,app.kubernetes.io/instance=helm-hooks" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace lab-10 $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace lab-10 port-forward $POD_NAME 8080:$CONTAINER_PORT
(venv) ➜  k8s git:(lab-10) ✗ k get po -n lab-10 
NAME                                 READY   STATUS    RESTARTS   AGE
helm-hooks-py-app-688575dcfd-qgdrb   1/1     Running   0          24s
```