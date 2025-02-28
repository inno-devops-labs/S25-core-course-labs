# Lab 10: Introduction to Helm

## Task 1: Helm Setup and Chart Creation

### Output of `kubectl get pods,svc`

```bash
NAME                                           READY       STATUS     RESTARTS AGE
pod/moscowtime-app-1740772199-5cc9dcd7d5-4g5c2 1/1         Running    0         2m1s
pod/moscowtime-app-1740772199-5cc9dcd7d5-jwqb7 1/1         Running    0         2m1s
pod/moscowtime-app-1740772199-5cc9dcd7d5-zrk7t 1/1         Running    0         2m1s

NAME                                TYPE            CLUSTER-IP      EXTERNAL-IP         PORT(S)         AGE
service/kubernetes                  ClusterIP       10.96.0.1       <none>              443/TCP         71m
service/moscowtime-app-1740772199   LoadBalancer    10.102.109.60   127.0.0.1           8000:30505/TCP  2m1s
```

### Steps to create a Helm chart

1. Created a Helm chart template for the application:

   ```bash
   helm create moscowtime-app
   ```

2. Modified the `values.yaml` file to update the following:

   - Set repository to `haidarjbeily/distroless-moscow-time-app`
   - Set tag to `latest`
   - Set service port to `8000`
   - Set service type to `LoadBalancer`
   - Set replicaCount to `3`

3. Installed the Helm chart:

   ```bash
   helm install moscowtime-app --generate-name
   ```

   **Output:**

   ```bash
    NAME: moscowtime-app-1740772199
    LAST DEPLOYED: Fri Feb 28 22:49:59 2025
    NAMESPACE: default
    STATUS: deployed
    REVISION: 1
    NOTES:

    1. Get the application URL by running these commands:
    NOTE: It may take a few minutes for the LoadBalancer IP to be available.
    You can watch its status by running 'kubectl get --namespace default svc -w moscowtime-app-1740772199'
    export SERVICE_IP=$(kubectl get svc --namespace default moscowtime-app-1740772199 --template "{{ range (index .status.loadBalancer.ingress 0) }}{{.}}{{ end }}")
    echo http://$SERVICE_IP:8000
   ```

4. Verified the installation by checking the Minikube dashboard:

   - Confirmed that all pods were running in the Workloads section
   - Verified that the service was properly configured
   - Ensured that all 3 replicas were healthy and running

5. Accessed the application using:

   ```bash
   minikube service moscowtime-app-1740772199
   ```

## Task 2: Helm Hooks

- **Output of `kubectl get pods,svc`:**

```bash
NAME                                            READY   STATUS      RESTARTS   AGE
pod/helm-hooks-moscowtime-app-6bb6fcc6c-hxfr5   1/1     Running     0          82s
pod/helm-hooks-moscowtime-app-6bb6fcc6c-s9cnj   1/1     Running     0          82s
pod/helm-hooks-moscowtime-app-6bb6fcc6c-sc2zs   1/1     Running     0          82s
pod/post-install-hook                           0/1     Completed   0          82s
pod/pre-install-hook                            0/1     Completed   0          108s

NAME                                TYPE           CLUSTER-IP    EXTERNAL-IP   PORT(S)          AGE
service/helm-hooks-moscowtime-app   LoadBalancer   10.98.7.143   <pending>     8000:31366/TCP   82s
service/kubernetes                  ClusterIP      10.96.0.1     <none>        443/TCP          12m
```

- **Output of `kubectl get po` After installing  completed:**

```bash
NAME                                        READY   STATUS      RESTARTS   AGE
helm-hooks-moscowtime-app-6bb6fcc6c-hxfr5   1/1     Running     0          39s
helm-hooks-moscowtime-app-6bb6fcc6c-s9cnj   1/1     Running     0          39s
helm-hooks-moscowtime-app-6bb6fcc6c-sc2zs   1/1     Running     0          39s
post-install-hook                           0/1     Completed   0          39s
pre-install-hook                            0/1     Completed   0          65s
```

- **Output of `kubectl describe po pre-install-hook`:**

```bash
Name:             pre-install-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sat, 01 Mar 2025 00:15:11 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.13
IPs:
  IP:  10.244.0.13
Containers:
  pre-install-hook:
    Container ID:  docker://ff3a1461abf8e12bb2e01b279f65d035220595d5004001e5350ac1a14d4f0727
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo Pre-install hook starting && sleep 20 && echo Pre-install hook complete
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Sat, 01 Mar 2025 00:15:15 +0300
      Finished:     Sat, 01 Mar 2025 00:15:35 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-v6ffg (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-v6ffg:
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
  Normal  Scheduled  2m53s  default-scheduler  Successfully assigned default/pre-install-hook to minikube
  Normal  Pulling    2m52s  kubelet            Pulling image "busybox"
  Normal  Pulled     2m49s  kubelet            Successfully pulled image "busybox" in 3.491s (3.491s including waiting). Image size: 4042190 bytes.
  Normal  Created    2m49s  kubelet            Created container: pre-install-hook
  Normal  Started    2m49s  kubelet            Started container pre-install-hook
```

- **Output of `kubectl describe po post-install-hook`:**

```bash
Name:             post-install-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sat, 01 Mar 2025 00:15:37 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.17
IPs:
  IP:  10.244.0.17
Containers:
  post-install-hook:
    Container ID:  docker://596714893bdcc1582ad17c009eabbf667a14f9294c801cee48a20d1a4323e4b9
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:498a000f370d8c37927118ed80afe8adc38d1edcbfc071627d17b25c88efcab0
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo Post-install hook starting && sleep 20 && echo Post-install hook complete
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Sat, 01 Mar 2025 00:15:41 +0300
      Finished:     Sat, 01 Mar 2025 00:16:01 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-4zbn6 (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-4zbn6:
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
  Normal  Scheduled  4m43s  default-scheduler  Successfully assigned default/post-install-hook to minikube
  Normal  Pulling    4m42s  kubelet            Pulling image "busybox"
  Normal  Pulled     4m39s  kubelet            Successfully pulled image "busybox" in 2.905s (2.905s including waiting). Image size: 4042190 bytes.
  Normal  Created    4m39s  kubelet            Created container: post-install-hook
  Normal  Started    4m39s  kubelet            Started container post-install-hook
```

- Implemented a hook delete policy to remove the hook once it has executed successfully by adding the annotation `"helm.sh/hook-delete-policy": hook-succeeded` to the hook's metadata section. This ensures that Kubernetes automatically cleans up the hook pod after successful execution, preventing resource accumulation.
