# Helm Setup

1. Installing helm

![helm_install_piton](assets/helm_install_piton.png)

2. Accessing dashboard

> minikube dashboard
>
> minikube service --all

* Deployments
![helm_deployment](assets/helm_deployment.png)

* Pods
![helm_pods](assets/helm_pods.png)

* Services
![helm_services](assets/helm_services.png)

3. Checking all pods and services

![helm_pods_services](assets/pods_svc.png)

4. Installing hooks

![helm_install_hooks](assets/helm_install_hooks_piton.png)

5. Lint with hooks

![lint_with_hooks](assets/lint_with_hooks.png)

6. Get all pods (with hooks)

![helm_hook_pods](assets/helm_hook_pods.png)

7. Describe hooks

![helm_describe_hooks](assets/describe_hooks.png)

8. Add delete policy

```yml
annotations:
    "helm.sh/hook-delete-policy": hook-succeeded
```

9. Checking if delete policy is applied (pre and post install hooks must not be listed)

![after_delete_policy](assets/helm_after_delete_policy.png)
