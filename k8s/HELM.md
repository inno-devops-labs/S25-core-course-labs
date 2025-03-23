# Helm Chart Documentation

## Overview
This document outlines the Helm chart setup for the Python application deployment in Kubernetes.

## Chart Structure
The chart is located in `k8s/python-app-chart` and includes:
- Deployment with 3 replicas
- Service of type NodePort
- Pre-install and Post-install hooks
- Volume for logs

## Installation

To install the chart:

```bash
# From the k8s directory
helm install python-app ./python-app-chart
```

To validate the chart:

```bash
helm lint python-app-chart
helm install --dry-run python-app-chart
```

## Hooks Implementation

The chart implements two hooks:
1. Pre-install hook - runs before installation
2. Post-install hook - runs after installation

Both hooks have the `hook-succeeded` delete policy, which means they will be removed after successful execution.

## Command Outputs

After installation, the output of `kubectl get pods,svc`:

```
NAME                                               READY   STATUS    RESTARTS   AGE
pod/python-app-python-app-chart-7c76557cdc-bncjz   1/1     Running   0          8m18s
pod/python-app-python-app-chart-7c76557cdc-d4b5l   1/1     Running   0          8m18s
pod/python-app-python-app-chart-7c76557cdc-h8dtl   1/1     Running   0          8m18s

NAME                                  TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
service/kubernetes                    ClusterIP   10.96.0.1       <none>        443/TCP        6h25m
service/python-app-python-app-chart   NodePort    10.98.179.202   <none>        80:31010/TCP   8m19s
```

### Service Access

The application can be accessed via:

```
minikube service python-app-python-app-chart

|-----------|-----------------------------|-------------|---------------------------|
| NAMESPACE |            NAME             | TARGET PORT |            URL            |
|-----------|-----------------------------|-------------|---------------------------|
| default   | python-app-python-app-chart | http/80     | http://192.168.49.2:31010 |
|-----------|-----------------------------|-------------|---------------------------|
```

### Hook Outputs

The pre-install and post-install hooks executed successfully and were automatically removed due to the `hook-succeeded` delete policy. This was confirmed by checking for completed pods:

```
kubectl get pods -A --field-selector=status.phase==Succeeded
No resources found
```

This confirms that the hooks ran successfully and were cleaned up as expected. 