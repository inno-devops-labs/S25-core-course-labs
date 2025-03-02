# HELM

## Task 1 

```markdown
$ kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-57d59698db-8tn4x   1/1     Running   0          7m15s

NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/app-python   ClusterIP   10.100.118.66   <none>        5000/TCP   7m15s
service/kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP    9m41s
```

## Task 2

1. `kubectl get po`

```markdown
kubectl get po
NAME                                     READY   STATUS      RESTARTS   AGE
app-python-5756db44f-zchrr               1/1     Running     0          3m59s
helm-hooks-app-python-72dk4f92f-clkm2    1/1     Running     0          46s
postinstall-hook                         0/1     Completed   0          15s
preinstall-hook                          0/1     Completed   0          37s
```

2. `kubectl describe po preinstall-hook`

```markdown
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sat, 01 Mar 2025 20:26:00 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
                  helm.sh/hook-delete-policy: before-hook-creation,hook-succeeded
Status:           Succeeded
IP:               10.244.0.11
IPs:
  IP:  10.244.0.11
Containers:
  pre-install-container:
    Container ID:  docker://c9fa1dd261c1615fe900a9894052071621f2ce78beab06e74ce7a2a683ec55d9
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The pre-install hook is running && sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Sat, 01 Mar 2025 20:26:01 +0300
      Finished:     Sat, 01 Mar 2025 20:26:21 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-rs682 (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-rs682:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age    From               Message
  ----    ------     ----   ----               -------
  Normal  Scheduled  6m31s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     6m30s  kubelet            Container image "busybox" already present on machine
  Normal  Created    6m30s  kubelet            Created container pre-install-container
  Normal  Started    6m30s  kubelet            Started container pre-install-container

```

3. `kubectl describe po postinstall-hook`

```markdown
Name:             postinstall-hook               
Namespace:        default                        
Priority:         0                              
Service Account:  default                        
Node:             minikube/192.168.49.2          
Start Time:       Sat, 01 Mar 2025 20:26:22 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
                  helm.sh/hook-delete-policy: before-hook-creation,hook-succeeded
Status:           Succeeded
IP:               10.244.0.12
IPs:
  IP:  10.244.0.12
Containers:
  post-install-container:
    Container ID:  docker://428af4f7cf077de10ef5ead5847e3025c085409416fca73afd789f1e1b2d93ac
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
      Started:      Sat, 01 Mar 2025 20:26:26 +0300
      Finished:     Sat, 01 Mar 2025 20:26:41 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-wjf4b (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-wjf4b:
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
  Normal  Scheduled  7m48s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    7m47s  kubelet            Pulling image "busybox"
  Normal  Pulled     7m44s  kubelet            Successfully pulled image "busybox" in 2.782s (2.782s including waiting)
  Normal  Created    7m44s  kubelet            Created container post-install-container
  Normal  Started    7m44s  kubelet            Started container post-install-container
```