
## Task 1: Helm Setup and Chart Creation

Screenshots demonstrate that I successfully installed Helm, configured Helm Chart for `moscow-time-app`
and installed Helm Chart on my Minikube cluster:

- Created Helm Chart
![created_helm_chart.png](screenshots/created_helm_chart.png)

- Display of created Helm chart: 
![helm_chart.png](screenshots/helm_chart.png)
![time.png](screenshots/time.png)

- Output for `kubectl get pods, svc`
![get_pods_svc.png](screenshots/get_pods_svc.png)


## Task2: Helm Chart Hooks

### Output of commands: 

`helm lint moscow-time-app`
![linting.png](screenshots/linting.png)

`helm install --dry-run helm-hooks <your_chart_name>`
![dry_run.png](screenshots/dry_run.png)

`kubectl get po --watch`
![get_po-watch.png](screenshots/get_po-watch.png)

`kubectl describe po my-app-pre-install-hook`
![preinstall.png](screenshots/preinstall.png)
![preinstall2.png](screenshots/preinstall2.png)

`kubectl describe po my-app-post-install-hook`

![postinstall.png](screenshots/postinstall.png)
![postinstall2.png](screenshots/postinstall2.png)