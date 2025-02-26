# Helm Deployment Documentation

## Overview
This document contains information about the Helm deployment of our Python and Node.js applications.

## Chart Structure
I have created three Helm charts:
1. `python-app` - Chart for the Python application
2. `nodejs-app` - Chart for the Node.js application
3. `common-lib` - Library chart containing common templates

## Library Chart
The common-lib chart provides shared templates for both applications:
- Common labels template that can be used across all resources

## Helm Hooks
Both applications implement:
- Pre-install hooks that run before the main deployment
- Post-install hooks that run after the main deployment
- Hook delete policy to clean up hook pods after successful execution

## Deployment Status
To check the status of the deployments, run:
```bash
$ kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/nodejs-app-75f6b7b478-jgg7g   1/1     Running   0          17s
pod/python-app-85f54f78b-xr2r6    1/1     Running   0          45s

NAME                         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes           ClusterIP   10.96.0.1       <none>        443/TCP          115m
service/nodejs-app           NodePort    10.99.179.87    <none>        3000:32036/TCP   17s
service/nodejs-app-service   NodePort    10.101.62.122   <none>        80:31267/TCP     114m
service/python-app           NodePort    10.96.31.193    <none>        5000:31220/TCP   45s
service/python-app-service   NodePort    10.109.161.94   <none>        80:31291/TCP     114m
```

## Hook Status
The pre-install and post-install hooks were executed successfully and were automatically cleaned up due to the `hook-delete-policy: hook-succeeded` setting in our hook configurations.

## Hook Troubleshooting
The following commands were run to verify the hooks:

### Helm Lint
```bash
$ helm lint python-app/
==> Linting python-app/
[INFO] Chart.yaml: icon is recommended
1 chart(s) linted, 0 chart(s) failed

$ helm lint nodejs-app/
==> Linting nodejs-app/
[INFO] Chart.yaml: icon is recommended
1 chart(s) linted, 0 chart(s) failed
```

### Dry Run Installation
Both applications' charts were tested with `helm install --dry-run`. The output showed that:
- Pre-install and post-install hooks are properly configured
- Hook delete policies are set correctly
- Service and deployment configurations are valid
- All required Kubernetes resources will be created

### Hook Status
The hooks were configured with the following features:
- Pre-install hooks run with weight "-5" (ensuring they run first)
- Post-install hooks run with weight "5" (ensuring they run after deployment)
- Both hooks use the `hook-succeeded` delete policy for automatic cleanup
- Simple "sleep 10" commands are used as placeholder operations

## Accessing the Applications
To access the Python application:
```bash
minikube service python-app
```

To access the Node.js application:
```bash
minikube service nodejs-app
```

## Library Chart Usage
Both applications are using the common library chart (`common-lib`) which provides shared templates for labels and other common configurations. This reduces duplication and maintains consistency across our deployments.
