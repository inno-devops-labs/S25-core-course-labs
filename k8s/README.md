# Task 1: Kubernetes Setup and Basic Deployment

## Step 1: Install kubectl and Minikube
Following the [documentation](https://kubernetes.io/docs/tasks/tools/) I installed `kubectl` and `minikube` successfully. 
![](../scr/kubectl-version.png)

## Step 2: Deploy the Application
To create a Kubernetes Deployment for the application, I configured a [deployment.yaml](service.yaml) file.

### Apply the Deployment:
```bash
kubectl apply -f deployment.yaml
```
### Verify Deployment:
```bash
kubectl get deployments
```
![](../scr/deployment-apply.png)

## Step 3: Expose the Application with a Service
To expose the application using a Kubernetes Service, I configured a [service.yaml](service.yaml) file.

### Apply the Service:
```bash
kubectl apply -f service.yaml
```
### Verify Service:
To know the URL that we can open to access the application:
```bash
minikube service flask-app-service --url
```

![](../scr/service-apply.png)

## Step 5: Access the Application
![](../scr/app-kube.png)

## Step 6: Cleanup Kubernetes Resources

### Delete the Deployment:
```bash
kubectl delete -f deployment.yaml
```
### Delete the Service:
```bash
kubectl delete -f service.yaml
```

![](../scr/kube-cleanup.png)

## Output: `kubectl get pods,svc`
![](..//scr/kube-command.png)

## Output: `minikube service --all`
![](../scr/kube-services.png)