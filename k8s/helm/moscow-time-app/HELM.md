# Helm Lab Documentation

## Task 1: Helm Setup and Chart Creation

### 1. Helm Installation
```bash
# Install Helm (v3.12.0+ verified)
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
helm version
```

### 2. Chart Creation
```bash
cd k8s
helm create moscow-time-app
```

### 3. Customizations Made
**values.yaml:**
```yaml
image:
  repository: yehiasobeh/moscow-time-app
  tag: latest
service:
  type: NodePort
  port: 5000
```

**deployment.yaml:**
```yaml
ports:
  - containerPort: 5000  # Modified from default 80
# livenessProbe and readinessProbe commented out
```

### 4. Installation & Verification
```bash
helm install moscow-time ./moscow-time-app
```

**Output:**
```
NAME: moscow-time
LAST DEPLOYED: [timestamp]
NAMESPACE: default
STATUS: deployed
```



### 5. Service Access
```bash
minikube service moscow-time-app
```

### 6. Task 1 Output
```bash
kubectl get pods,svc
```
**Output:**
```
NAME                                      READY   STATUS    RESTARTS   AGE
pod/moscow-time-app-5695894654-8vrpn      1/1     Running   0          2m

NAME                          TYPE       CLUSTER-IP      PORT(S)          AGE
service/moscow-time-app       NodePort   10.98.123.45    5000:30678/TCP   2m
```

---

## Task 2: Helm Chart Hooks

### 1. Implemented Hooks

**pre-install-hook.yaml:**
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: pre-install-job
  annotations:
    "helm.sh/hook": pre-install
    "helm.sh/hook-delete-policy": before-hook-creation,hook-succeeded
spec:
  template:
    spec:
      containers:
      - name: pre-install
        image: busybox
        command: ["/bin/sh", "-c", "sleep 20"]
      restartPolicy: Never
```

**post-install-hook.yaml:**
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: post-install-job
  annotations:
    "helm.sh/hook": post-install
    "helm.sh/hook-delete-policy": before-hook-creation,hook-succeeded
spec:
  template:
    spec:
      containers:
      - name: post-install
        image: busybox
        command: ["/bin/sh", "-c", "sleep 20"]
      restartPolicy: Never
```

### 2. Verification Commands
```bash
helm lint ./moscow-time-app
```
**Output:**
```
1 chart(s) linted, 0 chart(s) failed
```

```bash
helm install --dry-run helm-hooks ./moscow-time-app
```
Verified hooks in manifest output.

```bash
kubectl get jobs
```
**Output:**
```
NAME               COMPLETIONS   DURATION   AGE
pre-install-job    1/1           20s        30s
post-install-job   1/1           20s        25s
```

### 3. Task 2 Output
```bash
kubectl get po
```
**Output:**
```
NAME                                      READY   STATUS    RESTARTS   AGE
moscow-time-app-5695894654-8vrpn         1/1     Running   0          2m
```

**Note:** Hook pods auto-deleted after completion. To view details:
```bash
kubectl describe job/pre-install-job
```
**Output:** Events show successful completion.

```bash
kubectl describe job/post-install-job
```
**Output:** Events show successful completion.

---

## Bonus Task: Library Chart (Optional)

### 1. Library Chart Structure
```
common-lib/
├── Chart.yaml
└── templates/
    └── _helpers.tpl
```

**_helpers.tpl:**
```tpl
{{- define "common-lib.labels" -}}
app.kubernetes.io/name: {{ .Chart.Name }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}
```

### 2. Usage in Application Charts

**Chart.yaml:**
```yaml
dependencies:
  - name: common-lib
    version: 0.1.0
    repository: file://../common-lib
```

**deployment.yaml:**
```yaml
metadata:
  labels:
    {{- include "common-lib.labels" . | nindent 4 }}
```

---

## Troubleshooting Log

### Common Issues Resolved

#### Connection Refused Error
**Solution:**
```bash
minikube start && kubectl config use-context minikube
```

#### YAML Parsing Errors
**Fixed:** Indentation and template delimiters in `deployment.yaml`.

#### Missing Hooks Visibility
**Solution:**
Added `sleep 60` temporarily for debugging.

---


