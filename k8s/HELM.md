# Helm Chart Documentation

## Lab 10: Introduction to Helm

### Task 1: Helm Setup and Chart Creation

#### Cluster Verification
```bash
kubectl cluster-info
# Kubernetes control plane is running at https://127.0.0.1:60591
# CoreDNS is running at https://127.0.0.1:60591/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

minikube status
# minikube
# type: Control Plane
# host: Running
# kubelet: Running
# apiserver: Running
# kubeconfig: Configured
# docker-env: in-use


kubectl get pods,svc
# NAME                          READY   STATUS    RESTARTS   AGE
# pod/my-app-754689f9d6-z2b2n   1/1     Running   0          40s
#
# NAME                 TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
# service/kubernetes   ClusterIP   10.96.0.1        <none>        443/TCP   4m9s
# service/my-app       ClusterIP   10.111.112.184   <none>        80/TCP    40s

minikube service my-app --url
# http://127.0.0.1:63107

kubectl get po
NAME                      READY   STATUS    RESTARTS   AGE
my-app-754689f9d6-x2tx9   1/1     Running   0          59s

kubectl describe po <preinstall_hook_name>
Name:             my-app-754689f9d6-x2tx9
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sun, 27 Apr 2025 18:36:08 +0300
Labels:           app.kubernetes.io/instance=my-app
                  app.kubernetes.io/name=my-app
                  pod-template-hash=754689f9d6
Annotations:      <none>
Status:           Running
IP:               10.244.0.7
IPs:
  IP:           10.244.0.7
Controlled By:  ReplicaSet/my-app-754689f9d6
Containers:
  my-app:
    Container ID:   docker://483bf58ab65d1f213d9e12f02dacc47b78892161067b41b335f6dbc25ba6cc3a
    Image:          nginx:latest
    Image ID:       docker-pullable://nginx@sha256:5ed8fcc66f4ed123c1b2560ed708dc148755b6e4cbd8b943fab094f2c6bfa91e
    Port:           80/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Sun, 27 Apr 2025 18:36:12 +0300
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-z6tkf (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       True 
  ContainersReady             True 
  PodScheduled                True 
Volumes:
  kube-api-access-z6tkf:
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
  Normal  Scheduled  15m   default-scheduler  Successfully assigned default/my-app-754689f9d6-x2tx9 to minikube
  Normal  Pulling    15m   kubelet            Pulling image "nginx:latest"
  Normal  Pulled     15m   kubelet            Successfully pulled image "nginx:latest" in 1.431s (2.848s including waiting). Image size: 197741282 bytes.
  Normal  Created    15m   kubelet            Created container: my-app
  Normal  Started    15m   kubelet            Started container my-app

kubectl describe po <postinstall_hook_name>
Name:             my-app-754689f9d6-x2tx9
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sun, 27 Apr 2025 18:36:08 +0300
Labels:           app.kubernetes.io/instance=my-app
                  app.kubernetes.io/name=my-app
                  pod-template-hash=754689f9d6
Annotations:      <none>
Status:           Running
IP:               10.244.0.7
IPs:
  IP:           10.244.0.7
Controlled By:  ReplicaSet/my-app-754689f9d6
Containers:
  my-app:
    Container ID:   docker://483bf58ab65d1f213d9e12f02dacc47b78892161067b41b335f6dbc25ba6cc3a
    Image:          nginx:latest
    Image ID:       docker-pullable://nginx@sha256:5ed8fcc66f4ed123c1b2560ed708dc148755b6e4cbd8b943fab094f2c6bfa91e
    Port:           80/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Sun, 27 Apr 2025 18:36:12 +0300
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-z6tkf (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       True 
  ContainersReady             True 
  PodScheduled                True 
Volumes:
  kube-api-access-z6tkf:
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
  Normal  Scheduled  16m   default-scheduler  Successfully assigned default/my-app-754689f9d6-x2tx9 to minikube
  Normal  Pulling    16m   kubelet            Pulling image "nginx:latest"
  Normal  Pulled     16m   kubelet            Successfully pulled image "nginx:latest" in 1.431s (2.848s including waiting). Image size: 197741282 bytes.
  Normal  Created    16m   kubelet            Created container: my-app
  Normal  Started    16m   kubelet            Started container my-app
