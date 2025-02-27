# Helm

## Task 1

In this task I:

- Installed `Helm`
- Created chart using `helm create python-app`
- Modified `values.yaml`, replaced `image.repository`, `image.tag` and `service.port` with my values
- Installed  Helm chart and checked services' health
  ![Dashboard](img/helm_python_app_dashboard.png)
- Accessed my app

  ```sh
  vm@vm /m/v/d/h/V/U/L/P/D/S/k8s (lab10)> minikube service python-app-1740647493
  |-----------|-----------------------|-------------|--------------|
  | NAMESPACE |         NAME          | TARGET PORT |     URL      |
  |-----------|-----------------------|-------------|--------------|
  | default   | python-app-1740647493 |             | No node port |
  |-----------|-----------------------|-------------|--------------|
  😿  service default/python-app-1740647493 has no node port
  ❗  Services [default/python-app-1740647493] have type "ClusterIP" not meant to be exposed, however for local development minikube allows you to access this !
  🏃  Starting tunnel for service python-app-1740647493.
  |-----------|-----------------------|-------------|------------------------|
  | NAMESPACE |         NAME          | TARGET PORT |          URL           |
  |-----------|-----------------------|-------------|------------------------|
  | default   | python-app-1740647493 |             | http://127.0.0.1:35949 |
  |-----------|-----------------------|-------------|------------------------|
  🎉  Opening service default/python-app-1740647493 in default browser...
  ```

  ![Demonstration](img/helm_python_app_demo.png)
- Provided required outputs

  ```sh
  vm@vm /m/v/d/h/V/U/L/P/D/S/k8s (lab10)> kubectl get pods,svc
  NAME                                         READY   STATUS    RESTARTS   AGE
  pod/python-app-1740647493-6644874668-vsqqh   1/1     Running   0          19m

  NAME                            TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
  service/kubernetes              ClusterIP   10.96.0.1       <none>        443/TCP    11h
  service/python-app-1740647493   ClusterIP   10.111.189.12   <none>        5000/TCP   19m
  ```

## Task 2

In this task I:

- Created `pre-install-hook.yaml` and `post-install-hook.yaml` in `template` directory
- Implemented simple logic in new files
- Reinstalled chart

  ```sh
  vm@vm /m/v/d/h/V/U/L/P/D/S/k8s (lab10)> helm delete python-app-1740653771
  release "python-app-1740653771" uninstalled
  vm@vm /m/v/d/h/V/U/L/P/D/S/k8s (lab10)> helm install python-app --generate-name
  NAME: python-app-1740653873
  LAST DEPLOYED: Thu Feb 27 13:57:53 2025
  NAMESPACE: default
  STATUS: deployed
  REVISION: 1
  NOTES:
  1. Get the application URL by running these commands:
    export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=python-app,app.kubernetes.io/instance=python-app-1740653873" -o jsonpath="{.items[0].metadata.name}")
    export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
    echo "Visit http://127.0.0.1:8080 to use your application"
    kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
  ```
- Troubleshoot hooks

  ```sh
  vm@vm /m/v/d/h/V/U/L/P/D/S/k8s (lab10)> helm lint python-app
  ==> Linting python-app
  [INFO] Chart.yaml: icon is recommended

  1 chart(s) linted, 0 chart(s) failed
  vm@vm /m/v/d/h/V/U/L/P/D/S/k8s (lab10)> helm install --dry-run helm-hooks python-app
  NAME: helm-hooks
  LAST DEPLOYED: Thu Feb 27 13:59:56 2025
  NAMESPACE: default
  STATUS: pending-install
  REVISION: 1
  HOOKS:
  ---
  # Source: python-app/templates/post-install-hook.yaml
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
      command: ['sh', '-c', 'echo "The post-install hook is running" && sleep 15' ]
    restartPolicy: Never
    terminationGracePeriodSeconds: 0
  ---
  # Source: python-app/templates/pre-install-hook.yaml
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
      command: ['sh', '-c', 'echo "The pre-install hook is running" && sleep 20' ]
    restartPolicy: Never
    terminationGracePeriodSeconds: 0
  ---
  # Source: python-app/templates/tests/test-connection.yaml
  apiVersion: v1
  kind: Pod
  metadata:
    name: "helm-hooks-python-app-test-connection"
    labels:
      helm.sh/chart: python-app-0.1.0
      app.kubernetes.io/name: python-app
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
        args: ['helm-hooks-python-app:5000']
    restartPolicy: Never
  MANIFEST:
  ---
  # Source: python-app/templates/serviceaccount.yaml
  apiVersion: v1
  kind: ServiceAccount
  metadata:
    name: helm-hooks-python-app
    labels:
      helm.sh/chart: python-app-0.1.0
      app.kubernetes.io/name: python-app
      app.kubernetes.io/instance: helm-hooks
      app.kubernetes.io/version: "1.16.0"
      app.kubernetes.io/managed-by: Helm
  automountServiceAccountToken: true
  ---
  # Source: python-app/templates/service.yaml
  apiVersion: v1
  kind: Service
  metadata:
    name: helm-hooks-python-app
    labels:
      helm.sh/chart: python-app-0.1.0
      app.kubernetes.io/name: python-app
      app.kubernetes.io/instance: helm-hooks
      app.kubernetes.io/version: "1.16.0"
      app.kubernetes.io/managed-by: Helm
  spec:
    type: ClusterIP
    ports:
      - port: 5000
        targetPort: http
        protocol: TCP
        name: http
    selector:
      app.kubernetes.io/name: python-app
      app.kubernetes.io/instance: helm-hooks
  ---
  # Source: python-app/templates/deployment.yaml
  apiVersion: apps/v1
  kind: Deployment
  metadata:
    name: helm-hooks-python-app
    labels:
      helm.sh/chart: python-app-0.1.0
      app.kubernetes.io/name: python-app
      app.kubernetes.io/instance: helm-hooks
      app.kubernetes.io/version: "1.16.0"
      app.kubernetes.io/managed-by: Helm
  spec:
    replicas: 1
    selector:
      matchLabels:
        app.kubernetes.io/name: python-app
        app.kubernetes.io/instance: helm-hooks
    template:
      metadata:
        labels:
          helm.sh/chart: python-app-0.1.0
          app.kubernetes.io/name: python-app
          app.kubernetes.io/instance: helm-hooks
          app.kubernetes.io/version: "1.16.0"
          app.kubernetes.io/managed-by: Helm
      spec:
        serviceAccountName: helm-hooks-python-app
        containers:
          - name: python-app
            image: "voronm1522/devops:python-app"
            imagePullPolicy: IfNotPresent
            ports:
              - name: http
                containerPort: 5000
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
    export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=python-app,app.kubernetes.io/instance=helm-hooks" -o jsonpath="{.items[0].metadata.name}")
    export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
    echo "Visit http://127.0.0.1:8080 to use your application"
    kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
  vm@vm /m/v/d/h/V/U/L/P/D/S/k8s (lab10)> kubectl get po
  NAME                                     READY   STATUS      RESTARTS   AGE
  postinstall-hook                         0/1     Completed   0          108s
  preinstall-hook                          0/1     Completed   0          2m11s
  python-app-1740653873-6549598f49-mbtv9   1/1     Running     0          108s
  ```
- Provided reqiured outputs

  ```sh
  vm@vm /m/v/d/h/V/U/L/P/D/S/k8s (lab10)> kubectl get po
  NAME                                     READY   STATUS      RESTARTS   AGE
  postinstall-hook                         0/1     Completed   0          4m7s
  preinstall-hook                          0/1     Completed   0          4m30s
  python-app-1740653873-6549598f49-mbtv9   1/1     Running     0          4m7s
  vm@vm /m/v/d/h/V/U/L/P/D/S/k8s (lab10)> kubectl describe po preinstall-hook
  Name:             preinstall-hook
  Namespace:        default
  Priority:         0
  Service Account:  default
  Node:             minikube/192.168.49.2
  Start Time:       Thu, 27 Feb 2025 13:57:53 +0300
  Labels:           <none>
  Annotations:      helm.sh/hook: pre-install
  Status:           Succeeded
  IP:               10.244.0.48
  IPs:
    IP:  10.244.0.48
  Containers:
    pre-install-container:
      Container ID:  docker://7d1edf2c3f94c238ecd79973b7db01799088bb2a001e038bf6c2b60a3049b91e
      Image:         busybox
      Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
      Port:          <none>
      Host Port:     <none>
      Command:
        sh
        -c
        echo "The pre-install hook is running" && sleep 20
      State:          Terminated
        Reason:       Completed
        Exit Code:    0
        Started:      Thu, 27 Feb 2025 13:57:54 +0300
        Finished:     Thu, 27 Feb 2025 13:58:14 +0300
      Ready:          False
      Restart Count:  0
      Environment:    <none>
      Mounts:
        /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-fwmwf (ro)
  Conditions:
    Type                        Status
    PodReadyToStartContainers   False 
    Initialized                 True 
    Ready                       False 
    ContainersReady             False 
    PodScheduled                True 
  Volumes:
    kube-api-access-fwmwf:
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
    Normal  Scheduled  4m41s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
    Normal  Pulled     4m41s  kubelet            Container image "busybox" already present on machine
    Normal  Created    4m40s  kubelet            Created container: pre-install-container
    Normal  Started    4m40s  kubelet            Started container pre-install-container
  vm@vm /m/v/d/h/V/U/L/P/D/S/k8s (lab10)> kubectl describe po postinstall-hook
  Name:             postinstall-hook
  Namespace:        default
  Priority:         0
  Service Account:  default
  Node:             minikube/192.168.49.2
  Start Time:       Thu, 27 Feb 2025 13:58:16 +0300
  Labels:           <none>
  Annotations:      helm.sh/hook: post-install
  Status:           Succeeded
  IP:               10.244.0.50
  IPs:
    IP:  10.244.0.50
  Containers:
    post-install-container:
      Container ID:  docker://aa23d4aaabc024ec537eb87a88391cc7c6f9a7a7184ff30ccba41d961b6607ab
      Image:         busybox
      Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
      Port:          <none>
      Host Port:     <none>
      Command:
        sh
        -c
        echo "The post-install hook is running" && sleep 15
      State:          Terminated
        Reason:       Completed
        Exit Code:    0
        Started:      Thu, 27 Feb 2025 13:58:19 +0300
        Finished:     Thu, 27 Feb 2025 13:58:34 +0300
      Ready:          False
      Restart Count:  0
      Environment:    <none>
      Mounts:
        /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-xd72d (ro)
  Conditions:
    Type                        Status
    PodReadyToStartContainers   False 
    Initialized                 True 
    Ready                       False 
    ContainersReady             False 
    PodScheduled                True 
  Volumes:
    kube-api-access-xd72d:
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
    Normal  Scheduled  4m22s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
    Normal  Pulling    4m21s  kubelet            Pulling image "busybox"
    Normal  Pulled     4m19s  kubelet            Successfully pulled image "busybox" in 1.576s (1.576s including waiting). Image size: 4269694 bytes.
    Normal  Created    4m19s  kubelet            Created container: post-install-container
    Normal  Started    4m19s  kubelet            Started container post-install-container
  ```
- Implemented a hook delete policy and restarted for checking

  ```sh
  vm@vm /m/v/d/h/V/U/L/P/D/S/k8s (lab10)> helm install python-app --generate-name
  NAME: python-app-1740654265
  LAST DEPLOYED: Thu Feb 27 14:04:25 2025
  NAMESPACE: default
  STATUS: deployed
  REVISION: 1
  NOTES:
  1. Get the application URL by running these commands:
    export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=python-app,app.kubernetes.io/instance=python-app-1740654265" -o jsonpath="{.items[0].metadata.name}")
    export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
    echo "Visit http://127.0.0.1:8080 to use your application"
    kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
  vm@vm /m/v/d/h/V/U/L/P/D/S/k8s (lab10)> kubectl get po
  NAME                                     READY   STATUS    RESTARTS   AGE
  python-app-1740654265-579bdd9f5f-6mfqc   1/1     Running   0          28s
  ```
- Provided required outputs

  ```sh
  vm@vm /m/v/d/h/V/U/L/P/D/S/k8s (lab10)> kubectl get pods,svc
  NAME                                         READY   STATUS    RESTARTS   AGE
  pod/python-app-1740654265-579bdd9f5f-6mfqc   1/1     Running   0          79s

  NAME                            TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)    AGE
  service/kubernetes              ClusterIP   10.96.0.1    <none>        443/TCP    12h
  service/python-app-1740654265   ClusterIP   10.96.1.32   <none>        5000/TCP   79s
  ```

## Bonus Task
