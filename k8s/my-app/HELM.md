# Lab 10: Introduction to Helm

## Task 1

### Pods review

#### Command

```bash
kubectl get pods
```

#### Output

```bash
NAME                         READY   STATUS    RESTARTS   AGE
app-my-app-b6cb97564-g2zzb   1/1     Running   0          4m20s
```

### Services review

#### Command

```bash
kubectl get svc
```

#### Output

```bash
NAME         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
app-my-app   ClusterIP   10.97.119.126   <none>        80/TCP    4m25s
kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP   9h
```

## Task 2

### Command

```bash
helm lint my-app
```

### Output

```bash
==> Linting my-app
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed
```

### Command

```bash
helm install --dry-run helm-hooks my-app
```

### Output

```bash
NAME: helm-hooks
LAST DEPLOYED: Mon Feb 24 22:00:48 2025
NAMESPACE: default
STATUS: pending-install
REVISION: 1
HOOKS:
---
# Source: my-app/templates/post-install-hook.yaml
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
# Source: my-app/templates/pre-install-hook.yaml
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
# Source: my-app/templates/tests/test-connection.yaml
apiVersion: v1
kind: Pod
metadata:
  name: "helm-hooks-my-app-test-connection"
  labels:
    helm.sh/chart: my-app-0.1.0
    app.kubernetes.io/name: my-app
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
      args: ['helm-hooks-my-app:80']
  restartPolicy: Never
MANIFEST:
---
# Source: my-app/templates/serviceaccount.yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: helm-hooks-my-app
  labels:
    helm.sh/chart: my-app-0.1.0
    app.kubernetes.io/name: my-app
    app.kubernetes.io/instance: helm-hooks
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
automountServiceAccountToken: true
---
# Source: my-app/templates/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: helm-hooks-my-app
  labels:
    helm.sh/chart: my-app-0.1.0
    app.kubernetes.io/name: my-app
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
    app.kubernetes.io/name: my-app
    app.kubernetes.io/instance: helm-hooks
---
# Source: my-app/templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: helm-hooks-my-app
  labels:
    helm.sh/chart: my-app-0.1.0
    app.kubernetes.io/name: my-app
    app.kubernetes.io/instance: helm-hooks
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
spec:
  replicas: 1
  selector:
    matchLabels:
      app.kubernetes.io/name: my-app
      app.kubernetes.io/instance: helm-hooks
  template:
    metadata:
      labels:
        helm.sh/chart: my-app-0.1.0
        app.kubernetes.io/name: my-app
        app.kubernetes.io/instance: helm-hooks
        app.kubernetes.io/version: "1.16.0"
        app.kubernetes.io/managed-by: Helm
    spec:
      serviceAccountName: helm-hooks-my-app
      containers:
        - name: my-app
          image: "nikachek/moscow-time-api:latest"
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
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=my-app,app.kubernetes.io/instance=helm-hooks" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
```

### Command

```bash
kubectl get po
```

### Output

```bash
NAME                                READY   STATUS      RESTARTS   AGE
app-my-app-b6cb97564-g2zzb          1/1     Running     0          19m
helm-hooks-my-app-7cc9b5684-tghlw   1/1     Running     0          3m17s
postinstall-hook                    0/1     Completed   0          3m16s
preinstall-hook                     0/1     Completed   0          4m24s
```

### Command

```bash
kubectl get pods
```

### Output

```bash
NAME                                READY   STATUS    RESTARTS   AGE
app-my-app-b6cb97564-g2zzb          1/1     Running   0          26m
helm-hooks-my-app-7cc9b5684-n94z4   1/1     Running   0          76s
```

### Command

```bash
kubectl get svc
```

### Output
```bah
NAME                TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
app-my-app          ClusterIP   10.97.119.126    <none>        80/TCP    26m
helm-hooks-my-app   ClusterIP   10.102.232.233   <none>        80/TCP    80s
kubernetes          ClusterIP   10.96.0.1        <none>        443/TCP   10h
```

