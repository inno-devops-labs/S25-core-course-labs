# Helm Chart Documentation

## Overview
This document outlines the Helm chart setup for our Python application.

## Setup

1. Install Helm:
```bash
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
```

2. Create Helm chart:
```bash
cd k8s
helm create python-app
```

3. Customize chart files:

### values.yaml
```yaml
replicaCount: 3

image:
  repository: mazzz3r/app_python
  pullPolicy: IfNotPresent
  tag: "latest"

serviceAccount:
  create: false
  annotations: {}
  name: ""
  automount: true

service:
  type: NodePort
  port: 5000
  nodePort: 30001

ingress:
  enabled: false
  className: ""
  annotations: {}
  hosts:
    - host: chart-example.local
      paths:
        - path: /
          pathType: ImplementationSpecific
  tls: []

autoscaling:
  enabled: false
  minReplicas: 1
  maxReplicas: 100
  targetCPUUtilizationPercentage: 80

resources: {}
```

### templates/deployment.yaml
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "python-app.fullname" . }}
  labels:
    {{- include "python-app.labels" . | nindent 4 }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      {{- include "python-app.selectorLabels" . | nindent 6 }}
  template:
    metadata:
      labels:
        {{- include "python-app.selectorLabels" . | nindent 8 }}
    spec:
      containers:
        - name: {{ .Chart.Name }}
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag | default .Chart.AppVersion }}"
          imagePullPolicy: {{ .Values.image.pullPolicy }}
          ports:
            - name: http
              containerPort: 5000
              protocol: TCP
          env:
            - name: TZ
              value: "Europe/Moscow"
          # Comment out the probes as they might cause issues
          # livenessProbe:
          #   httpGet:
          #     path: /
          #     port: http
          # readinessProbe:
          #   httpGet:
          #     path: /
          #     port: http
          resources:
            {{- toYaml .Values.resources | nindent 12 }}
```

### templates/pre-install-job.yaml
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: "{{ .Release.Name }}-pre-install"
  annotations:
    "helm.sh/hook": pre-install
    "helm.sh/hook-weight": "-5"
    "helm.sh/hook-delete-policy": hook-succeeded
spec:
  template:
    metadata:
      name: "{{ .Release.Name }}-pre-install"
    spec:
      restartPolicy: Never
      containers:
      - name: pre-install-job
        image: busybox
        command: ["sh", "-c", "echo Pre-install hook running && sleep 60"]
```

### templates/post-install-job.yaml
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: "{{ .Release.Name }}-post-install"
  annotations:
    "helm.sh/hook": post-install
    "helm.sh/hook-weight": "5"
    "helm.sh/hook-delete-policy": hook-succeeded
spec:
  template:
    metadata:
      name: "{{ .Release.Name }}-post-install"
    spec:
      restartPolicy: Never
      containers:
      - name: post-install-job
        image: busybox
        command: ["sh", "-c", "echo Post-install hook running && sleep 60"]
```

4. Install the chart:
```bash
helm install python-app-release ./python-app
```

## Current Status

### Pods and Services
```bash
# Output of kubectl get pods,svc
NAME                                      READY   STATUS    RESTARTS      AGE
pod/python-app-5d57df446c-2hrnf           1/1     Running   1 (44m ago)   58m
pod/python-app-5d57df446c-gnjvx           1/1     Running   1 (44m ago)   58m
pod/python-app-5d57df446c-t7zph           1/1     Running   1 (44m ago)   58m
pod/python-app-release-696c67fc9b-9229j   1/1     Running   0             79s
pod/python-app-release-696c67fc9b-9h6bk   1/1     Running   0             79s
pod/python-app-release-696c67fc9b-bbpld   1/1     Running   0             79s

NAME                         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/kubernetes           ClusterIP   10.96.0.1        <none>        443/TCP          59m
service/python-app-release   NodePort    10.107.188.152   <none>        5000:30000/TCP   79s
```

### Hook Details

#### Pre-install Hook
```bash
# Output of kubectl describe pod for pre-install hook
kubectl describe pod $(kubectl get pods -l job-name=python-app-release-pre-install -o jsonpath='{.items[0].metadata.name}')

Name:             python-app-release-pre-install-q29hq
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 26 Feb 2025 12:33:16 +0300
Labels:           batch.kubernetes.io/controller-uid=62572545-45cc-46b6-bd6c-1c650e1960c6
                  batch.kubernetes.io/job-name=python-app-release-pre-install
                  controller-uid=62572545-45cc-46b6-bd6c-1c650e1960c6
                  job-name=python-app-release-pre-install
Annotations:      <none>
Status:           Running
IP:               10.244.0.23
IPs:
  IP:           10.244.0.23
Controlled By:  Job/python-app-release-pre-install
Containers:
  pre-install-job:
    Container ID:  docker://2b53bcfe5942e3d4b3bd26b5f8cf5805bb219489cd1b25e8fb7c8c147b59596f
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo Pre-install hook running && sleep 60
    State:          Running
      Started:      Wed, 26 Feb 2025 12:33:18 +0300
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-wb6f6 (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       True 
  ContainersReady             True 
  PodScheduled                True 
Volumes:
  kube-api-access-wb6f6:
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
  Normal  Scheduled  27s   default-scheduler  Successfully assigned default/python-app-release-pre-install-q29hq to minikube
  Normal  Pulling    27s   kubelet            Pulling image "busybox"
  Normal  Pulled     25s   kubelet            Successfully pulled image "busybox" in 1.948s (1.948s including waiting). Image size: 4042190 bytes.
  Normal  Created    25s   kubelet            Created container: pre-install-job
  Normal  Started    25s   kubelet            Started container pre-install-job
```

#### Post-install Hook
```bash
# Output of kubectl describe pod for post-install hook
kubectl describe pod $(kubectl get pods -l job-name=python-app-release-post-install -o jsonpath='{.items[0].metadata.name}')

Name:             python-app-release-post-install-8ts8b
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 26 Feb 2025 12:39:57 +0300
Labels:           batch.kubernetes.io/controller-uid=55eed81f-c853-46bc-bad2-4a9ae953f6b1
                  batch.kubernetes.io/job-name=python-app-release-post-install
                  controller-uid=55eed81f-c853-46bc-bad2-4a9ae953f6b1
                  job-name=python-app-release-post-install
Annotations:      <none>
Status:           Running
IP:               10.244.0.31
IPs:
  IP:           10.244.0.31
Controlled By:  Job/python-app-release-post-install
Containers:
  post-install-job:
    Container ID:  docker://28d615f297a6a978f40a7aa764f8eae1f5c037d126f14b1c41499bc321b6db64
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo Post-install hook running && sleep 60
    State:          Running
      Started:      Wed, 26 Feb 2025 12:40:00 +0300
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-9fznr (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       True 
  ContainersReady             True 
  PodScheduled                True 
Volumes:
  kube-api-access-9fznr:
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
  Normal  Scheduled  9s    default-scheduler  Successfully assigned default/python-app-release-post-install-8ts8b to minikube
  Normal  Pulling    9s    kubelet            Pulling image "busybox"
  Normal  Pulled     7s    kubelet            Successfully pulled image "busybox" in 1.865s (1.865s including waiting). Image size: 4042190 bytes.
  Normal  Created    7s    kubelet            Created container: post-install-job
  Normal  Started    7s    kubelet            Started container post-install-job
```

### Application Access
To access the application:
```bash
minikube service python-app-release
```

```bash
# Output of minikube service python-app-release
|-----------|--------------------|-------------|---------------------------|
| NAMESPACE |        NAME        | TARGET PORT |            URL            |
|-----------|--------------------|-------------|---------------------------|
| default   | python-app-release | http/5000   | http://192.168.49.2:30000 |
|-----------|--------------------|-------------|---------------------------|
🏃  Starting tunnel for service python-app-release.
|-----------|--------------------|-------------|------------------------|
| NAMESPACE |        NAME        | TARGET PORT |          URL           |
|-----------|--------------------|-------------|------------------------|
| default   | python-app-release |             | http://127.0.0.1:53397 |
|-----------|--------------------|-------------|------------------------|
🎉  Opening service default/python-app-release in default browser...
❗  Because you are using a Docker driver on darwin, the terminal needs to be open to run it.
```

## Cleanup

To uninstall the Helm chart:
```bash
helm uninstall python-app-release
```

To stop minikube:
```bash
minikube stop
```
