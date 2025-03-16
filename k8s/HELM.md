# Helm Setup

1. I installed helm
2. I created default helm chart for my python app
```bash
  helm create app-python
```
3. I changed **values.yml** to work with my app
```yaml
image:
  repository: secretanry/python_app
  # This sets the pull policy for images.
  pullPolicy: IfNotPresent
  # Overrides the image tag whose default is the chart appVersion.
  tag: "latest"
```
```yaml
service:
  # This sets the service type more information can be found here: https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types
  type: ClusterIP
  # This sets the ports more information can be found here: https://kubernetes.io/docs/concepts/services-networking/service/#field-spec-ports
  port: 8000
```

4. I deployed my chart
```bash
  helm install app-python ./app-python
```
```
NAME: app-python
LAST DEPLOYED: Sun Mar  2 02:32:28 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=app-python,app.kubernetes.io/instance=app-python" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
```

5. Lets check chart status using **minikube dashboard**
![Dashboard](static/dashboard.png, "dashboard")

6. I verified that my app is accessible
![App](static/helm_app.png, "app")

7. Pods status
```bash
  kubectl get pods
```
```
  NAME                          READY   STATUS    RESTARTS   AGE
  app-python-587c89d856-pl4t9   1/1     Running   0          12m
```

8. Service status
```bash
  kubectl get svc
```
```
  NAME         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
  app-python   ClusterIP   10.103.90.217   <none>        8000/TCP   13m
  kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP    30m
```


# Helm hooks

1. I added logic for pre-install hook **./templates/pre-install-job.yml**
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: {{ .Chart.Name }}-preinstall
  annotations:
    "helm.sh/hook": pre-install
    "helm.sh/hook-weight": "-5"
spec:
  template:
    spec:
      containers:
        - name: preinstall
          image: busybox
          command: ["/bin/sh", "-c", "sleep 20; echo Pre-install hook completed"]
      restartPolicy: Never
```

2. I added logic for post-install hook **./templates/post-install-job.yml**
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: {{ .Chart.Name }}-postinstall
  annotations:
    "helm.sh/hook": post-install
    "helm.sh/hook-weight": "5"
spec:
  template:
    spec:
      containers:
        - name: postinstall
          image: busybox
          command: ["/bin/sh", "-c", "sleep 20; echo Post-install hook completed"]
      restartPolicy: Never
```

3. Hooks troubleshooting
```bash
  helm lint app-python
```
```
  ==> Linting app-python
  [INFO] Chart.yaml: icon is recommended

  1 chart(s) linted, 0 chart(s) failed
```

```bash
  helm install --dry-run helm-hooks app-python
```
```
NAME: helm-hooks
LAST DEPLOYED: Sun Mar  2 02:54:42 2025
NAMESPACE: default
STATUS: pending-install
REVISION: 1
HOOKS:
---
# Source: app-python/templates/tests/test-connection.yaml
apiVersion: v1
kind: Pod
metadata:
  name: "helm-hooks-app-python-test-connection"
  labels:
    helm.sh/chart: app-python-0.1.0
    app.kubernetes.io/name: app-python
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
      args: ['helm-hooks-app-python:8000']
  restartPolicy: Never
---
# Source: app-python/templates/post-install-job.yml
apiVersion: batch/v1
kind: Job
metadata:
  name: app-python-postinstall
  annotations:
    "helm.sh/hook": post-install
    "helm.sh/hook-weight": "5"
    "helm.sh/hook-delete-policy": hook-succeeded
spec:
  template:
    spec:
      containers:
        - name: postinstall
          image: busybox
          command: ["/bin/sh", "-c", "sleep 20; echo Post-install hook completed"]
      restartPolicy: Never
---
# Source: app-python/templates/pre-install-job.yml
apiVersion: batch/v1
kind: Job
metadata:
  name: app-python-preinstall
  annotations:
    "helm.sh/hook": pre-install
    "helm.sh/hook-weight": "-5"
    "helm.sh/hook-delete-policy": hook-succeeded
spec:
  template:
    spec:
      containers:
        - name: preinstall
          image: busybox
          command: ["/bin/sh", "-c", "sleep 20; echo Pre-install hook completed"]
      restartPolicy: Never
MANIFEST:
---
# Source: app-python/templates/serviceaccount.yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: helm-hooks-app-python
  labels:
    helm.sh/chart: app-python-0.1.0
    app.kubernetes.io/name: app-python
    app.kubernetes.io/instance: helm-hooks
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
automountServiceAccountToken: true
---
# Source: app-python/templates/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: helm-hooks-app-python
  labels:
    helm.sh/chart: app-python-0.1.0
    app.kubernetes.io/name: app-python
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
    app.kubernetes.io/name: app-python
    app.kubernetes.io/instance: helm-hooks
---
# Source: app-python/templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: helm-hooks-app-python
  labels:
    helm.sh/chart: app-python-0.1.0
    app.kubernetes.io/name: app-python
    app.kubernetes.io/instance: helm-hooks
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
spec:
  replicas: 1
  selector:
    matchLabels:
      app.kubernetes.io/name: app-python
      app.kubernetes.io/instance: helm-hooks
  template:
    metadata:
      labels:
        helm.sh/chart: app-python-0.1.0
        app.kubernetes.io/name: app-python
        app.kubernetes.io/instance: helm-hooks
        app.kubernetes.io/version: "1.16.0"
        app.kubernetes.io/managed-by: Helm
    spec:
      serviceAccountName: helm-hooks-app-python
      containers:
        - name: app-python
          image: "secretanry/python_app:latest"
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
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=app-python,app.kubernetes.io/instance=helm-hooks" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
```
```bash
  kubectl get po
```
```
NAME                          READY   STATUS    RESTARTS   AGE
app-python-587c89d856-pl4t9   1/1     Running   0          23m
```

4. Info commands after reinstallation with hooks
```bash
  kubectl get po
```
```
NAME                           READY   STATUS      RESTARTS   AGE
app-python-587c89d856-xr2j9    1/1     Running     0          50s
app-python-postinstall-5flp7   0/1     Completed   0          50s
app-python-preinstall-xs6bn    0/1     Completed   0          77s
```

```bash
  kubectl describe po app-python-preinstall
```
```
Name:             app-python-preinstall-xs6bn
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sun, 02 Mar 2025 03:02:42 +0300
Labels:           batch.kubernetes.io/controller-uid=552d13c8-10f9-4467-b8a8-2917e3ec82d7
                  batch.kubernetes.io/job-name=app-python-preinstall
                  controller-uid=552d13c8-10f9-4467-b8a8-2917e3ec82d7
                  job-name=app-python-preinstall
Annotations:      <none>
Status:           Succeeded
IP:               10.244.0.20
IPs:
  IP:           10.244.0.20
Controlled By:  Job/app-python-preinstall
Containers:
  preinstall:
    Container ID:  docker://4deda9a3cd29221f5cc3829666b997c7fcf2260e7e0c396fd2e950dd825f2617
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
      /bin/sh
      -c
      sleep 20; echo Pre-install hook completed
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Sun, 02 Mar 2025 03:02:45 +0300
      Finished:     Sun, 02 Mar 2025 03:03:06 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-pxm9g (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-pxm9g:
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
  Normal  Scheduled  2m1s  default-scheduler  Successfully assigned default/app-python-preinstall-xs6bn to minikube
  Normal  Pulling    2m    kubelet            Pulling image "busybox"
  Normal  Pulled     118s  kubelet            Successfully pulled image "busybox" in 2.489s (2.489s including waiting). Image size: 4042190 bytes.
  Normal  Created    118s  kubelet            Created container: preinstall
  Normal  Started    118s  kubelet            Started container preinstall
```

```bash
  kubectl describe po app-python-postinstall
```
```
Name:             app-python-postinstall-5flp7
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sun, 02 Mar 2025 03:03:09 +0300
Labels:           batch.kubernetes.io/controller-uid=dcffa2dc-9c70-49f2-acc8-a509bf7d5a5c
                  batch.kubernetes.io/job-name=app-python-postinstall
                  controller-uid=dcffa2dc-9c70-49f2-acc8-a509bf7d5a5c
                  job-name=app-python-postinstall
Annotations:      <none>
Status:           Succeeded
IP:               10.244.0.22
IPs:
  IP:           10.244.0.22
Controlled By:  Job/app-python-postinstall
Containers:
  postinstall:
    Container ID:  docker://6aa138b149c8328baff8a88db425009bd5e630c148c4d6301ae44089836c98e7
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
      /bin/sh
      -c
      sleep 20; echo Post-install hook completed
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Sun, 02 Mar 2025 03:03:11 +0300
      Finished:     Sun, 02 Mar 2025 03:03:31 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-2vxff (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-2vxff:
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
  Type    Reason     Age    From               Message
  ----    ------     ----   ----               -------
  Normal  Scheduled  2m22s  default-scheduler  Successfully assigned default/app-python-postinstall-5flp7 to minikube
  Normal  Pulling    2m22s  kubelet            Pulling image "busybox"
  Normal  Pulled     2m20s  kubelet            Successfully pulled image "busybox" in 1.925s (1.925s including waiting). Image size: 4042190 bytes.
  Normal  Created    2m20s  kubelet            Created container: postinstall
  Normal  Started    2m20s  kubelet            Started container postinstall
```

5. Hook delete policy
I added such line to both configurations to delete all succeeded hooks 
```yaml
    "helm.sh/hook-delete-policy": hook-succeeded
```

# Bonus

1. I created the same default chart with corresponding changes
2. Verified deployment
```bash
  kubectl get po
```
```
NAME                           READY   STATUS      RESTARTS   AGE
app-go-6477bd4964-q7wlv        1/1     Running     0          37s
app-python-587c89d856-xr2j9    1/1     Running     0          7m40s
app-python-postinstall-5flp7   0/1     Completed   0          7m40s
app-python-preinstall-xs6bn    0/1     Completed   0          8m7s
```

## Library charts
1. I created **charts** folder inside **k8s** directory and folder **common-lib** inside of it
2. Inside **common-lib** i created **Chart.yaml** file and **templates** directory
```yaml
  apiVersion: v2
  name: common-lib
  description: Common labels library chart fo python app
  type: library
  version: 0.1.0
```
3. Inside **templates** directory I created **_labels.tpl** file
```
{{- define "common.labels" -}}
helm.sh/chart: {{ .Chart.Name }}-{{ .Chart.Version | replace "+" "_" }}
app.kubernetes.io/name: {{ .Chart.Name }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/version: {{ .Chart.Version }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end -}}
```

4. I added these lines to Charts of both apps
```yaml
  dependencies:
    - name: common-lib
      version: 0.1.0
      repository: file://../charts/common-lib
```

5. I updated dependencies of both apps
```bash
  helm dependency update ./app-python
```
```
Saving 1 charts
Deleting outdated charts
```

```bash
  helm dependency update ./app-go
```
```
Saving 1 charts
Deleting outdated charts
```

6. Labels update
Python:
```yaml
   labels:
      {{- include "common.labels" . | nindent 4 }}
      app-python/special-label: "app-python"
```
Go:
```yaml
    labels:
      {{- include "common.labels" . | nindent 4 }}
      app-go/special-label: "app-go"
```

7. Final versions of deployments
Python:
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Chart.Name }}
  labels:
    {{- include "common.labels" . | nindent 4 }}
    app-python/special-label: "app-python"
spec:
  selector:
    matchLabels:
      app.kubernetes.io/name: {{ .Chart.Name }}
  template:
    metadata:
      labels:
        {{- include "common.labels" . | nindent 8 }}
    spec:
      containers:
        - name: {{ .Chart.Name }}
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
          ports:
            - name: http
              containerPort: {{ .Values.service.port }}
              protocol: TCP
```
Go:
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Chart.Name }}
  labels:
    {{- include "common.labels" . | nindent 4 }}
    app-go/special-label: "app-go"
spec:
  selector:
    matchLabels:
      app.kubernetes.io/name: {{ .Chart.Name }}
  template:
    metadata:
      labels:
        {{- include "common.labels" . | nindent 8 }}
    spec:
      containers:
        - name: {{ .Chart.Name }}
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
          ports:
            - name: http
              containerPort: {{ .Values.service.port }}
              protocol: TCP
```

8. Finally, I deployed my apps and verified the deployment 
```bash
  kubectl get po
```
```
NAME                          READY   STATUS    RESTARTS   AGE
app-go-864df4cbf9-7kmr2       1/1     Running   0          4m38s
app-python-6c6854fdcf-xqw98   1/1     Running   0          3m10s
```