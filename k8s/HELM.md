# HELM APPLICATION
## Helm instalation

1. To create helm chart I use the command:
```bash
   helm create my-app
```
2. After creating the template of the HELM chart I configure it updating the structure and removing all unnecessary files
The strcuture is
```bash
app-python/
├── Chart.yaml
├── values.yaml
└── templates/
    ├── db/
    │   ├── configmap.yaml
    │   ├── deployment.yaml
    │   ├── service.yaml
    │   └── secrets.yaml
    ├── backend/
    │   ├── deployment.yaml
    │   └── service.yaml
    └── frontend/
        ├── deployment.yaml
        └── service.yaml
```
As I have 3-layer architecture, I use 3 folders with service. deployment for each part of my application, and configMap with secrets for database.
3. To execute the helm chart, I use the command
```bash
helm install my-app ./app-python
```
4. Verification that all pods and services are accessible:
```bash
   kubectl get pods
NAME                               READY   STATUS    RESTARTS      AGE
my-app-backend-85c865f55c-lwdbq    1/1     Running   0             101s
my-app-db-6564759ccf-5qrhv         1/1     Running   0             101s
my-app-frontend-5d4cf5c5dc-tm25n   1/1     Running   1 (26s ago)   101s

```
```bash
NAME                  TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
kubernetes            ClusterIP   10.96.0.1        <none>        443/TCP          5h19m
my-app-backend-svc    ClusterIP   10.101.79.156    <none>        8080/TCP         2m50s
my-app-db-svc         ClusterIP   10.106.199.175   <none>        5432/TCP         2m50s
my-app-frontend-svc   NodePort    10.99.84.170     <none>        3000:32303/TCP   2m50s
```
5. Using minikube dashboard I can ensure that all minikube services are health
![image](https://github.com/user-attachments/assets/6ab57715-b9db-4fb9-95f4-4dac03354579)

6. Using `minikube service my-app-frontend-svc` I can run the service in the browser (I use frontend, because it is not isolated)
As I see, everything is accessible
![image](https://github.com/user-attachments/assets/ea61b924-ee5b-4297-8b96-f38aa8a3914c)

## Hooks
1. I update the structure of Chart and make the directory for hooks and put `pre-install-hook.yaml` and `post-install-hook.yaml` inside it.
2. Then I reinstall the helm chart
```bash
helm uninstall my-app
helm install my-app ./app-python
```
3. Checking pods:
```bash
NAME                               READY   STATUS      RESTARTS   AGE
my-app-backend-85c865f55c-qhn7f    1/1     Running     0          88s
my-app-db-6564759ccf-7g648         1/1     Running     0          88s
my-app-frontend-5d4cf5c5dc-jdpkc   1/1     Running     0          88s
my-app-post-install-hook-j277z     0/1     Completed   0          87s
my-app-pre-install-hook-lrz2d      0/1     Completed   0          2m2s
```
```
kubectl describe po my-app-post-install-hook-j277z
Name:             my-app-post-install-hook-j277z
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.85.2
Start Time:       Sun, 20 Apr 2025 18:29:46 +0200
Labels:           batch.kubernetes.io/controller-uid=d652d61a-27a1-4652-bc57-32217046fc3e
                  batch.kubernetes.io/job-name=my-app-post-install-hook
                  controller-uid=d652d61a-27a1-4652-bc57-32217046fc3e
                  job-name=my-app-post-install-hook
Annotations:      <none>
Status:           Succeeded
IP:               10.244.0.76
IPs:
  IP:           10.244.0.76
Controlled By:  Job/my-app-post-install-hook
Containers:
  post-install:
    Container ID:  docker://6ae6aae3d249a8a4b8122a653d956f9fda159600b460cb629ed327c19e690f2a
    Image:         alpine:3.18
    Image ID:      docker-pullable://alpine@sha256:de0eb0b3f2a47ba1eb89389859a9bd88b28e82f5826b6969ad604979713c2d4f
    Port:          <none>
    Host Port:     <none>
    Command:
      /bin/sh
      -c
      sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Sun, 20 Apr 2025 18:29:54 +0200
      Finished:     Sun, 20 Apr 2025 18:30:15 +0200
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-g6spf (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-g6spf:
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
  Normal  Scheduled  3m22s  default-scheduler  Successfully assigned default/my-app-post-install-hook-j277z to minikube
  Normal  Pulled     3m14s  kubelet            Container image "alpine:3.18" already present on machine
  Normal  Created    3m14s  kubelet            Created container: post-install
  Normal  Started    3m13s  kubelet            Started container post-install
```
```bash
kubectl describe po my-app-pre-install-hook-lrz2d 
Name:             my-app-pre-install-hook-lrz2d
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.85.2
Start Time:       Sun, 20 Apr 2025 18:29:11 +0200
Labels:           batch.kubernetes.io/controller-uid=a2a4fd0c-9306-4aa6-b982-3aafd8d2dcda
                  batch.kubernetes.io/job-name=my-app-pre-install-hook
                  controller-uid=a2a4fd0c-9306-4aa6-b982-3aafd8d2dcda
                  job-name=my-app-pre-install-hook
Annotations:      <none>
Status:           Succeeded
IP:               10.244.0.73
IPs:
  IP:           10.244.0.73
Controlled By:  Job/my-app-pre-install-hook
Containers:
  pre-install:
    Container ID:  docker://8ed9a492d3650d70ea18b884a5f367a1975f7ad515fe9f3a7e5e1a5f6b57d05e
    Image:         alpine:3.18
    Image ID:      docker-pullable://alpine@sha256:de0eb0b3f2a47ba1eb89389859a9bd88b28e82f5826b6969ad604979713c2d4f
    Port:          <none>
    Host Port:     <none>
    Command:
      /bin/sh
      -c
      sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Sun, 20 Apr 2025 18:29:17 +0200
      Finished:     Sun, 20 Apr 2025 18:29:38 +0200
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-lpxfr (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-lpxfr:
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
  Normal  Scheduled  4m58s  default-scheduler  Successfully assigned default/my-app-pre-install-hook-lrz2d to minikube
  Normal  Pulled     4m53s  kubelet            Container image "alpine:3.18" already present on machine
  Normal  Created    4m53s  kubelet            Created container: pre-install
  Normal  Started    4m51s  kubelet            Started container pre-install
```
5. After that I implemented hook delete policy entiring into the hooks yaml parameter `"helm.sh/hook-delete-policy": hook-succeeded`
 
