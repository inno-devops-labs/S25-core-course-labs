# Kubernetes Setup Report

## Task1 Setup and Deployment 

- Installed minikube and kubectl : 
![which_kubectl_minikube.png](screenshots/which_kubectl_minikube.png)

- Created `moscow-time-app` Deployment with the use of image `theanushervon/moscow_time:latest` from DockerHub
![kubectl_deployment_created.png](screenshots/kubectl_deployment_created.png)

- Verification of deployment
![verify_deployment.png](screenshots/verify_deployment.png)

- created a Service to access application from outside k8s cluster network
![kubectl_created_service.png.png](screenshots/kubectl_created_service.png.png)
![minikube_service.png](screenshots/minikube_service.png)
![time.png](screenshots/time.png)

- Removed Deployment and Service resources
![delete_service_deployment.png](screenshots/delete_service_deployment.png)

## Task2 Declarative Kubernetes Manifests

- Created `deployment` and `service` manifests

- Output of `kubectl get pods, svc`
![deployment_output.png](screenshots/deployment_output.png)

- Output of `minikube service --all` and its result 
![minikube_service_all.png](screenshots/minikube_service_all.png)
![time2.png](screenshots/time2.png)

- Cleanup resources: 
![cleanup_resources.png](screenshots/cleanup_resources.png)