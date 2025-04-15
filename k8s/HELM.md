# Lab 10: Introduction to Helm
## Task 1: Helm Setup and Chart Creation
```txt
fridorovich@DESKTOP-FRR2QTC:/home/devops/S25-core-course-labs/k8s$ helm install python-web ./python-web
NAME: python-web
LAST DEPLOYED: Wed Apr 16 02:15:03 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=python-web,app.kubernetes.io/instance=python-web" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
```
```txt
fridorovich@DESKTOP-FRR2QTC:/home/devops/S25-core-course-labs/k8s$ kubectl get po,svc
NAME                             READY   STATUS    RESTARTS   AGE
pod/python-web-856974874-bcwbc   1/1     Running   0          56s
pod/python-web-856974874-fgcc5   1/1     Running   0          56s
pod/python-web-856974874-l25gc   1/1     Running   0          56s

NAME                 TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE
service/kubernetes   ClusterIP   10.96.0.1      <none>        443/TCP    101s
service/python-web   ClusterIP   10.97.63.173   <none>        8000/TCP   56s
```
```txt
fridorovich@DESKTOP-FRR2QTC:/home/devops/S25-core-course-labs/k8s$ minikube service python-web
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | python-web |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/python-web has no node port
❗  Services [default/python-web] have type "ClusterIP" not meant to be exposed, however for local development minikube allows you to access this !
🏃  Starting tunnel for service python-web.
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | python-web |             | http://127.0.0.1:37987 |
|-----------|------------|-------------|------------------------|
🎉  Opening service default/python-web in default browser...
👉  http://127.0.0.1:37987
❗  Because you are using a Docker driver on linux, the terminal needs to be open to run it.
```

## Task 2: Helm Chart Hooks
```txt
fridorovich@DESKTOP-FRR2QTC:/home/devops/S25-core-course-labs/k8s$ helm lint python-web
==> Linting python-web
[INFO] Chart.yaml: icon is recommended
1 chart(s) linted, 0 chart(s) failed
```
```txt
fridorovich@DESKTOP-FRR2QTC:/home/devops/S25-core-course-labs/k8s$ helm install --dry-run helm-hooks ./python-web
NAME: helm-hooks
LAST DEPLOYED: Wed Apr 16 02:25:33 2025
NAMESPACE: default
STATUS: pending-install
REVISION: 1
HOOKS:
---
# Source: python-web/templates/tests/test-connection.yaml
apiVersion: v1
kind: Pod
metadata:
  name: "helm-hooks-python-web-test-connection"
  labels:
    helm.sh/chart: python-web-0.1.0
    app.kubernetes.io/name: python-web
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
      args: ['helm-hooks-python-web:8000']
  restartPolicy: Never
---
# Source: python-web/templates/post-install-hook.yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: "helm-hooks-post-install-hook"
  annotations:
    "helm.sh/hook": post-install
    "helm.sh/hook-weight": "0"
    "helm.sh/hook-delete-policy": hook-succeeded
spec:
  template:
    spec:
      containers:
      - name: post-install
        image: busybox
        command: ["/bin/sh", "-c", "echo 'Post-install hook is running'; sleep 20"]
      restartPolicy: Never
---
# Source: python-web/templates/pre-install-hook.yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: "helm-hooks-pre-install-hook"
  annotations:
    "helm.sh/hook": pre-install
    "helm.sh/hook-weight": "0"
    "helm.sh/hook-delete-policy": hook-succeeded
spec:
  template:
    spec:
      containers:
      - name: pre-install
        image: busybox
        command: ["/bin/sh", "-c", "echo 'Pre-install hook is running'; sleep 20"]
      restartPolicy: Never
MANIFEST:
---
# Source: python-web/templates/serviceaccount.yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: helm-hooks-python-web
  labels:
    helm.sh/chart: python-web-0.1.0
    app.kubernetes.io/name: python-web
    app.kubernetes.io/instance: helm-hooks
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
automountServiceAccountToken: true
---
# Source: python-web/templates/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: helm-hooks-python-web
  labels:
    helm.sh/chart: python-web-0.1.0
    app.kubernetes.io/name: python-web
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
    app.kubernetes.io/name: python-web
    app.kubernetes.io/instance: helm-hooks
---
# Source: python-web/templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: helm-hooks-python-web
  labels:
    helm.sh/chart: python-web-0.1.0
    app.kubernetes.io/name: python-web
    app.kubernetes.io/instance: helm-hooks
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
spec:
  replicas: 3
  selector:
    matchLabels:
      app.kubernetes.io/name: python-web
      app.kubernetes.io/instance: helm-hooks
  template:
    metadata:
      labels:
        helm.sh/chart: python-web-0.1.0
        app.kubernetes.io/name: python-web
        app.kubernetes.io/instance: helm-hooks
        app.kubernetes.io/version: "1.16.0"
        app.kubernetes.io/managed-by: Helm
    spec:
      serviceAccountName: helm-hooks-python-web
      containers:
        - name: python-web
          image: "fridorovich04/python-web:latest"
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
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=python-web,app.kubernetes.io/instance=helm-hooks" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
```
```txt
fridorovich@DESKTOP-FRR2QTC:/home/devops/S25-core-course-labs/k8s$ helm install --name-template=python-web python-web
NAME: python-web
LAST DEPLOYED: Wed Apr 16 02:36:22 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=python-web,app.kubernetes.io/instance=python-web" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
```
```txt
fridorovich@DESKTOP-FRR2QTC:/home/devops/S25-core-course-labs/k8s$ kubectl get po
NAME                         READY   STATUS      RESTARTS   AGE
post-install                 0/1     Completed   0          12m
pre-install                  0/1     Completed   0          12m
python-web-856974874-bcwbc   1/1     Running     0          12m
python-web-856974874-fgcc5   1/1     Running     0          12m
python-web-856974874-l25gc   1/1     Running     0          12m
```