# Introduction to Kubernetes

## Task 1: Kubernetes Setup and Basic Deployment

### Deploy Application

 ```bash
   > minikube start
```

 ```bash
   > kubectl create deployment app-node --image=karimnasybul/app_python 

   deployment.apps/app-node created
 ```

 ```bash
   > kubectl get deployments

   NAME       READY   UP-TO-DATE   AVAILABLE   AGE
   app-node   1/1     1            1           35s
 ```

 ```bash
   > kubectl get pods   

   NAME                        READY   STATUS    RESTARTS   AGE
   app-node-787c6f5ccd-47q5w   1/1     Running   0          2m40s
 ```

### Access Application

 ```bash
   > kubectl expose deployment app-node --type=LoadBalancer --port=8000

   service/app-node exposed
 ```

 ```bash
   > kubectl get pods,svc

   NAME                            READY   STATUS    RESTARTS   AGE
   pod/app-node-8645984d45-9psfm   1/1     Running   0          6m37s

   NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
   service/app-node     LoadBalancer   10.104.55.238   <pending>     8000:32083/TCP   6m13s       
   service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          20h
 ```

 ```bash
   > minikube service app-node
 ```

### Cleanup

 ```bash
   > kubectl delete svc,deployments app-node

   service "app-node" deleted
   deployment.apps "app-node" deleted
 ```

## Task 2: Declarative Kubernetes Manifests

### Manifest Files for Application

Created a `deployment.yml` manifest file with 3 replicas:

Apply the manifest `deployment.yml`:

 ```bash
   > kubectl apply -f k8s/deployment.yml
   deployment.apps/app-python-deployment created
 ```

### Service Manifest

Developed a `service.yml` manifest file:

Deploy the service manifest:

 ```bash
   > kubectl apply -f k8s/service.yml
   service/app-python-service created
 ```

### Output

 ```bash
   > kubectl get pods,svc
   NAME                                         READY   STATUS    RESTARTS      AGE
   pod/app-python-deployment-64759766c8-46vx2   1/1     Running   1 (42s ago)   97s
   pod/app-python-deployment-64759766c8-pk9bv   1/1     Running   1 (42s ago)   97s
   pod/app-python-deployment-64759766c8-th28p   1/1     Running   1 (42s ago)   97s
   NAME                         TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
   service/app-python-service   LoadBalancer   10.108.28.55   <pending>     8000:30488/TCP   79s
   service/kubernetes           ClusterIP      10.96.0.1      <none>        443/TCP          2d16h
 ```

 ```bash
   > minikube service --all
   🎉  Opening service default/app-python-service in default browser...
   🎉  Opening service default/kubernetes in default browser...
 ```