# **HELM.md**

## **Lab 10: Introduction to Helm**

### **Overview**
In this lab, we explored Helm, a package manager for Kubernetes, to create, deploy, and manage Helm charts for two applications: **Java App** and **Python App**. We also implemented Helm hooks, created a library chart, and ensured that all services were healthy and accessible.

---

## **Task 1: Helm Setup and Chart Creation**

### **Step 1: Helm Installation**
Helm was successfully installed using the official instructions:
[Helm Installation](https://helm.sh/docs/intro/install/)

### **Step 2: Create Helm Charts**
Helm charts were created for both applications using the following commands:
```bash
helm create java-app
helm create python-app
```

### Step 2: Update `values.yaml` and Modify `deployment.yaml`

The `values.yaml` files were updated with the correct container images and ports:

- **Java App**:
  - Image: `nickwidbestie/random-color-picker:6d9f319aeb8fe1782ca1a1037371a90ab8867a3f`
  - Port: `8081`

- **Python App**:
  - Image: `nickwidbestie/region-time-api:latest`
  - Port: `80`

The `deployment.yaml` files were modified to include liveness and readiness probes:

- **Java App**:
  - Path: `/hex/color`
  - Port: `8081`

- **Python App**:
  - Path: `/time/moscow`
  - Port: `80`

### Step 3: Install Helm Charts

The Helm charts were installed successfully:

```bash
helm install java-app-release ./java-app
helm install python-app-release ./python-app
```

### Step 4: Verify Application Accessibility

Both applications were verified to be healthy and accessible using the Minikube dashboard and the following commands:

```bash
minikube service java-app-release
minikube service python-app-release
```

Output:
```commandline
NAME                                      READY   STATUS    RESTARTS   AGE
pod/java-app-release-6776b855fb-tt86x     1/1     Running   0          5m
pod/python-app-release-79f9b5774b-z9kps   1/1     Running   0          5m

NAME                          TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
service/java-app-release      ClusterIP   10.104.121.99             8081/TCP   5m
service/kubernetes            ClusterIP   10.96.0.1                 443/TCP    10m
service/python-app-release    ClusterIP   10.105.167.122            80/TCP     5m
```

Screenshot from the Minikube Dashboard:
[]

### Task 2: Helm Chart Hooks

#### Step 1: Implement Pre-Install and Post-Install Hooks

Pre-install and post-install hooks were implemented in both the **Java** and **Python** charts. The hook definitions are as follows:

---

##### **Pre-Install Hook**

The pre-install hook ensures that certain actions are executed before the main chart resources are deployed. Below is the YAML definition for the pre-install hook:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: "preinstall-hook"
  annotations:
    "helm.sh/hook": pre-install
    "helm.sh/hook-delete-policy": hook-succeeded
spec:
  containers:
  - name: pre-install-container
    image: busybox
    imagePullPolicy: IfNotPresent
    command: ['sh', '-c', 'echo The pre-install hook is running && sleep 20']
  restartPolicy: Never
  terminationGracePeriodSeconds: 0
```

### Post-Install Hook

The post-install hook ensures that certain actions are executed after the main chart resources are successfully deployed. Below is the YAML definition for the post-install hook:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: "postinstall-hook"
  annotations:
    "helm.sh/hook": post-install
    "helm.sh/hook-delete-policy": hook-succeeded
spec:
  containers:
  - name: post-install-container
    image: busybox
    imagePullPolicy: Always
    command: ['sh', '-c', 'echo The post-install hook is running && sleep 15']
  restartPolicy: Never
  terminationGracePeriodSeconds: 0
```

### Step 2: Troubleshoot Hooks

The hooks were validated using the following commands:

```bash
helm lint java-app
helm lint python-app
helm install --dry-run helm-hooks java-app
helm install --dry-run helm-hooks python-app
```

Output of kubectl get pods:
```commandline
NAME                                    READY   STATUS    RESTARTS   AGE
helm-hooks-java-app-5fc6fc9c47-dwdbt   1/1     Running   0          2m
java-app-release-6776b855fb-tt86x      1/1     Running   0          10m
python-app-release-79f9b5774b-z9kps    1/1     Running   0          10m
```

```commandline
command: kubectl get po
NAME                                  READY   STATUS    RESTARTS   AGE
java-app-release-6776b855fb-tt86x     1/1     Running   0          4m16s
python-app-release-79f9b5774b-z9kps   1/1     Running   0          4m4s
```

```commandline
kubectl describe po helm-hooks-java-app-5fc6fc9c47-dwdbt
Name:             helm-hooks-java-app-5fc6fc9c47-dwdbt
Namespace:        default
Priority:         0
Service Account:  helm-hooks-java-app
Node:             minikube/192.168.49.2
Start Time:       Sun, 02 Mar 2025 21:38:51 +0300
Labels:           app.kubernetes.io/instance=helm-hooks
                  app.kubernetes.io/managed-by=Helm
                  app.kubernetes.io/name=java-app
                  app.kubernetes.io/version=1.16.0
                  helm.sh/chart=java-app-0.1.0
                  pod-template-hash=5fc6fc9c47
Annotations:      <none>
Status:           Running
IP:               10.244.0.42
IPs:
  IP:           10.244.0.42
Controlled By:  ReplicaSet/helm-hooks-java-app-5fc6fc9c47
Containers:
  java-app:
    Container ID:   docker://4f319f045548af08be5662591fb40b62a5a7af3a924af209a2e057a0183f4511
    Image:          nickwidbestie/random-color-picker:6d9f319aeb8fe1782ca1a1037371a90ab8867a3f
    Image ID:       docker-pullable://nickwidbestie/random-color-picker@sha256:ebd3352214a6ad033e144fcc100efcceb6ccb356e09137dd368a471fa5226fcb
    Port:           8081/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Sun, 02 Mar 2025 21:38:52 +0300
    Ready:          True
    Restart Count:  0
    Limits:
      cpu:     1
      memory:  1Gi
    Requests:
      cpu:        500m
      memory:     512Mi
    Liveness:     http-get http://:8081/hex/color delay=5s timeout=1s period=10s #success=1 #failure=3
    Readiness:    http-get http://:8081/hex/color delay=5s timeout=1s period=10s #success=1 #failure=3
    Environment:  <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-kbzsn (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       True 
  ContainersReady             True 
  PodScheduled                True 
Volumes:
  kube-api-access-kbzsn:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   Burstable
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  104s  default-scheduler  Successfully assigned default/helm-hooks-java-app-5fc6fc9c47-dwdbt to minikube
  Normal  Pulled     103s  kubelet            Container image "nickwidbestie/random-color-picker:6d9f319aeb8fe1782ca1a1037371a90ab8867a3f" already present on machine
  Normal  Created    103s  kubelet            Created container: java-app
  Normal  Started    103s  kubelet            Started container java-app

```

Output of kubectl describe pod <preinstall_hook_name>:
```commandline
Name:             preinstall-hook
Namespace:        default
Priority:         0
Node:             minikube/192.168.49.2
Start Time:       Sun, 02 Mar 2025 21:38:51 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
                  helm.sh/hook-delete-policy: hook-succeeded
Status:           Succeeded
...
Events:
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  104s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     103s  kubelet            Container image "busybox" already present on machine
  Normal  Created    103s  kubelet            Created container: pre-install-container
  Normal  Started    103s  kubelet            Started container pre-install-container
```

Output of kubectl describe pod <postinstall_hook_name>:
```commandline
Name:             postinstall-hook
Namespace:        default
Priority:         0
Node:             minikube/192.168.49.2
Start Time:       Sun, 02 Mar 2025 21:38:51 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
                  helm.sh/hook-delete-policy: hook-succeeded
Status:           Succeeded
...
Events:
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  104s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulled     103s  kubelet            Container image "busybox" already present on machine
  Normal  Created    103s  kubelet            Created container: post-install-container
  Normal  Started    103s  kubelet            Started container post-install-container
```

### Bonus Task: Helm Library Chart

#### Step 1: Create a Library Chart

A library chart named `my-library` was created to define reusable templates. The `labels` template was added to `_helpers.tpl`:

```yaml
{{- define "my-library.labels" -}}
app.kubernetes.io/name: {{ include "my-library.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/version: "{{ .Chart.AppVersion }}"
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}
```

### Step 2: Use the Library Chart

The `my-library` chart was referenced in both `java-app` and `python-app` charts. The `labels` template was used in the `deployment.yaml` files:

```yaml
metadata:
  labels:
    {{- include "my-library.labels" . | nindent 4 }}
    {{- include "python-app.labels" . | nindent 4 }}
spec:
  selector:
    matchLabels:
      {{- include "my-library.labels" . | nindent 6 }}
      {{- include "python-app.selectorLabels" . | nindent 6 }}
template:
  metadata:
    labels:
      {{- include "my-library.labels" . | nindent 8 }}
      {{- include "python-app.labels" . | nindent 8 }}
```

Update dependencies by:
```commandline
helm dependency update
```

Output:
```commandline
Saving 1 charts
Deleting outdated charts
```

As for the **helm upgrade --install python-app-release python-app** the output is:
```commandline
Release "python-app-release" has been upgraded. Happy Helming!
NAME: python-app-release
LAST DEPLOYED: Sun Mar  2 22:04:42 2025
NAMESPACE: default
STATUS: deployed
REVISION: 6
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=python-app,app.kubernetes.io/instance=python-app-release" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
```