# Helm Deployment Guide

## Creating and Deploying a Helm Chart

1. Creating a New Helm Chart

To create a new Helm chart, use the following command:

```shell
helm create app-python
```

This command generates a default Helm chart structure. After creation, update `values.yaml` by replacing the default repository and tag with your repository name. Modify `templates/deployment.yaml` to set the `livenessProbe` and `readinessProbe` paths according to your application's health check requirements.

2. Installing the Helm Chart

To deploy the Helm chart to Kubernetes cluster, run:

```shell
helm install python app-python/ 
```

3. Verifying the Deployment

After installation, check if the pods and services are running correctly:

```shell
kubectl get pods,svc
NAME                                     READY   STATUS    RESTARTS        AGE
pod/python-app-python-854646957c-8rfv2   1/1     Running   0               22s
pod/python-app-python-854646957c-d4ctn   1/1     Running   0               22s
pod/python-app-python-854646957c-rj28w   1/1     Running   0               22s
pod/python-deployment-cf645b767-4r8jm    1/1     Running   1 (6d20h ago)   6d20h
pod/python-deployment-cf645b767-7j4hx    1/1     Running   1 (6d20h ago)   6d20h
pod/python-deployment-cf645b767-ksgct    1/1     Running   1 (6d20h ago)   6d20h

NAME                        TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/app-python          LoadBalancer   10.99.169.216    <pending>     8080:31152/TCP   6d20h
service/kubernetes          ClusterIP      10.96.0.1        <none>        443/TCP          6d20h
service/python-app-python   LoadBalancer   10.101.232.241   <pending>     8080:32465/TCP   22s
service/python-service      LoadBalancer   10.111.209.63    <pending>     8080:31584/TCP   6d20h
```

To expose and access the service, use:

```shell
minikube service python-app-python
|-----------|-------------------|-------------|---------------------------|
| NAMESPACE |       NAME        | TARGET PORT |            URL            |
|-----------|-------------------|-------------|---------------------------|
| default   | python-app-python | http/8080   | http://192.168.49.2:32465 |
|-----------|-------------------|-------------|---------------------------|
```

## Helm Hooks and Troubleshooting

1. Validating the Helm Chart

Before installing, ensure the Helm chart is correctly formatted:

```shell
helm lint app-python/
==> Linting app-python/
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed
```

2. Checking Pod Status After Installation

After installing the chart, check the running pods:

```shell
kubectl get po                    
NAME                                 READY   STATUS      RESTARTS        AGE
python-app-python-854646957c-96nrx   1/1     Running     0               36s
python-app-python-854646957c-jdtcc   1/1     Running     0               36s
python-app-python-854646957c-xt5ph   1/1     Running     0               36s
python-deployment-cf645b767-4r8jm    1/1     Running     1 (6d20h ago)   6d20h
python-deployment-cf645b767-7j4hx    1/1     Running     1 (6d20h ago)   6d20h
python-deployment-cf645b767-ksgct    1/1     Running     1 (6d20h ago)   6d20h
python-postinstall-hook              0/1     Completed   0               5m11s
python-preinstall-hook               0/1     Completed   0               4m26s
```

3. Understanding the `postinstall` Hook

To inspect the `postinstall` hook, run:

```shell
kubectl describe po python-postinstall-hook 
Name:             python-postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 25 Feb 2025 11:00:02 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
                  helm.sh/hook-delete-policy: hook-succeeded
Status:           Succeeded
IP:               10.244.0.17
IPs:
  IP:  10.244.0.17
Containers:
  post-install-container:
    Container ID:  docker://480fb65a949f72c3cfff5fef1c31aea023997a98d8b4d7d7ed8b09db264bd76e
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The post-install hook is running && sleep 15
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Tue, 25 Feb 2025 11:00:09 +0300
      Finished:     Tue, 25 Feb 2025 11:00:24 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-d2rd8 (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-d2rd8:
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
  Normal  Scheduled  7m54s  default-scheduler  Successfully assigned default/python-postinstall-hook to minikube
  Normal  Pulling    7m53s  kubelet            Pulling image "busybox"
  Normal  Pulled     7m47s  kubelet            Successfully pulled image "busybox" in 5.823s (5.824s including waiting)
  Normal  Created    7m47s  kubelet            Created container post-install-container
  Normal  Started    7m47s  kubelet            Started container post-install-container
```

4. Hook Deletion Policy

To automatically delete hooks after execution, ensure the following annotation is added to the hook template: `"helm.sh/hook-delete-policy": hook-succeeded`

After installing the Helm chart, confirm that hooks are removed:

```shell
kubectl get pods,svc
NAME                                     READY   STATUS      RESTARTS        AGE
pod/python-app-python-854646957c-96nrx   1/1     Running     0               5m43s
pod/python-app-python-854646957c-jdtcc   1/1     Running     0               5m43s
pod/python-app-python-854646957c-xt5ph   1/1     Running     0               5m43s
pod/python-deployment-cf645b767-4r8jm    1/1     Running     1 (6d20h ago)   6d20h
pod/python-deployment-cf645b767-7j4hx    1/1     Running     1 (6d20h ago)   6d20h
pod/python-deployment-cf645b767-ksgct    1/1     Running     1 (6d20h ago)   6d20h

NAME                        TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python          LoadBalancer   10.99.169.216   <pending>     8080:31152/TCP   6d21h
service/kubernetes          ClusterIP      10.96.0.1       <none>        443/TCP          6d21h
service/python-app-python   LoadBalancer   10.96.69.197    <pending>     8080:32276/TCP   5m44s
service/python-service      LoadBalancer   10.111.209.63   <pending>     8080:31584/TCP   6d20h

```
