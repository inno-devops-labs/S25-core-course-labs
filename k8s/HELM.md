![alt text](image-1.png)

```
lekski@LAPTOP-EA8M0FT5:/mnt/c/Users/Honor/Desktop/S25-core-course-labs$ curl python-web-app.local
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="./static/css/main.css">
        <title>Moscow</title>
    </head>
    <body>
        <div class="time">
            <h1 id='main_text'>MSC Time</h1>
            <h1 id='msc-time'>24-02-2025 12:28:41</h1>
        </div>
    </body>
</html>
```


```
NAME                            READY   STATUS    RESTARTS   AGE
pod/web-apps-6c5469f97d-j8wfw   1/1     Running   0          6m2s

NAME                 TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
service/kubernetes   ClusterIP   10.96.0.1        <none>        443/TCP    10m
service/web-apps     ClusterIP   10.106.108.139   <none>        8000/TCP   6m2s
```


```
lekski@LAPTOP-EA8M0FT5:/mnt/c/Users/Honor/Desktop/S25-core-course-labs/k8s$ helm install helm-hooks-release ./web-apps
NAME: helm-hooks-release
LAST DEPLOYED: Mon Feb 24 13:43:39 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  http://python-web-app.local/
```

```
lekski@LAPTOP-EA8M0FT5:/mnt/c/Users/Honor/Desktop/S25-core-course-labs/k8s$ kubectl get po
NAME                                           READY   STATUS    RESTARTS   AGE
helm-hooks-release-web-apps-67688955f8-q6hwj   1/1     Running   0          4m29s
web-apps-6c5469f97d-j8wfw                      1/1     Running   0          83m
```

Часть 2
```
lekski@LAPTOP-EA8M0FT5:/mnt/c/Users/Honor/Desktop/S25-core-course-labs/k8s$ kubectl get po
NAME                                           READY   STATUS      RESTARTS   AGE
helm-hooks-release-web-apps-67688955f8-pvchc   1/1     Running     0          8m38s
my-web-apps-84bf78bd7f-t5nsz                   0/1     Running     0          12s
postinstall-hook                               0/1     Completed   0          8m37s
preinstall-hook                                0/1     Completed   0          35s
```
```
lekski@LAPTOP-EA8M0FT5:/mnt/c/Users/Honor/Desktop/S25-core-course-labs/k8s$ kubectl describe po postinstall-hook
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Mon, 24 Feb 2025 14:25:35 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.34
IPs:
  IP:  10.244.0.34
Containers:
  post-install-container:
    Container ID:  docker://4c2bba5ca78b05b342fa1c484491bb79c3c1da40f43076cbfd18b62546e8491c
    Image:         busybox:latest
    Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The post-install hook is running && sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Mon, 24 Feb 2025 14:25:39 +0300
      Finished:     Mon, 24 Feb 2025 14:25:59 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-7n657 (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False
  Initialized                 True
  Ready                       False
  ContainersReady             False
  PodScheduled                True
Volumes:
  kube-api-access-7n657:
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
  Normal  Scheduled  86s   default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    85s   kubelet            Pulling image "busybox:latest"
  Normal  Pulled     83s   kubelet            Successfully pulled image "busybox:latest" in 2.862s (2.862s including waiting). Image size: 4269694 bytes.
  Normal  Created    83s   kubelet            Created container: post-install-container
  Normal  Started    83s   kubelet            Started container post-install-container
```

```
lekski@LAPTOP-EA8M0FT5:/mnt/c/Users/Honor/Desktop/S25-core-course-labs/k8s$ kubectl describe po preinstall-hook
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Mon, 24 Feb 2025 14:25:10 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.32
IPs:
  IP:  10.244.0.32
Containers:
  pre-install-container:
    Container ID:  docker://175e17277cd7ebbb1c39ba02ab6c0cc60e4534647f6a1b475ad481fac4854cd8
    Image:         busybox:latest
    Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The pre-install hook is running && sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Mon, 24 Feb 2025 14:25:11 +0300
      Finished:     Mon, 24 Feb 2025 14:25:31 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-ckmxx (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False
  Initialized                 True
  Ready                       False
  ContainersReady             False
  PodScheduled                True
Volumes:
  kube-api-access-ckmxx:
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
  Normal  Scheduled  3m39s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     3m39s  kubelet            Container image "busybox:latest" already present on machine
  Normal  Created    3m39s  kubelet            Created container: pre-install-container
  Normal  Started    3m39s  kubelet            Started container pre-install-container
```

```
lekski@LAPTOP-EA8M0FT5:/mnt/c/Users/Honor/Desktop/S25-core-course-labs/k8s$ kubectl get pods,svc
NAME                                               READY   STATUS      RESTARTS   AGE
pod/helm-hooks-release-web-apps-67688955f8-pvchc   1/1     Running     0          9m2s
pod/my-web-apps-84bf78bd7f-t5nsz                   1/1     Running     0          36s
pod/postinstall-hook                               0/1     Completed   0          9m1s
pod/preinstall-hook                                0/1     Completed   0          59s

NAME                                  TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
service/helm-hooks-release-web-apps   ClusterIP   10.97.254.224    <none>        8000/TCP   9m2s
service/kubernetes                    ClusterIP   10.96.0.1        <none>        443/TCP    134m
service/my-web-apps                   ClusterIP   10.103.98.88     <none>        8000/TCP   36s
service/web-apps                      ClusterIP   10.106.108.139   <none>        8000/TCP   129m
```


Бонусное задание: 
Я создал дополнительную helm конфигурацию для моего экстра веб приложения на golang. 
Затем по гайду приведенному в задании создал mylibchart, указал тип как library, а так же использовал шаблок для _labels.tlp из гайда. 

Затем в самих веб приложениях я добавил зависимости от mylibchart и в метаданных указал include "mylibchart.labels" . | nindent 4. 
После этого я проверил корректно работы mylibchart используя helm template ./golang-web-app --debug для обеих веб приложения и проверил строку с метаданными на корректность вывода. Вывод этой команды вы можете увидеть ниже, как видно ошибок нет и метаданные выводятся корректно, что нам говорит о правильной работе mylibchart. 

```
lekski@LAPTOP-EA8M0FT5:/mnt/c/Users/Honor/Desktop/S25-core-course-labs/k8s$ helm template ./web-apps --debug
install.go:225: 2025-02-26 11:39:23.072574783 +0300 MSK m=+1.947332066 [debug] Original chart version: ""
install.go:242: 2025-02-26 11:39:23.077091284 +0300 MSK m=+1.951848567 [debug] CHART PATH: /mnt/c/Users/Honor/Desktop/S25-core-course-labs/k8s/web-apps

---
# Source: web-apps/templates/serviceaccount.yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: release-name-web-apps
  labels:
    helm.sh/chart: web-apps-0.1.0
    app.kubernetes.io/name: web-apps
    app.kubernetes.io/instance: release-name
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
automountServiceAccountToken: true
---
# Source: web-apps/templates/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: release-name-web-apps
  labels:
    app.kubernetes.io/name: web-apps
    app.kubernetes.io/instance: release-name
    app.kubernetes.io/version: 1.16.0
    app.kubernetes.io/managed-by: Helm
spec:
  type: ClusterIP
  ports:
    - port: 8000
      targetPort: 8000
      protocol: TCP
      name: http
  selector:
    app.kubernetes.io/name: web-apps
    app.kubernetes.io/instance: release-name
---
# Source: web-apps/templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: release-name-web-apps
  labels:
    app.kubernetes.io/name: web-apps
    app.kubernetes.io/instance: release-name
    app.kubernetes.io/version: 1.16.0
    app.kubernetes.io/managed-by: Helm
spec:
  replicas: 1
  selector:
    matchLabels:
      app.kubernetes.io/name: web-apps
      app.kubernetes.io/instance: release-name
  template:
    metadata:
      labels:
        helm.sh/chart: web-apps-0.1.0
        app.kubernetes.io/name: web-apps
        app.kubernetes.io/instance: release-name
        app.kubernetes.io/version: "1.16.0"
        app.kubernetes.io/managed-by: Helm
    spec:
      serviceAccountName: release-name-web-apps
      containers:
        - name: web-apps
          image: "lekski/python-web-app:latest"
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
---
# Source: web-apps/templates/ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: release-name-web-apps
  labels:
    helm.sh/chart: web-apps-0.1.0
    app.kubernetes.io/name: web-apps
    app.kubernetes.io/instance: release-name
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
spec:
  rules:
    - host: "python-web-app.local"
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: release-name-web-apps
                port:
                  number: 8000
---
# Source: web-apps/templates/post-install-hook.yaml
apiVersion: v1
kind: Pod
metadata:
   name: postinstall-hook
   annotations:
       "helm.sh/hook": "post-install"
       # "helm.sh/hook-delete-policy": hook-succeeded
spec:
  containers:
  - name: post-install-container
    image: busybox:latest
    imagePullPolicy: Always
    command: ['sh', '-c', 'echo The post-install hook is running && sleep 20' ]
  restartPolicy: Never
  terminationGracePeriodSeconds: 0
---
# Source: web-apps/templates/pre-install-hook.yaml
apiVersion: v1
kind: Pod
metadata:
   name: preinstall-hook
   annotations:
       "helm.sh/hook": "pre-install"
       # "helm.sh/hook-delete-policy": hook-succeeded
spec:
  containers:
  - name: pre-install-container
    image: busybox:latest
    imagePullPolicy: IfNotPresent
    command: ['sh', '-c', 'echo The pre-install hook is running && sleep 20' ]
  restartPolicy: Never
  terminationGracePeriodSeconds: 0
---
# Source: web-apps/templates/tests/test-connection.yaml
apiVersion: v1
kind: Pod
metadata:
  name: "release-name-web-apps-test-connection"
  labels:
    helm.sh/chart: web-apps-0.1.0
    app.kubernetes.io/name: web-apps
    app.kubernetes.io/instance: release-name
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
  annotations:
    "helm.sh/hook": test
spec:
  containers:
    - name: wget
      image: busybox
      command: ['wget']
      args: ['release-name-web-apps:8000']
  restartPolicy: Never
lekski@LAPTOP-EA8M0FT5:/mnt/c/Users/Honor/Desktop/S25-core-course-labs/k8s$ helm template ./golang-web-app --debug
install.go:225: 2025-02-26 11:39:59.338521641 +0300 MSK m=+1.521960738 [debug] Original chart version: ""
install.go:242: 2025-02-26 11:39:59.34224403 +0300 MSK m=+1.525683127 [debug] CHART PATH: /mnt/c/Users/Honor/Desktop/S25-core-course-labs/k8s/golang-web-app

---
# Source: golang-web-app/templates/serviceaccount.yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: release-name-golang-web-app
  labels:
    helm.sh/chart: golang-web-app-0.1.0
    app.kubernetes.io/name: golang-web-app
    app.kubernetes.io/instance: release-name
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
automountServiceAccountToken: true
---
# Source: golang-web-app/templates/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: release-name-golang-web-app
  labels:
    app.kubernetes.io/name: golang-web-app
    app.kubernetes.io/instance: release-name
    app.kubernetes.io/version: 1.16.0
    app.kubernetes.io/managed-by: Helm
spec:
  type: ClusterIP
  ports:
    - port: 8000
      targetPort: 8000
      protocol: TCP
      name: http
  selector:
    app.kubernetes.io/name: golang-web-app
    app.kubernetes.io/instance: release-name
---
# Source: golang-web-app/templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: release-name-golang-web-app
  labels:
    app.kubernetes.io/name: golang-web-app
    app.kubernetes.io/instance: release-name
    app.kubernetes.io/version: 1.16.0
    app.kubernetes.io/managed-by: Helm
spec:
  replicas: 1
  selector:
    matchLabels:
      app.kubernetes.io/name: golang-web-app
      app.kubernetes.io/instance: release-name
  template:
    metadata:
      labels:
        helm.sh/chart: golang-web-app-0.1.0
        app.kubernetes.io/name: golang-web-app
        app.kubernetes.io/instance: release-name
        app.kubernetes.io/version: "1.16.0"
        app.kubernetes.io/managed-by: Helm
    spec:
      serviceAccountName: release-name-golang-web-app
      containers:
        - name: golang-web-app
          image: "lekski/golang-web-app:latest"
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
---
# Source: golang-web-app/templates/ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: release-name-golang-web-app
  labels:
    helm.sh/chart: golang-web-app-0.1.0
    app.kubernetes.io/name: golang-web-app
    app.kubernetes.io/instance: release-name
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
spec:
  rules:
    - host: "golang-web-app.local"
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: release-name-golang-web-app
                port:
                  number: 8000
---
# Source: golang-web-app/templates/tests/test-connection.yaml
apiVersion: v1
kind: Pod
metadata:
metadata:
  name: "release-name-golang-web-app-test-connection"
  labels:
    helm.sh/chart: golang-web-app-0.1.0
    app.kubernetes.io/name: golang-web-app
    app.kubernetes.io/instance: release-name
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
  annotations:
metadata:
  name: "release-name-golang-web-app-test-connection"
  labels:
  name: "release-name-golang-web-app-test-connection"
  labels:
    helm.sh/chart: golang-web-app-0.1.0
    app.kubernetes.io/name: golang-web-app
    app.kubernetes.io/instance: release-name
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
  annotations:
    "helm.sh/hook": test
spec:
  containers:
    - name: wget
      image: busybox
      command: ['wget']
      args: ['release-name-golang-web-app:8000']
  restartPolicy: Never
```