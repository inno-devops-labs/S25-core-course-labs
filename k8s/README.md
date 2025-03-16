# Kubernetes

## Lab 9: Introduction to Kubernetes

## Task 1: Kubernetes Setup and Basic Deployment

In this task, I:

- installed `kubectl` and `minikube` for managing Kubernetes:
  ![which_kubectl_minikube.png](screenshots/which_kubectl_minikube.png)
- created a  `moscow-time-app` `Deployment` for `app_python`
  with `nshlyakhtin/devops:lab8-app-python-amd64` Docker image from Docker Hub:
  ![kubectl_created_deployment.png](screenshots/kubectl_created_deployment.png)
- created a `Service` to access application from outside k8s cluster network:
  ![kubectl_created_service.png](screenshots/kubectl_created_service.png)
  ![minikube_service_moscow_time_app.png](screenshots/minikube_service_moscow_time_app.png)
  ![moscow_time_app.png](screenshots/moscow_time_app.png)
- removed the created `Deployment` and `Service` resources:
  ![remove_resources.png](screenshots/remove_resources.png)

## Task 2: Declarative Kubernetes Manifests

In this task I created a `Deployment` and `Service` with manifest files:

![create_deployment_and_service_with_manifest.png](screenshots/create_deployment_and_service_with_manifest.png)
![minikube_tunnel.png](screenshots/minikube_tunnel.png)
![minikube_tunnel_output.png](screenshots/minikube_tunnel_output.png)

## Bonus Task: Additional Configuration and Ingress

In this task I added the `Deployment` and `Service` manifest files for my app_go crypto-price-tracker app
and added `Ingress` manifest to expose 2 apps (app_python and app_go) from k8s cluster network:

![2_apps_deployment.png](screenshots/2_apps_deployment.png)

The apps can be accessed with `localhost` base URL and `/time` endpoint to access `moscow-time-app`
or `/crypto/price` to access `crypto-price-tracker`. It is important to note that applications are accessed
through `minikube tunnel` because of `Docker Desktop` limitations on `MacOS`:

![app_python_ingress.png](screenshots/app_python_ingress.png)

![app_go_ingress.png](screenshots/app_go_ingress.png)
