# Helm Chart Deployments

This document provides information about the Helm chart deployments for both JavaScript and Python applications.

## 1. JavaScript Application

### Helm Chart Structure

The Helm chart is located in the `k8s/js-app` directory and follows the standard Helm chart structure:

```
js-app/
  Chart.yaml          # Chart metadata
  values.yaml         # Default configuration values
  templates/          # Kubernetes manifest templates
    deployment.yaml   # Deployment template
    service.yaml      # Service template
    _helpers.tpl      # Helper functions
    ...
```

### Deployment

The JavaScript Helm chart was deployed using the following command:

```bash
helm install js-app-release ./js-app
```

### Accessing the Application

The JavaScript application can be accessed using the following command:

```bash
minikube service js-app-release
```

This will open the application in your default web browser.

## 2. Python Application

### Helm Chart Structure

The Helm chart is located in the `k8s/python-app` directory and follows the standard Helm chart structure:

```
python-app/
  Chart.yaml          # Chart metadata
  values.yaml         # Default configuration values
  templates/          # Kubernetes manifest templates
    deployment.yaml   # Deployment template
    service.yaml      # Service template
    _helpers.tpl      # Helper functions
    ...
```

### Deployment

The Python Helm chart was deployed using the following command:

```bash
helm install python-app-release ./python-app
```

### Accessing the Application

The Python application can be accessed using the following command:

```bash
minikube service python-app-release
```

This will open the application in your default web browser.

## 3. Helm Chart Hooks

Helm chart hooks were implemented for both applications to run before and after the chart installations. The hooks are defined in the following files:

- `pre-install-hook.yaml`: Runs before the chart is installed
- `post-install-hook.yaml`: Runs after the chart is installed

### Hook Implementation

Both hooks use the busybox image and run a simple command that sleeps for 20 seconds. The hooks are configured with the `hook-succeeded` delete policy, which means they are automatically deleted after they complete successfully.

#### JavaScript Application Hooks

```yaml
# pre-install-hook.yaml
apiVersion: v1
kind: Pod
metadata:
  name: {{ .Release.Name }}-pre-install-hook
  annotations:
    "helm.sh/hook": pre-install
    "helm.sh/hook-weight": "-5"
    "helm.sh/hook-delete-policy": hook-succeeded
spec:
  containers:
  - name: pre-install-job
    image: busybox
    command: ['sh', '-c', 'echo Pre-install hook is running && sleep 20']
  restartPolicy: Never
```

```yaml
# post-install-hook.yaml
apiVersion: v1
kind: Pod
metadata:
  name: {{ .Release.Name }}-post-install-hook
  annotations:
    "helm.sh/hook": post-install
    "helm.sh/hook-weight": "5"
    "helm.sh/hook-delete-policy": hook-succeeded
spec:
  containers:
  - name: post-install-job
    image: busybox
    command: ['sh', '-c', 'echo Post-install hook is running && sleep 20']
  restartPolicy: Never
```

#### Python Application Hooks

```yaml
# pre-install-hook.yaml
apiVersion: v1
kind: Pod
metadata:
  name: {{ .Release.Name }}-pre-install-hook
  annotations:
    "helm.sh/hook": pre-install
    "helm.sh/hook-weight": "-5"
    "helm.sh/hook-delete-policy": hook-succeeded
spec:
  containers:
  - name: pre-install-job
    image: busybox
    command: ['sh', '-c', 'echo Pre-install hook for Python application is running && sleep 20']
  restartPolicy: Never
```

```yaml
# post-install-hook.yaml
apiVersion: v1
kind: Pod
metadata:
  name: {{ .Release.Name }}-post-install-hook
  annotations:
    "helm.sh/hook": post-install
    "helm.sh/hook-weight": "5"
    "helm.sh/hook-delete-policy": hook-succeeded
spec:
  containers:
  - name: post-install-job
    image: busybox
    command: ['sh', '-c', 'echo Post-install hook for Python application is running && sleep 20']
  restartPolicy: Never
```

## 4. Kubernetes Resources

The following Kubernetes resources were created for both applications:

```bash
$ kubectl get pods,svc
NAME                                     READY   STATUS    RESTARTS   AGE
pod/helm-hooks-js-app-66d98ccb6-4t82z    1/1     Running   0          5m17s
pod/helm-hooks-js-app-66d98ccb6-hwg9n    1/1     Running   0          5m17s
pod/helm-hooks-js-app-66d98ccb6-klf8w    1/1     Running   0          5m17s
pod/js-app-7c9644bbbd-p2ltl              1/1     Running   0          21m
pod/js-app-7c9644bbbd-rpsz6              1/1     Running   0          21m
pod/js-app-7c9644bbbd-wq8j2              1/1     Running   0          21m
pod/js-app-release-76548596f8-gnx74      1/1     Running   0          7m51s
pod/js-app-release-76548596f8-h4z6f      1/1     Running   0          7m51s
pod/js-app-release-76548596f8-lhdfp      1/1     Running   0          7m51s
pod/python-app-6589d9468-57vzw           1/1     Running   0          22m
pod/python-app-6589d9468-hmp7c           1/1     Running   0          22m
pod/python-app-6589d9468-rrn9g           1/1     Running   0          22m
pod/python-app-release-c7f4d6686-96vhq   1/1     Running   0          28s
pod/python-app-release-c7f4d6686-khvhh   1/1     Running   0          28s
pod/python-app-release-c7f4d6686-mcttf   1/1     Running   0          28s

NAME                         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/helm-hooks-js-app    NodePort    10.111.91.120    <none>        3000:32085/TCP   5m17s
service/js-app               NodePort    10.107.88.63     <none>        3000:30245/TCP   22m
service/js-app-release       NodePort    10.110.161.89    <none>        3000:32703/TCP   7m51s
service/kubernetes           ClusterIP   10.96.0.1        <none>        443/TCP          31m
service/python-app           NodePort    10.110.215.222   <none>        8000:31745/TCP   22m
service/python-app-release   NodePort    10.105.44.249    <none>        8000:30373/TCP   28s
```

The hooks for both applications were automatically deleted after they completed successfully due to the `hook-succeeded` delete policy.

## 5. Hook Examination

For the purpose of examining the hooks, we created a version without the delete policy. Here are the outputs of the required commands:

### kubectl get po

```bash
$ kubectl get po
NAME                                 READY   STATUS      RESTARTS   AGE
helm-hooks-js-app-66d98ccb6-4t82z    1/1     Running     0          13m
helm-hooks-js-app-66d98ccb6-hwg9n    1/1     Running     0          13m
helm-hooks-js-app-66d98ccb6-klf8w    1/1     Running     0          13m
hooks-demo-js-app-59b48466dc-7g58p   1/1     Running     0          33s
hooks-demo-js-app-59b48466dc-nrq5h   1/1     Running     0          33s
hooks-demo-js-app-59b48466dc-qq2lv   1/1     Running     0          33s
hooks-demo-post-install-hook         0/1     Completed   0          33s
hooks-demo-pre-install-hook          0/1     Completed   0          59s
js-app-7c9644bbbd-p2ltl              1/1     Running     0          30m
js-app-7c9644bbbd-rpsz6              1/1     Running     0          29m
js-app-7c9644bbbd-wq8j2              1/1     Running     0          29m
js-app-release-76548596f8-gnx74      1/1     Running     0          16m
js-app-release-76548596f8-h4z6f      1/1     Running     0          16m
js-app-release-76548596f8-lhdfp      1/1     Running     0          16m
python-app-6589d9468-57vzw           1/1     Running     0          31m
python-app-6589d9468-hmp7c           1/1     Running     0          31m
python-app-6589d9468-rrn9g           1/1     Running     0          31m
python-app-release-c7f4d6686-96vhq   1/1     Running     0          8m45s
python-app-release-c7f4d6686-khvhh   1/1     Running     0          8m45s
python-app-release-c7f4d6686-mcttf   1/1     Running     0          8m45s
```

### kubectl describe po hooks-demo-pre-install-hook

```bash
Name:             hooks-demo-pre-install-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sun, 02 Mar 2025 20:14:48 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
                  helm.sh/hook-weight: -5
Status:           Succeeded
IP:               10.244.0.26
IPs:
  IP:  10.244.0.26
Containers:
  pre-install-job:
    Container ID:  docker://59781651158adb3760ab4298cca627b91ee4ac5331a5450143fd5ff5c2c378a6
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo Pre-install hook is running && sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Sun, 02 Mar 2025 20:14:52 +0300
      Finished:     Sun, 02 Mar 2025 20:15:12 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-47hr5 (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-47hr5:
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
  Normal  Scheduled  63s   default-scheduler  Successfully assigned default/hooks-demo-pre-install-hook to minikube
  Normal  Pulling    62s   kubelet            Pulling image "busybox"
  Normal  Pulled     59s   kubelet            Successfully pulled image "busybox" in 3.604s (3.604s including waiting). Image size: 4042190 bytes.
  Normal  Created    59s   kubelet            Created container: pre-install-job
  Normal  Started    59s   kubelet            Started container pre-install-job
```

### kubectl describe po hooks-demo-post-install-hook

```bash
Name:             hooks-demo-post-install-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sun, 02 Mar 2025 20:15:14 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
                  helm.sh/hook-weight: 5
Status:           Succeeded
IP:               10.244.0.29
IPs:
  IP:  10.244.0.29
Containers:
  post-install-job:
    Container ID:  docker://825cc4ac1d7bcb4abf283aab2889370070d1dbb9a3c7d0f5fef80b90f9da44f8
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo Post-install hook is running && sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Sun, 02 Mar 2025 20:15:17 +0300
      Finished:     Sun, 02 Mar 2025 20:15:37 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-k7mv2 (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-k7mv2:
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
  Normal  Scheduled  40s   default-scheduler  Successfully assigned default/hooks-demo-post-install-hook to minikube
  Normal  Pulling    40s   kubelet            Pulling image "busybox"
  Normal  Pulled     37s   kubelet            Successfully pulled image "busybox" in 2.756s (2.756s including waiting). Image size: 4042190 bytes.
  Normal  Created    37s   kubelet            Created container: post-install-job
  Normal  Started    37s   kubelet            Started container post-install-job
```