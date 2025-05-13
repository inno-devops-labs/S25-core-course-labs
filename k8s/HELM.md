# Using Helm charts

```bash
NAME: timeapp
LAST DEPLOYED: Fri Mar  7 12:08:40 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
```

```bash
➜  k8s git:(lab10) ✗ kubectl get pods
NAME                       READY   STATUS    RESTARTS   AGE
timeapp-75f8877cc9-7wqm6   1/1     Running   0          30s
timeapp-75f8877cc9-g2dp2   1/1     Running   0          30s
timeapp-75f8877cc9-xpqkp   1/1     Running   0          30s
```

```bash
➜  k8s git:(lab10) ✗ kubectl get pods,svc
NAME                           READY   STATUS    RESTARTS   AGE
pod/timeapp-75f8877cc9-7wqm6   1/1     Running   0          67s
pod/timeapp-75f8877cc9-g2dp2   1/1     Running   0          67s
pod/timeapp-75f8877cc9-xpqkp   1/1     Running   0          67s

NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP    4d1h
service/timeapp      ClusterIP   10.98.117.118   <none>        8080/TCP   67s
```

## Hooks

Running the hooks:

```bash
➜  k8s git:(lab10) ✗ helm install timeapp timeapp/ --debug
install.go:225: 2025-03-07 12:51:16.083326692 +0300 MSK m=+0.017964728 [debug] Original chart version: ""
install.go:242: 2025-03-07 12:51:16.083355336 +0300 MSK m=+0.017993362 [debug] CHART PATH: /home/ucat/Study/S25-core-course-labs/k8s/timeapp

client.go:142: 2025-03-07 12:51:16.157603238 +0300 MSK m=+0.092241264 [debug] creating 1 resource(s)
client.go:720: 2025-03-07 12:51:16.161303706 +0300 MSK m=+0.095941742 [debug] Watching for changes to Pod timeapp-pre-install with timeout of 5m0s
client.go:748: 2025-03-07 12:51:16.164933863 +0300 MSK m=+0.099571909 [debug] Add/Modify event for timeapp-pre-install: ADDED
client.go:807: 2025-03-07 12:51:16.164951406 +0300 MSK m=+0.099589442 [debug] Pod timeapp-pre-install pending
client.go:748: 2025-03-07 12:51:16.165154865 +0300 MSK m=+0.099792911 [debug] Add/Modify event for timeapp-pre-install: MODIFIED
client.go:807: 2025-03-07 12:51:16.165164192 +0300 MSK m=+0.099802228 [debug] Pod timeapp-pre-install pending
client.go:748: 2025-03-07 12:51:16.171209992 +0300 MSK m=+0.105848018 [debug] Add/Modify event for timeapp-pre-install: MODIFIED
client.go:807: 2025-03-07 12:51:16.171414593 +0300 MSK m=+0.106052629 [debug] Pod timeapp-pre-install pending
client.go:748: 2025-03-07 12:51:19.186988584 +0300 MSK m=+3.121626610 [debug] Add/Modify event for timeapp-pre-install: MODIFIED
client.go:809: 2025-03-07 12:51:19.187008581 +0300 MSK m=+3.121646617 [debug] Pod timeapp-pre-install running
client.go:748: 2025-03-07 12:51:39.249675817 +0300 MSK m=+23.184313843 [debug] Add/Modify event for timeapp-pre-install: MODIFIED
client.go:809: 2025-03-07 12:51:39.249693139 +0300 MSK m=+23.184331165 [debug] Pod timeapp-pre-install running
client.go:748: 2025-03-07 12:51:40.435095752 +0300 MSK m=+24.369733788 [debug] Add/Modify event for timeapp-pre-install: MODIFIED
client.go:802: 2025-03-07 12:51:40.435117392 +0300 MSK m=+24.369755418 [debug] Pod timeapp-pre-install succeeded
client.go:142: 2025-03-07 12:51:40.435183385 +0300 MSK m=+24.369821421 [debug] creating 2 resource(s)
client.go:142: 2025-03-07 12:51:40.473459244 +0300 MSK m=+24.408097280 [debug] creating 1 resource(s)
client.go:720: 2025-03-07 12:51:40.47670829 +0300 MSK m=+24.411346326 [debug] Watching for changes to Pod timeapp-post-install with timeout of 5m0s
client.go:748: 2025-03-07 12:51:40.477546643 +0300 MSK m=+24.412184679 [debug] Add/Modify event for timeapp-post-install: ADDED
client.go:807: 2025-03-07 12:51:40.477555469 +0300 MSK m=+24.412193495 [debug] Pod timeapp-post-install pending
client.go:748: 2025-03-07 12:51:40.480030683 +0300 MSK m=+24.414668719 [debug] Add/Modify event for timeapp-post-install: MODIFIED
client.go:807: 2025-03-07 12:51:40.480043207 +0300 MSK m=+24.414681233 [debug] Pod timeapp-post-install pending
client.go:748: 2025-03-07 12:51:40.487465983 +0300 MSK m=+24.422104009 [debug] Add/Modify event for timeapp-post-install: MODIFIED
client.go:807: 2025-03-07 12:51:40.487473898 +0300 MSK m=+24.422111924 [debug] Pod timeapp-post-install pending
client.go:748: 2025-03-07 12:51:47.299382139 +0300 MSK m=+31.234020175 [debug] Add/Modify event for timeapp-post-install: MODIFIED
client.go:809: 2025-03-07 12:51:47.299403308 +0300 MSK m=+31.234041334 [debug] Pod timeapp-post-install running
client.go:748: 2025-03-07 12:52:07.375279699 +0300 MSK m=+51.309917735 [debug] Add/Modify event for timeapp-post-install: MODIFIED
client.go:809: 2025-03-07 12:52:07.375309835 +0300 MSK m=+51.309947861 [debug] Pod timeapp-post-install running
client.go:748: 2025-03-07 12:52:08.584209251 +0300 MSK m=+52.518847287 [debug] Add/Modify event for timeapp-post-install: MODIFIED
client.go:802: 2025-03-07 12:52:08.58423015 +0300 MSK m=+52.518868186 [debug] Pod timeapp-post-install succeeded
NAME: timeapp
LAST DEPLOYED: Fri Mar  7 12:51:16 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
USER-SUPPLIED VALUES:
{}
```

Description:

```bash
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
```
