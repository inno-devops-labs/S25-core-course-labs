# Lab 10: Introduction to Helm

## Overview

In this lab, you will become familiar with Helm, set up a local development environment, and generate manifests for your application.

## Task 1: Helm Setup and Chart Creation

**6 Points:**

1. Learn About Helm:
   - Begin by exploring the architecture and concepts of Helm:
     - [Helm Architecture](https://helm.sh/docs/topics/architecture/)
     - [Understanding Helm Charts](https://helm.sh/docs/topics/charts/)

2. Install Helm:
   - Install Helm using the instructions provided:
     - [Helm Installation](https://helm.sh/docs/intro/install/)
     - [Chart Repository Initialization](https://helm.sh/docs/intro/quickstart/#initialize-a-helm-chart-repository)

3. Create Your Own Helm Chart:
   - Generate a Helm chart for your application.
     - Inside the `k8s` folder, create a Helm chart template by using the command `helm create your-app`.
     - Replace the default repository and tag inside the `values.yaml` file with your repository name.
     - Modify the `containerPort` setting in the `deployment.yml` file.
     - If you encounter issues with `livenessProbe` and `readinessProbe`, you can comment them out.

   > For troubleshooting, you can use the `minikube dashboard` command.

4. Install Your Helm Chart:
   - Install your custom Helm chart and ensure that all services are healthy. Verify this by checking the `Workloads` page in the Minikube dashboard.

5. Access Your Application:
   - Confirm that your application is accessible by running the `minikube service your_service_name` command.

6. Create a HELM.md File:
   - Construct a `HELM.md` file and provide the output of the `kubectl get pods,svc` command within it.

## Task 2: Helm Chart Hooks

**4 Points:**

1. Learn About Chart Hooks:
   - Familiarize yourself with [Helm Chart Hooks](https://helm.sh/docs/topics/charts_hooks/).

2. Implement Helm Chart Hooks:
   - Develop pre-install and post-install pods within your Helm chart, without adding any complex logic (e.g., use "sleep 20"). You can refer to [Example 1 in the guide](https://www.golinuxcloud.com/kubernetes-helm-hooks-examples/).

3. Troubleshoot Hooks:
   - Execute the following commands to troubleshoot your hooks:
     1. `helm lint <your_chart_name>`
     2. `helm install --dry-run helm-hooks <your_chart_name>`
     3. `kubectl get po`

4. Provide Output:
   - Execute the following commands and include their output in your report:
     1. `kubectl get po`
     2. `kubectl describe po <preinstall_hook_name>`
     3. `kubectl describe po <postinstall_hook_name>`

5. Hook Delete Policy:
   - Implement a hook delete policy to remove the hook once it has executed successfully.

**List of Requirements:**

- Helm Chart with Hooks implemented, including the hook delete policy.
- Output of the `kubectl get pods,svc` command in `HELM.md`.
- Output of all commands from the step 4 of Task 2 in `HELM.md`.

## Bonus Task: Helm Library Chart

**To Earn 2.5 Additional Points:**

1. Helm Chart for Extra App:
   - Prepare a Helm chart for an additional application.

2. Helm Library Charts:
   - Get acquainted with [Helm Library Charts](https://helm.sh/docs/topics/library_charts/).

3. Create a Library Chart:
   - Develop a simple library chart that includes a "labels" template. You can follow the steps outlined in [the Using Library Charts guide](https://austindewey.com/2020/08/17/how-to-reduce-helm-chart-boilerplate-with-library-charts/). Use this library chart for both of your applications.

### Guidelines

- Ensure your documentation is clear and well-structured.
- Include all the necessary components.
- Follow appropriate file and folder naming conventions.
- Create and participate in PRs for the peer review process.
- Create pull requests (PRs) as needed: from your fork to the main branch of this repository, and from your fork's branch to your fork's master branch.

> Note: Detailed documentation is crucial to ensure that your Helm deployment and hooks function as expected. Engage with the bonus tasks to further enhance your understanding and application deployment skills.
