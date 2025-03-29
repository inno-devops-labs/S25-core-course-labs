# K8S

## Cluster setup

I used [kind](https://kind.sigs.k8s.io/) to set up local cluster:
```bash
➜  ~ kind create cluster --name devops-lab-9
Creating cluster "devops-lab-9" ...
 ✓ Ensuring node image (kindest/node:v1.30.0) 🖼
 ✓ Preparing nodes 📦
 ✓ Writing configuration 📜
 ✓ Starting control-plane 🕹️
 ✓ Installing CNI 🔌
 ✓ Installing StorageClass 💾
Set kubectl context to "kind-devops-lab-9"
You can now use your cluster with:

kubectl cluster-info --context kind-devops-lab-9

Thanks for using kind! 😊
```

## Deployment

We apply manifests to deploy app into cluster:
```bash
➜  k8s git:(lab-9) ✗ k apply -f pyapp
deployment.apps/py-app-deployment created
ingress.networking.k8s.io/py-app-ingress created
service/py-app-service created
```

After some time we can list created resources:
```bash
➜  k8s git:(lab-9) ✗ k get pods,svc
NAME                                     READY   STATUS    RESTARTS   AGE
pod/py-app-deployment-58cd5444cf-7ljnd   1/1     Running   0          20s
pod/py-app-deployment-58cd5444cf-858q6   1/1     Running   0          20s
pod/py-app-deployment-58cd5444cf-bgfk5   1/1     Running   0          20s

NAME                     TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)    AGE
service/kubernetes       ClusterIP   10.96.0.1     <none>        443/TCP    15m
service/py-app-service   ClusterIP   10.96.24.66   <none>        8000/TCP   20s
```

Then we will port-forward our service to local machine:
```bash
➜  k8s git:(lab-9) ✗ k port-forward services/py-app-service 8000
Forwarding from 127.0.0.1:8000 -> 8000
Forwarding from [::1]:8000 -> 8000
Handling connection for 8000
```

After this, it can be accessed using `curl`:
```bash
➜  ~ curl http://localhost:8000/time
{"time":"2025-02-23T14:15:45.599888+03:00"}%
```

## Note on ingress
It will not work until we connect some ingress-controller for it.

## Extra app

For extra application everything is the same as for python app.
