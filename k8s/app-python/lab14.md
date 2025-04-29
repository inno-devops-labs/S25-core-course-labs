# Lab14
## `kubectl get po, svc, sts, pvc`
```
NAME                                  READY   STATUS             RESTARTS         AGE
my-app-backend-0                      1/1     Running            0                113s
my-app-backend-1                      1/1     Running            0                46s
my-app-backend-2                      1/1     Running            0                3s
my-app-db-0                           1/1     Running            0                113s
my-app-frontend-5d4cf5c5dc-ppq2b      1/1     Running            0
NAME                      TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
kubernetes                ClusterIP   10.96.0.1        <none>        443/TCP          40h
my-app-backend-svc        ClusterIP   10.111.215.90    <none>        8080/TCP         2m53s
my-app-db-svc             ClusterIP   10.111.32.189    <none>        5432/TCP         2m53s
my-app-frontend-svc       NodePort    10.109.110.79    <none>        3000:31564/
NAME                              STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
my-app-db-pvc                     Bound    pvc-b0c7fb51-e57b-4f46-ba32-6e0e65af6761   1Gi        RWO            standard       <unset>                 3m17s
my-app-visits-pvc                 Bound    pvc-5742ba61-587d-48ee-b671-7e4764c42244   100Mi      RWO            standard       <unset>                 3m17s
visits-storage-my-app-backend-0   Bound    pvc-4d2c24b5-23fc-468d-a714-f2bddfcbbda3   100Mi      RWO            standard       <unset>                 3m17s
visits-storage-my-app-backend-1   Bound    pvc-5b88aaaa-8ee1-41ba-ad55-224db778c990   100Mi      RWO            standard       <unset>                 3m17s
visits-storage-my-app-backend-2   Bound    pvc-47adacc0-ab84-484f-b9bd-7d29e4f3d1bc   100Mi      RWO            standard       <unset>                 3m17s
NAME             READY   AGE
my-app-backend   3/3     3m57s
my-app-db        1/1     3m57s

```
## Content of visits
```
kubectl exec my-app-backend-0 -- cat /usr/local/app/visit
3
```
## Deletion of the pod and validation of the storage
```
kubectl delete pod my-app-backend-0
pod "my-app-backend-0" deleted
```
```
NAME                              STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
my-app-db-pvc                     Bound    pvc-b0c7fb51-e57b-4f46-ba32-6e0e65af6761   1Gi        RWO            standard       <unset>                 54m
my-app-visits-pvc                 Bound    pvc-5742ba61-587d-48ee-b671-7e4764c42244   100Mi      RWO            standard       <unset>                 54m
visits-storage-my-app-backend-0   Bound    pvc-4d2c24b5-23fc-468d-a714-f2bddfcbbda3   100Mi      RWO            standard       <unset>                 54m
visits-storage-my-app-backend-1   Bound    pvc-5b88aaaa-8ee1-41ba-ad55-224db778c990   100Mi      RWO            standard       <unset>                 54m
visits-storage-my-app-backend-2   Bound    pvc-47adacc0-ab84-484f-b9bd-7d29e4f3d1bc   100Mi      RWO            standard       <unset>                 54m
```
```
kubectl exec my-app-backend-0 -- cat /usr/local/app/visit
3
```
## Headless Service Action
```
Server:    10.118.0.12
Address 1: 10.118.0.12 kube-dns.kube-system.svc.cluster.local

Name:      my-app-backend-svc
Address 1: 10.111.215.90 my-app-backend-svc.default.svc.cluster.local
```
## How do the probes ensure the performance of the pods:
- **Liveness Probe**:
 - Checks that the container is working correctly. 
 - If the check fails 3 times in a row (default value), Kubernetes restarts under.
 - Example: Checking the endpoint `/visits` every 10 seconds after a 30-second delay.

- **Readiness Probe**:
- Determines whether the container is ready to receive traffic.
 - Pods with failed validation are excluded from load balancing.
 - Example: Checking the endpoint `/times` every 5 seconds.

**Why is it important for StatefulSet:**
1. **Data loss prevention**:
- Samples ensure that the pod does not receive traffic until it completes initialization (for example, connecting to a database).
2. **Replication stability**:
- For stateful applications (for example, databases), samples prevent writes to unsynchronized replicas.
## Ordering Guarantee and Parallel Operations

### Why guarantees of order are not needed
1. **Stateless-architecture**:
 - The backend does not store the state locally (all data is in PostgreSQL).
 - The replicas are identical and independent of each other.
2. **Horizontal scaling**:
 - There is no need for synchronization between the pods.
 - Requests are distributed randomly through the Service.

### Parallel start/stop
``yaml
podManagementPolicy: Parallel # Included in StatefulSet
