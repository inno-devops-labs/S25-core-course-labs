# Helm Deployment

## Task 1: Basic Helm Chart Deployment

The application has been deployed using Helm with a custom chart. The chart includes:
- Deployment configuration with resource limits
- LoadBalancer service configuration
- Health check probes configured for the `/time` endpoint

### Current Status of Pods and Services

```bash
NAME                          READY   STATUS    RESTARTS   AGE
moscow-time-5cbccbbfb-2vstn   1/1     Running   0          2m34s

NAME                  TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/kubernetes    ClusterIP      10.96.0.1        <none>        443/TCP          4h25m
service/moscow-time   LoadBalancer   10.107.208.114   <pending>     8000:32287/TCP   8s
```

The deployment is running successfully with one replica, and the service is exposed as a LoadBalancer on port 8000.

## Task 2: Helm Chart Hooks

The chart has been enhanced with pre-install and post-install hooks:

### Hook Implementation
- Pre-install hook: Executes before the main deployment, sleeps for 20 seconds
- Post-install hook: Executes after the main deployment, sleeps for 20 seconds
- Both hooks use the `hook-succeeded` delete policy for automatic cleanup

### Hook Details

Complete execution log from Helm debug output:

Pre-install hook lifecycle:
```bash
[debug] creating 1 resource(s)
[debug] Watching for changes to Pod moscow-time-pre-install-hook with timeout of 5m0s
[debug] Add/Modify event for moscow-time-pre-install-hook: ADDED
[debug] Pod moscow-time-pre-install-hook pending
[debug] Add/Modify event for moscow-time-pre-install-hook: MODIFIED
[debug] Pod moscow-time-pre-install-hook pending
[debug] Add/Modify event for moscow-time-pre-install-hook: MODIFIED
[debug] Pod moscow-time-pre-install-hook running
[debug] Pod moscow-time-pre-install-hook succeeded
[debug] Starting delete for "moscow-time-pre-install-hook" Pod
[debug] beginning wait for 1 resources to be deleted with timeout of 5m0s
```

Post-install hook lifecycle:
```bash
[debug] creating 1 resource(s)
[debug] Watching for changes to Pod moscow-time-post-install-hook with timeout of 5m0s
[debug] Add/Modify event for moscow-time-post-install-hook: ADDED
[debug] Pod moscow-time-post-install-hook pending
[debug] Add/Modify event for moscow-time-post-install-hook: MODIFIED
[debug] Pod moscow-time-post-install-hook pending
[debug] Pod moscow-time-post-install-hook running
[debug] Pod moscow-time-post-install-hook succeeded
[debug] Starting delete for "moscow-time-post-install-hook" Pod
[debug] beginning wait for 1 resources to be deleted with timeout of 5m0s
```

Hook Configurations:

Pre-install hook:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: moscow-time-pre-install-hook
  annotations:
    "helm.sh/hook": pre-install
    "helm.sh/hook-weight": "-5"
    "helm.sh/hook-delete-policy": hook-succeeded
spec:
  containers:
  - name: pre-install
    image: busybox
    command: ['sh', '-c', 'echo Starting pre-install hook && sleep 20 && echo Pre-install hook completed']
  restartPolicy: Never
```

Post-install hook:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: moscow-time-post-install-hook
  annotations:
    "helm.sh/hook": post-install
    "helm.sh/hook-weight": "5"
    "helm.sh/hook-delete-policy": hook-succeeded
spec:
  containers:
  - name: post-install
    image: busybox
    command: ['sh', '-c', 'echo Starting post-install hook && sleep 20 && echo Post-install hook completed']
  restartPolicy: Never
```

The hooks executed in the following sequence:
1. Pre-install hook ran first (weight: -5)
   - Started execution
   - Transitioned from pending to running state
   - Ran for 20 seconds
   - Completed successfully and was automatically deleted

2. Main deployment was installed
   - Created service account, service, and deployment resources
   - Started the main application pod

3. Post-install hook ran last (weight: 5)
   - Started execution after main deployment
   - Transitioned from pending to running state
   - Ran for 20 seconds
   - Completed successfully and was automatically deleted

Both hooks were configured with the `hook-succeeded` delete policy, ensuring they were automatically cleaned up after successful execution. This helps maintain a clean cluster state and prevents accumulation of completed hook pods. The debug output shows the complete lifecycle of both hooks, from creation through execution to automatic cleanup. 