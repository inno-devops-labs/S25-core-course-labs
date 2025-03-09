![image](https://github.com/user-attachments/assets/d0d0ad0f-5784-45c9-be8b-a9f49008c202)


```
meowal@meowal-1-2:~/S25-core-course-labs/k8s$ minikube service  my-release-time-app
|-----------|---------------------|-------------|--------------|
| NAMESPACE |        NAME         | TARGET PORT |     URL      |
|-----------|---------------------|-------------|--------------|
| default   | my-release-time-app |             | No node port |
|-----------|---------------------|-------------|--------------|
😿  service default/my-release-time-app has no node port
❗  Services [default/my-release-time-app] have type "ClusterIP" not meant to be exposed, however for local development minikube allows you to access this !
🏃  Starting tunnel for service my-release-time-app.
|-----------|---------------------|-------------|------------------------|
| NAMESPACE |        NAME         | TARGET PORT |          URL           |
|-----------|---------------------|-------------|------------------------|
| default   | my-release-time-app |             | http://127.0.0.1:33389 |
|-----------|---------------------|-------------|------------------------|
🎉  Opening service default/my-release-time-app in default browser...
❗  Because you are using a Docker driver on linux, the terminal needs to be open to run it.
Gtk-Message: 01:58:03.957: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.

meowal@meowal-1-2:~/S25-core-course-labs/k8s$ kubectl get pods,svc
NAME                                       READY   STATUS    RESTARTS   AGE
pod/msk-time-deployment-fb64c7cfc-5csfj    1/1     Running   0          65m
pod/msk-time-deployment-fb64c7cfc-7m4pm    1/1     Running   0          65m
pod/msk-time-deployment-fb64c7cfc-wltfr    1/1     Running   0          65m
pod/my-release-time-app-56fbb7fd74-d2k9z   1/1     Running   0          26m

NAME                          TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/kubernetes            ClusterIP   10.96.0.1        <none>        443/TCP          72m
service/msk-time-service      NodePort    10.105.160.200   <none>        5000:30920/TCP   65m
service/my-release-time-app   ClusterIP   10.98.55.138     <none>        80/TCP           26m
meowal@meowal-1-2:~/S25-core-course-labs/k8s$ 


TASK 2

meowal@meowal-1-2:~/S25-core-course-labs/k8s$ helm lint time-app
==> Linting time-app
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed

meowal@meowal-1-2:~/S25-core-course-labs/k8s$ helm install --dry-run helm-hooks ./time-app
NAME: helm-hooks
LAST DEPLOYED: Thu Feb 27 02:05:00 2025
NAMESPACE: default
STATUS: pending-install
REVISION: 1
HOOKS:
---
# Source: time-app/templates/tests/test-connection.yaml
apiVersion: v1
kind: Pod
metadata:
  name: "helm-hooks-time-app-test-connection"
  labels:
    helm.sh/chart: time-app-0.1.0
    app.kubernetes.io/name: time-app
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
      args: ['helm-hooks-time-app:80']
  restartPolicy: Never
---
# Source: time-app/templates/hooks.yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: "helm-hooks-time-app-preinstall"
  annotations:
    "helm.sh/hook": pre-install
    "helm.sh/hook-delete-policy": hook-succeeded
spec:
  template:
    spec:
      containers:
      - name: preinstall
        image: busybox
        command: ["sh", "-c", "echo Pre-install hook: sleeping for 20 seconds && sleep 20"]
      restartPolicy: Never
MANIFEST:
---
# Source: time-app/templates/serviceaccount.yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: helm-hooks-time-app
  labels:
    helm.sh/chart: time-app-0.1.0
    app.kubernetes.io/name: time-app
    app.kubernetes.io/instance: helm-hooks
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
automountServiceAccountToken: true
---
# Source: time-app/templates/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: helm-hooks-time-app
  labels:
    helm.sh/chart: time-app-0.1.0
    app.kubernetes.io/name: time-app
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
    app.kubernetes.io/name: time-app
    app.kubernetes.io/instance: helm-hooks
---
# Source: time-app/templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: helm-hooks-time-app
  labels:
    helm.sh/chart: time-app-0.1.0
    app.kubernetes.io/name: time-app
    app.kubernetes.io/instance: helm-hooks
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
spec:
  replicas: 1
  selector:
    matchLabels:
      app.kubernetes.io/name: time-app
      app.kubernetes.io/instance: helm-hooks
  template:
    metadata:
      labels:
        helm.sh/chart: time-app-0.1.0
        app.kubernetes.io/name: time-app
        app.kubernetes.io/instance: helm-hooks
        app.kubernetes.io/version: "1.16.0"
        app.kubernetes.io/managed-by: Helm
    spec:
      serviceAccountName: helm-hooks-time-app
      containers:
        - name: time-app
          image: "meowal/msk-time-app:latest"
          imagePullPolicy: IfNotPresent
          ports:
            - name: http
              containerPort: 5000
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
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=time-app,app.kubernetes.io/instance=helm-hooks" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT



meowal@meowal-1-2:~/S25-core-course-labs/k8s$ kubectl get po
NAME                                   READY   STATUS    RESTARTS   AGE
msk-time-deployment-fb64c7cfc-5csfj    1/1     Running   0          70m
msk-time-deployment-fb64c7cfc-7m4pm    1/1     Running   0          70m
msk-time-deployment-fb64c7cfc-wltfr    1/1     Running   0          70m
my-release-time-app-56fbb7fd74-d2k9z   1/1     Running   0          30m
meowal@meowal-1-2:~/S25-core-course-labs/k8s$ 


meowal@meowal-1-2:~/S25-core-course-labs/k8s$ kubectl describe po my-release-time-app-56fbb7fd74-d2k9z
Name:             my-release-time-app-56fbb7fd74-d2k9z
Namespace:        default
Priority:         0
Service Account:  my-release-time-app
Node:             minikube/192.168.49.2
Start Time:       Thu, 27 Feb 2025 01:34:23 +0300
Labels:           app.kubernetes.io/instance=my-release
                  app.kubernetes.io/managed-by=Helm
                  app.kubernetes.io/name=time-app
                  app.kubernetes.io/version=1.16.0
                  helm.sh/chart=time-app-0.1.0
                  pod-template-hash=56fbb7fd74
Annotations:      <none>
Status:           Running
IP:               10.244.0.41
IPs:
  IP:           10.244.0.41
Controlled By:  ReplicaSet/my-release-time-app-56fbb7fd74
Containers:
  time-app:
    Container ID:   docker://40ffb11cecba4d2361c4ef9497083ea9bb08a7d0f2dd4f50e5cf6f2839495247
    Image:          meowal/msk-time-app:latest
    Image ID:       docker-pullable://meowal/msk-time-app@sha256:abd6b4c9eb8be1eac78e25164f4e462c99b933f9e99f29950639640b55ac72d1
    Port:           5000/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Thu, 27 Feb 2025 01:34:25 +0300
    Ready:          True
    Restart Count:  0
    Liveness:       http-get http://:http/ delay=0s timeout=1s period=10s #success=1 #failure=3
    Readiness:      http-get http://:http/ delay=0s timeout=1s period=10s #success=1 #failure=3
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-4tkr5 (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       True 
  ContainersReady             True 
  PodScheduled                True 
Volumes:
  kube-api-access-4tkr5:
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
  Type     Reason     Age                From               Message
  ----     ------     ----               ----               -------
  Normal   Scheduled  33m                default-scheduler  Successfully assigned default/my-release-time-app-56fbb7fd74-d2k9z to minikube
  Normal   Pulled     33m                kubelet            Container image "meowal/msk-time-app:latest" already present on machine
  Normal   Created    33m                kubelet            Created container: time-app
  Normal   Started    33m                kubelet            Started container time-app
  Warning  Unhealthy  33m (x2 over 33m)  kubelet            Readiness probe failed: Get "http://10.244.0.41:5000/": dial tcp 10.244.0.41:5000: connect: connection refused
meowal@meowal-1-2:~/S25-core-course-labs/k8s$ 


```


