# StatefulSet Implementation for Python App

This document provides information about the StatefulSet implementation for the Python application.

## Implementation Overview

The StatefulSet provides the following features for the Python application:
- Stable, unique network identifiers for each pod
- Persistent storage for visit count data
- Ordered, graceful deployment and scaling
- Ordered, automated rolling updates

## Key Components

1. **StatefulSet**: Manages pod creation with stable identities
2. **Headless Service**: Enables direct DNS access to individual pods
3. **Persistent Volumes**: Stores visit counter data persistently
4. **Health Probes**: Ensures pods are healthy and ready to serve requests

## Directory Structure

```
k8s/python-app-chart/
├── templates/
│   ├── statefulset.yaml       # StatefulSet definition
│   ├── service.yaml           # Headless service when enabled
│   └── other templates...
├── values.yaml                # Configuration values
└── Chart.yaml                 # Chart metadata
```

## Configuration Options

The StatefulSet implementation adds the following configuration options in `values.yaml`:

```yaml
statefulSet:
  enabled: true                # Enable StatefulSet instead of Deployment
  podManagementPolicy: Parallel  # Pod management policy
  updateStrategy: RollingUpdate  # Update strategy
  persistence:
    enabled: true              # Enable persistent storage
    storageClassName: ""       # StorageClass name
    accessModes:
      - ReadWriteOnce          # Access mode for PVCs
    size: 1Gi                  # Storage size
    mountPath: /data           # Mount path in containers
```

## Testing

1. Test with dry-run:
   ```bash
   helm install --dry-run --debug python-stateful ./k8s/python-app-chart
   ```

2. Deploy the chart:
   ```bash
   helm install python-stateful ./k8s/python-app-chart
   ```

3. Check the status:
   ```bash
   kubectl get statefulsets,pods,services,pvc
   ```

4. Access the application:
   ```bash
   minikube service python-stateful-python-app-chart
   ```

5. Test persistent storage:
   ```bash
   # Delete a pod
   kubectl delete pod python-stateful-python-app-chart-0
   
   # Check if data persists after pod recreation
   kubectl exec python-stateful-python-app-chart-0 -- cat /data/visits
   ```

6. Test DNS resolution:
   ```bash
   kubectl exec python-stateful-python-app-chart-0 -- nslookup python-stateful-python-app-chart-1.python-stateful-python-app-chart
   ```

## Cleaning Up

```bash
helm uninstall python-stateful
kubectl delete pvc --selector=app.kubernetes.io/instance=python-stateful
``` 