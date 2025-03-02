# Helm

## Task 1

### 1. Create an application for the first time
```bash
helm create python-app
```

### 2. Update the generated file `python-app/values.yaml`:
```bash
image:
  repository: dew1769/application-real-time
  tag: latest

service:
  port: 5000
```

### 3. Run the `helm install`:
```bash
PS C:\Users\S25-core-course-labs\k8s> helm install python-app ./python-app
NAME: python-app
LAST DEPLOYED: Sun Mar  2 23:25:14 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=python-app,app.kubernetes.io/instance=python-app" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
```

### 5. Check the minikube dashboard:
```bash
PS C:\Users\S25-core-course-labs\k8s> minikube dashboard
🔌  Enabling dashboard ...
    ▪ Using image docker.io/kubernetesui/dashboard:v2.7.0
    ▪ Using image docker.io/kubernetesui/metrics-scraper:v1.0.8
💡  Some dashboard features require the metrics-server addon. To enable all features please run:

        minikube addons enable metrics-server

🤔  Verifying dashboard health ...
🚀  Launching proxy ...
🤔  Verifying proxy health ...
🎉  Opening http://127.0.0.1:54908/api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard:/proxy/ in your default browser...
```

The screenshot of openned dashboard:

![Dash](img/dashboard.png)

`minikube service python-app`:
```bash
🏃  Starting tunnel for service python-app.
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | python-app |             | http://127.0.0.1:55112 |
|-----------|------------|-------------|------------------------|
🎉  Opening service default/python-app in default browser...
❗  Because you are using a Docker driver on windows, the terminal needs to be open to run it.
```
The page with app has opened

### 6. Get pods, svc:
```bash
PS C:\Users\S25-core-course-labs\k8s> kubectl get pods,svc
NAME                             READY   STATUS    RESTARTS   AGE
pod/python-app-c8445db89-xg7vs   1/1     Running   0          5m11s

NAME                 TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
service/kubernetes   ClusterIP   10.96.0.1        <none>        443/TCP    38m
service/python-app   ClusterIP   10.100.109.232   <none>        5000/TCP   12m
```

## Task 2

### 1. Validate helm chart
```bash
PS C:\Users\S25-core-course-labs\k8s> helm lint python-app
==> Linting python-app
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed
```

### 2. In the `python-app/templates/` I've added 2 files (`pre-install.yaml` and `post-install.yaml`). To make sure they are correct we will run the following command:
```bash
PS C:\Users\S25-core-course-labs\k8s> helm install --dry-run helm-hooks python-app
NAME: helm-hooks
LAST DEPLOYED: Sun Mar  2 23:41:36 2025
NAMESPACE: default
STATUS: pending-install
REVISION: 1
HOOKS:
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
      args: ['helm-hooks-python-app:5000']
  restartPolicy: Never
---
# Source: python-app/templates/hooks/post-install.yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: post-install-job
  annotations:
    "helm.sh/hook": post-install
    "helm.sh/hook-weight": "5"
    "helm.sh/hook-delete-policy": hook-succeeded
spec:
  template:
    spec:
      containers:
        - name: post-install
          image: busybox
          command: ["sh", "-c", "echo Post-Install Hook Running; sleep 20"]
      restartPolicy: Never
---
# Source: python-app/templates/hooks/pre-install.yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: pre-install-job
  annotations:
    "helm.sh/hook": pre-install
    "helm.sh/hook-weight": "-5"
    "helm.sh/hook-delete-policy": hook-succeeded
spec:
  template:
    spec:
      containers:
        - name: pre-install
          image: busybox
          command: ["sh", "-c", "echo Pre-Install Hook Running; sleep 20"]
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
    - port: 5000
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
  replicas: 1
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
          image: "dew1769/application-real-time:latest"
          imagePullPolicy:
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
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=python-app,app.kubernetes.io/instance=helm-hooks" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
```

### 3. After reinstalling the helm chart verify that hooks running:
```bash
PS C:\Users\S25-core-course-labs\k8s> kubectl get pods
NAME                         READY   STATUS              RESTARTS   AGE
post-install-job-bjslj       0/1     ContainerCreating   0          4s
pre-install-job-zkpn8        0/1     ContainerCreating   0          4s
python-app-c8445db89-snwsg   1/1     Running             0          55s
python-app-test-connection   0/1     Completed           0          4s
```

### 4. Hooks description:
```bash
PS C:\Users\S25-core-course-labs\k8s> kubectl describe po pre-install-job-zkpn8
Name:             pre-install-job-zkpn8
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sun, 02 Mar 2025 23:54:13 +0300
Labels:           batch.kubernetes.io/controller-uid=59e556d5-f81e-49df-a93e-b46db7890645
                  batch.kubernetes.io/job-name=pre-install-job
                  controller-uid=59e556d5-f81e-49df-a93e-b46db7890645
                  job-name=pre-install-job
Annotations:      <none>
Status:           Succeeded
IP:               10.244.0.33
IPs:
  IP:           10.244.0.33
Controlled By:  Job/pre-install-job
Containers:
  pre-install:
    Container ID:  docker://309ef7eb2983bf8377622dc2e1367540bf703255f727463b0747ccd50849e8bd
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo Pre-Install Hook Running; sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Sun, 02 Mar 2025 23:54:19 +0300
      Finished:     Sun, 02 Mar 2025 23:54:39 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-lfrr7 (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False
  Initialized                 True
  Ready                       False
  ContainersReady             False
  PodScheduled                True
Volumes:
  kube-api-access-lfrr7:
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
  Normal  Scheduled  75s   default-scheduler  Successfully assigned default/pre-install-job-zkpn8 to minikube
  Normal  Pulling    75s   kubelet            Pulling image "busybox"
  Normal  Pulled     69s   kubelet            Successfully pulled image "busybox" in 1.74s (5.528s including waiting). Image size: 4269694 bytes.
  Normal  Created    69s   kubelet            Created container: pre-install
  Normal  Started    69s   kubelet            Started container pre-install
PS C:\Users\S25-core-course-labs\k8s> kubectl describe po post-install-job-bjslj
Name:             post-install-job-bjslj
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sun, 02 Mar 2025 23:54:13 +0300
Labels:           batch.kubernetes.io/controller-uid=2f15bfff-4977-424b-800b-bd4044f22a61
                  batch.kubernetes.io/job-name=post-install-job
                  controller-uid=2f15bfff-4977-424b-800b-bd4044f22a61
                  job-name=post-install-job
Annotations:      <none>
Status:           Succeeded
IP:               10.244.0.32
IPs:
  IP:           10.244.0.32
Controlled By:  Job/post-install-job
Containers:
  post-install:
    Container ID:  docker://57d3bcd115a5a93ba0255264adf043748cd21d8d5bf8f4f3020d4e4553d28336
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo Post-Install Hook Running; sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Sun, 02 Mar 2025 23:54:17 +0300
      Finished:     Sun, 02 Mar 2025 23:54:37 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-7xg4b (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False
  Initialized                 True
  Ready                       False
  ContainersReady             False
  PodScheduled                True
Volumes:
  kube-api-access-7xg4b:
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
  Normal  Scheduled  108s  default-scheduler  Successfully assigned default/post-install-job-bjslj to minikube
  Normal  Pulling    108s  kubelet            Pulling image "busybox"
  Normal  Pulled     104s  kubelet            Successfully pulled image "busybox" in 1.729s (3.799s including waiting). Image size: 4269694 bytes.
  Normal  Created    104s  kubelet            Created container: post-install
  Normal  Started    104s  kubelet            Started container post-install
```

### 5. Delete policy:
In the files we can see the line: `"helm.sh/hook-delete-policy": hook-succeeded`.

So, we wont see the hooks:
```bash
PS C:\Users\S25-core-course-labs\k8s> kubectl get pods
NAME                         READY   STATUS    RESTARTS   AGE
python-app-c8445db89-8v2pq   1/1     Running   0          47s
```