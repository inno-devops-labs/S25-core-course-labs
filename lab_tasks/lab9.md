# Lab 9: Introduction to Kubernetes

## Overview

In this lab, you will explore Kubernetes, set up a local development environment, and create manifests for your application.

## Task 1: Kubernetes Setup and Basic Deployment

**6 Points:**

1. Learn About Kubernetes:
   - Begin by studying the fundamentals of Kubernetes:
     - [What is Kubernetes](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/)
     - [Kubernetes Components](https://kubernetes.io/docs/concepts/overview/components/)

2. Install Kubernetes Tools:
   - Install `kubectl` and `minikube`, essential tools for managing Kubernetes.
     - [Kubernetes Tools](https://kubernetes.io/docs/tasks/tools/)

3. Deploy Your Application:
   - Deploy your application within the Minikube cluster using the `kubectl create` command. Create a `Deployment` resource for your app.
     - [Example of Creating a Deployment](https://kubernetes.io/docs/tutorials/hello-minikube/#create-a-deployment)
     - [Deployment Overview](https://kubernetes.io/docs/tutorials/kubernetes-basics/deploy-app/deploy-intro/)

4. Access Your Application:
   - Make your application accessible from outside the Kubernetes virtual network. Achieve this by creating a `Service` resource.
     - [Example of Creating a Service](https://kubernetes.io/docs/tutorials/hello-minikube/#create-a-service)
     - [Service Overview](https://kubernetes.io/docs/tutorials/kubernetes-basics/expose/expose-intro/)

5. Create a Kubernetes Folder:
   - Establish a `k8s` folder within your repository.
   - Create a `README.md` report within this folder and include the output of the `kubectl get pods,svc` command.

6. Cleanup:
   - Remove the `Deployment` and `Service` resources that you created, maintaining a tidy Kubernetes environment.

## Task 2: Declarative Kubernetes Manifests

**4 Points:**

1. Manifest Files for Your Application:
   - As a more efficient and structured approach, employ configuration files to deploy your application.
   - Create a `deployment.yml` manifest file that describes your app's deployment, specifying at least 3 replicas.
     - [Kubernetes Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
     - [Declarative Management of Kubernetes Objects Using Configuration Files](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/declarative-config/)

2. Service Manifest:
   - Develop a `service.yml` manifest file for your application.

3. Manifest Files in `k8s` Folder:
   - Store these manifest files in the `k8s` folder of your repository.
   - Additionally, provide the output of the `kubectl get pods,svc` command in the `README.md` report.
   - Include the output of the `minikube service --all` command and the result from your browser, with a screenshot demonstrating that the IP matches the output of `minikube service --all`.

## Bonus Task: Additional Configuration and Ingress

**To Earn 2.5 Additional Points:**

1. Manifests for Extra App:
   - Create `deployment` and `service` manifests for an additional application.

2. Ingress Manifests:
   - Construct [Ingress manifests](https://kubernetes.io/docs/tasks/access-application-cluster/ingress-minikube/) for your applications.

3. Application Availability Check:
   - Utilize `curl` or a similar tool to verify the availability of your applications. Include the output in the report.

**Guidelines:**

- Maintain a clear and well-structured `README.md` document.
- Ensure that all required components are included.
- Adhere to file and folder naming conventions.
- Create and participate in PRs to facilitate the peer review process.
- Create pull requests (PRs) as needed: from your fork to the main branch of this repository, and from your fork's branch to your fork's master branch.

> Note: Detailed documentation is crucial to ensure that your Kubernetes deployment is fully functional and accessible. Engage with the bonus tasks to further enhance your understanding and application deployment skills.
