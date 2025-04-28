# Lab 11: Kubernetes Secrets and Hashicorp Vault

## Overview

In this lab, you will learn how to manage sensitive data, such as passwords, tokens, or keys, within Kubernetes. Additionally, you will configure CPU and memory limits for your application.

## Task 1: Kubernetes Secrets and Resource Management

**6 Points:**

1. Create a Secret Using `kubectl`:
   - Learn about Kubernetes Secrets and create a secret using the `kubectl` command:
     - [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)
     - [Managing Secrets with kubectl](https://kubernetes.io/docs/tasks/configmap-secret/managing-secret-using-kubectl/#decoding-secret)

2. Verify and Decode Your Secret:
   - Confirm and decode the secret, then create an `11.md` file within the `k8s` folder. Provide the output of the necessary commands inside this file.

3. Manage Secrets with Helm:
   - Use Helm to manage your secrets.
   - Create a `secrets.yaml` file in the `templates` folder.
   - Define a `secret` object within this YAML file.
   - Add an `env` field to your `Deployment`. The path to update is: `spec.template.spec.containers.env`.

     > Refer to this [Helm Secrets Video](https://www.youtube.com/watch?v=hRSlKRvYe1A) for guidance.

   - Update your Helm deployment as instructed in the video.
   - Retrieve the list of pods using the command `kubectl get po`. Use the name of the pod as proof of your success within the report.
   - Verify your secret inside the pod, for example: `kubectl exec demo-5f898f5f4c-2gpnd -- printenv | grep MY_PASS`. Share this output in `11.md`.

## Task 2: Vault Secret Management System

**4 Points:**

1. Install Vault Using Helm Chart:
   - Install Vault using a Helm chart. Follow the steps provided in this guide:
     - [Vault Installation Guide](https://developer.hashicorp.com/vault/tutorials/kubernetes/kubernetes-sidecar#install-the-vault-helm-chart)

2. Follow the Tutorial with Your Helm Chart:
   - Adapt the tutorial to work with your Helm chart, including the following steps:
     - [Set a Secret in Vault](https://developer.hashicorp.com/vault/tutorials/kubernetes/kubernetes-sidecar#set-a-secret-in-vault)
     - [Configure Kubernetes Authentication](https://developer.hashicorp.com/vault/tutorials/kubernetes/kubernetes-sidecar#configure-kubernetes-authentication)
     - Be cautious with the service account. If you used `helm create ...`, it will be created automatically. In the guide, they create it manually.
       - [Manually Define a Kubernetes Service Account](https://developer.hashicorp.com/vault/tutorials/kubernetes/kubernetes-sidecar#define-a-kubernetes-service-account)

3. Implement Vault Secrets in Your Helm Chart:
   - Use the steps from the guide as an example for your Helm chart:
     - [Update values.yaml](https://developer.hashicorp.com/vault/tutorials/kubernetes/kubernetes-sidecar#launch-an-application)
     - [Add Labels](https://developer.hashicorp.com/vault/tutorials/kubernetes/kubernetes-sidecar#inject-secrets-into-the-pod)
   - Test to ensure your credentials are injected successfully. Use the `kubectl exec -it <your_app> -- bash` command to access the container. Verify the injected secrets using `cat /path/to/your/secret` and `df -h`. Share the output in the `11.md` report.
   - Apply a template as described in the guide. Test the updates as you did in the previous step and provide the outputs in `11.md`.

**List of Requirements:**

- Proof of work with a secret in `11.md` for the Task 1 - steps 2 and 3.
- `secrets.yaml` file.
- Resource requests and limits for CPU and memory.
- Vault configuration implemented, with proofs in `11.md`.

## Bonus Task: Resource Management and Environment Variables

**2.5 Points:**

1. Read About Resource Management:
   - Familiarize yourself with resource management in Kubernetes:
     - [Resource Management](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)

2. Set Up Requests and Limits for CPU and Memory for Both Helm Charts:
   - Configure resource requests and limits for CPU and memory for your application.
   - Test to ensure these configurations work correctly.

3. Add Environment Variables for Your Containers for Both Helm Charts:
   - Read about Kubernetes environment variables:
     - [Kubernetes Environment Variables](https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-container/)
   - Update your Helm chart with several environment variables using named templates. Move these variables to the `_helpers.tpl` file:
     - [Helm Named Templates](https://helm.sh/docs/chart_template_guide/named_templates/)

### Guidelines

- Ensure that your documentation is clear and organized.
- Include all the necessary components.
- Follow appropriate file and folder naming conventions.
- Create pull requests (PRs) as needed: from your fork to the main branch of this repository, and from your fork's branch to your fork's master branch.

> Note: Thorough documentation is essential to demonstrate your success in managing secrets and resource allocation in Kubernetes. Explore the bonus tasks to enhance your skills further.
