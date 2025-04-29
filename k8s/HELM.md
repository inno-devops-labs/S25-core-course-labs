# Helm

### Install helm

![img.png](screenshots-helm/install_helm.png)

### Create Helm Chart

1. Create Helm chart for my python app
```bash
helm create app-python-helm
Creating app-python-helm
```

2. Repository, port and tag in values.yaml
```bash
image:
  repository: darrpyy/devops
  tag: "latest"
  
service:
  port: 8001
```

3. Install helm chart
```bash
helm install app-python-helm ./app-python-helm

NAME: app-python-helm
LAST DEPLOYED: Tue Apr 29 16:02:29 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=app-python-helm,app.kubernetes.io/instance=app-python-helm" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
```

4. See Dashboard
надо картинку, у меня не открылось ничего

5. Checking application using `minikube service`
```bash
minikube service app-python-helm
```
+ картинка

6. Checking the pods and services
```bash
kubectl get pods,svc
```

### Helm chart hooks

