# Lab 10 Report

## Task 1: Helm Chart

### Pods and Services
```bash
kubectl get pods,svc -l app.kubernetes.io/instance=python-app
```

```
NAME                              READY   STATUS    RESTARTS   AGE
pod/python-app-64dc554f95-jfmfr   1/1     Running   0          5m4s

NAME                 TYPE       CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/python-app   NodePort   10.99.213.27   <none>        8080:32162/TCP   5m4s
```

## Task 2: Hooks

### Hook Execution Status
Hooks were successfully executed and automatically deleted according to the `hook-delete-policy`.

#### Execution Confirmation:
```bash
helm get hooks python-app
```

```
---
# Source: python-app/templates/post-install-hook.yaml
apiVersion: v1
kind: Pod
metadata:
  name: post-install-hook
  annotations:
    "helm.sh/hook": post-install
    "helm.sh/hook-delete-policy": before-creation,hook-succeeded
spec:
  containers:
  - name: busybox
    image: busybox
    command: ['sh', '-c', 'echo "Post-install hook executed!" && sleep 20']
  restartPolicy: Never
---
# Source: python-app/templates/pre-install-hook.yaml
apiVersion: v1
kind: Pod
metadata:
  name: pre-install-hook
  annotations:
    "helm.sh/hook": pre-install
    "helm.sh/hook-delete-policy": before-creation,hook-succeeded
spec:
  containers:
  - name: busybox
    image: busybox
    command: ['sh', '-c', 'echo "Pre-install hook executed!" && sleep 20']
  restartPolicy: Never
---
# Source: python-app/templates/tests/test-connection.yaml
apiVersion: v1
kind: Pod
metadata:
  name: "python-app-test-connection"
  labels:
    helm.sh/chart: python-app-0.1.0
    app.kubernetes.io/name: python-app
    app.kubernetes.io/instance: python-app
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
  annotations:
    "helm.sh/hook": test
spec:
  containers:
    - name: wget
      image: busybox
      command: ['wget']
      args: ['python-app:8080']
  restartPolicy: Never
```
