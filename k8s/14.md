# Lab 14: StatefulSet Implementation and Exploration

## Task 1: Implement StatefulSet in Helm Chart

Renamed `deployment.yml` to `statefulset.yml` with changes:
- Added `serviceName` for headless service
- Added `volumeClaimTemplates` for persistent storage
- Added `podManagementPolicy: Parallel`

Tested and deployed:
```bash
helm install app-python ./k8s/app-python
```

## Task 2: StatefulSet Exploration and Optimization

### 1. Resource Overview

```bash
kubectl get pods,sts,svc,pvc
```

```text
NAME                                         READY   STATUS    RESTARTS       AGE
pod/app-python-0                             1/1     Running   0              44s
pod/app-python-1                             1/1     Running   0              42s
pod/app-python-2                             1/1     Running   0              31s
pod/python-app-app-python-789896d4c5-cm8rv   1/1     Running   112 (8h ago)   35d
pod/python-app-app-python-789896d4c5-dkqzd   1/1     Running   75 (8h ago)    35d
pod/python-app-app-python-789896d4c5-tv79p   1/1     Running   79 (8h ago)    35d

NAME                          READY   AGE
statefulset.apps/app-python   3/3     44s

NAME                            TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/app-python              ClusterIP   10.96.239.140   <none>        5000/TCP   45s
service/kubernetes              ClusterIP   10.96.0.1       <none>        443/TCP    35d
service/python-app-app-python   ClusterIP   10.96.144.248   <none>        5000/TCP   35d

NAME                                      STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
persistentvolumeclaim/data-app-python-0   Bound    pvc-1edaa608-7929-4e25-8a96-9242cc2f98cd   1Gi        RWO           standard       20m
persistentvolumeclaim/data-app-python-1   Bound    pvc-5459f0f3-7736-4af8-9e75-f917808992d8   1Gi        RWO           standard       20m
persistentvolumeclaim/data-app-python-2   Bound    pvc-49af605a-9e9c-484a-bf4d-44469e60a0a4   1Gi        RWO           standard       20m
```

Accessed application:
```bash
kubectl port-forward svc/app-python 8082:5000
```

### 2. Visit Counters

```bash
kubectl exec app-python-0 -- cat /app/data/visits.txt
```
```text
98
```

```bash
kubectl exec app-python-1 -- cat /app/data/visits.txt
```
```text
86
```

```bash
kubectl exec app-python-2 -- cat /app/data/visits.txt
```
```text
85
```

**Explanation**: Each pod has its own counter stored in a separate PVC, causing different values across pods.

### 3. Persistent Storage Validation

Deleted pod:
```bash
kubectl delete pod app-python-0
```

Verified data persistence:
```bash
kubectl exec app-python-0 -- cat /app/data/visits.txt
```
```text
98
```

This confirms StatefulSets maintain the same PVC when pods are recreated.

### 4. Headless Service Access

```bash
dm@DESKTOP-85MKAD8:/mnt/d/github_repos/S25-core-course-labs$ kubectl exec -it app-python-0 -- nslookup app-python-1.app-python
```

```text
;; Got recursion not available from 10.96.0.10
;; Got recursion not available from 10.96.0.10
;; Got recursion not available from 10.96.0.10
;; Got SERVFAIL reply from 10.96.0.10
Server:         10.96.0.10
Address:        10.96.0.10#53

** server can't find app-python-1.app-python: SERVFAIL

command terminated with exit code 1
```

DNS resolution failed (SERVFAIL). Full DNS names like app-python-1.app-python-headless.default.svc.cluster.local were not resolved.
The issue is related to CoreDNS or service configuration, not the StatefulSet itself.



### 5. Monitoring & Alerts

Added probes to the StatefulSet:
```yaml
livenessProbe:
  httpGet:
    path: /
    port: http
readinessProbe:
  httpGet:
    path: /
    port: http
```

**Health assurance**:
- Liveness probe restarts failing pods
- Readiness probe removes unready pods from service

**Critical for stateful apps because**:
- Prevents data corruption from unhealthy pods
- Avoids sending traffic to initializing pods

### 6. Parallel Pod Management

Implemented with:
```yaml
podManagementPolicy: Parallel
```

**Why ordering is unnecessary**:
- Independent pod operation
- No inter-pod dependencies
- No leader/follower relationships
- No sequential initialization requirements