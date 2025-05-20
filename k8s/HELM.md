# Helm Chart Documentation

## Chart Information
- Chart Name: python-app
- Created using: `helm create python-app`
- Location: `k8s/python-app/`

## Deployment Status
Current status of pods and services:
```bash
$ kubectl get pods,svc
NAME                             READY   STATUS    RESTARTS   AGE
pod/python-app-788f5cc5d-kl6lf   1/1     Running   0          32s

NAME                         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
service/kubernetes           ClusterIP   10.96.0.1       <none>        443/TCP        33h
service/python-app           ClusterIP   10.99.112.42    <none>        8000/TCP       32s
service/python-app-service   NodePort    10.102.207.85   <none>        80:31519/TCP   33h
```

## Installation
The chart has been successfully installed using:
```bash
helm install python-app ./python-app
```

Output:
```
NAME: python-app
LAST DEPLOYED: Tue May 20 04:03:15 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
```

## Accessing the Application
The application can be accessed using:
```bash
minikube service python-app
```

## Chart Hooks
The chart includes pre-install and post-install hooks as required in Task 2. These hooks are implemented in the templates directory.

Hook Names:
- Pre-install hook: `pre-install-hook`
- Post-install hook: `post-install-hook`

Hook Configuration:
```yaml
# Pre-install hook
metadata:
  name: pre-install-hook
  annotations:
    "helm.sh/hook": pre-install
    "helm.sh/hook-weight": "-5"
    "helm.sh/hook-delete-policy": hook-succeeded

# Post-install hook
metadata:
  name: post-install-hook
  annotations:
    "helm.sh/hook": post-install
    "helm.sh/hook-weight": "5"
    "helm.sh/hook-delete-policy": hook-succeeded
```

Note: The hooks have been executed and deleted as per the `hook-delete-policy: hook-succeeded` setting. This is the expected behavior - the hooks run once during installation and are then removed.

To see the hooks in action, we would need to temporarily remove the delete policy. The hooks would then be visible with:
```bash
kubectl describe po pre-install-hook
kubectl describe po post-install-hook
```

## Verification Steps
1. Chart syntax verification:
```bash
helm lint python-app
```
No errors were reported.

2. Dry run installation was successful:
```bash
helm install --dry-run helm-hooks python-app
```

3. Current pod status shows the main application pod is running:
```bash
kubectl get po
NAME                             READY   STATUS    RESTARTS   AGE
pod/python-app-788f5cc5d-kl6lf   1/1     Running   0          32s
```

## Hook Implementation Details
The hooks are implemented as Kubernetes Jobs that run a simple sleep command for 20 seconds:

Pre-install hook:
```yaml
spec:
  template:
    spec:
      containers:
      - name: pre-install
        image: busybox
        command: ["/bin/sh", "-c", "sleep 20"]
      restartPolicy: Never
  backoffLimit: 1
```

Post-install hook:
```yaml
spec:
  template:
    spec:
      containers:
      - name: post-install
        image: busybox
        command: ["/bin/sh", "-c", "sleep 20"]
      restartPolicy: Never
  backoffLimit: 1
``` 